"""
Модуль: test_get_transactions_by_keyword
Данный модуль содержит модульные тесты для функции get_transactions_by_keyword из модуля src/services.

Тесты охватывают сценарии, при которых искомое ключевое слово найдено в описании, категории,
обработке ошибки файла не найден и других исключениях.

Функции:
- test_search_term_in_description: Тест на нахождение ключевого слова в описании транзакции.
- test_search_term_in_category: Тест на нахождение ключевого слова в категории транзакции.
- test_file_not_found_error: Тест обработки ошибки файла не найден.
- test_other_exceptions: Тест обработки других исключений.
"""

import json
import unittest
from typing import Any
from unittest.mock import patch

import pandas as pd

from src.services import get_transactions_by_keyword


@patch("pandas.read_excel")
def test_search_term_in_description(mock_read_excel: Any) -> None:
    mock_data = [{"description": "Visited a cafe", "category": "Food"}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    search_term = "cafe"
    expected_result = json.dumps(mock_data, indent=4)
    actual_result = get_transactions_by_keyword(search_term)

    assert actual_result == expected_result


@patch("pandas.read_excel")
def test_search_term_in_category(mock_read_excel: Any) -> None:
    mock_data = [{"description": "Lunch", "category": "Cafe"}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    search_term = "Cafe"
    expected_result = json.dumps(mock_data, indent=4)
    actual_result = get_transactions_by_keyword(search_term)

    assert actual_result == expected_result


@patch("pandas.read_excel")
def test_file_not_found_error(mock_read_excel: Any) -> None:
    mock_read_excel.side_effect = FileNotFoundError()
    search_term = "test"

    expected_result = json.dumps({"error": "Файл operations.xls не найден."}, indent=4, ensure_ascii=False)
    actual_result = get_transactions_by_keyword(search_term)

    assert actual_result == expected_result


@patch("pandas.read_excel")
def test_other_exceptions(mock_read_excel: Any) -> None:
    mock_read_excel.side_effect = Exception()
    search_term = "test"

    expected_result = json.dumps({"error": "Произошла ошибка: "}, indent=4, ensure_ascii=False)
    actual_result = get_transactions_by_keyword(search_term)

    assert actual_result == expected_result


if __name__ == "main":
    unittest.main()
