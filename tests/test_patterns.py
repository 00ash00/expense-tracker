"""Tests for Strategy and Factory patterns."""

import pytest
from datetime import date

from src.models.expense import Category, Expense, PaymentMethod
from src.patterns.factory import CsvExporter, ExporterFactory, JsonExporter
from src.patterns.strategy import SortByAmount, SortByCategory, SortByDate


def make_expense(amount, category, desc, d):
    return Expense(amount=amount, category=category,
                   description=desc, payment_method=PaymentMethod.CASH, date=d)


@pytest.fixture
def sample_expenses():
    return [
        make_expense(50.0, Category.FOOD, "Lunch", date(2024, 3, 1)),
        make_expense(200.0, Category.BILLS, "Rent", date(2024, 1, 1)),
        make_expense(15.0, Category.TRANSPORT, "Bus", date(2024, 2, 1)),
    ]


def test_sort_by_date(sample_expenses):
    result = SortByDate().sort(sample_expenses)
    dates = [e.date for e in result]
    assert dates == sorted(dates)


def test_sort_by_amount(sample_expenses):
    result = SortByAmount().sort(sample_expenses)
    assert result[0].amount == 200.0
    assert result[-1].amount == 15.0


def test_sort_by_category(sample_expenses):
    result = SortByCategory().sort(sample_expenses)
    cats = [e.category.value for e in result]
    assert cats == sorted(cats)


def test_factory_creates_json_exporter():
    exporter = ExporterFactory.create("json")
    assert isinstance(exporter, JsonExporter)


def test_factory_creates_csv_exporter():
    exporter = ExporterFactory.create("csv")
    assert isinstance(exporter, CsvExporter)


def test_factory_unknown_format():
    with pytest.raises(ValueError):
        ExporterFactory.create("xml")


def test_json_export_contains_data(sample_expenses):
    result = JsonExporter().export(sample_expenses)
    assert "Lunch" in result
    assert "food" in result


def test_csv_export_has_header(sample_expenses):
    result = CsvExporter().export(sample_expenses)
    assert "id,amount,category" in result
    assert "Lunch" in result


def test_bdd_given_expenses_when_export_json_then_valid(sample_expenses):
    """
    BDD Acceptance Test:
    Given a list of expenses
    When exported to JSON format
    Then the output is valid JSON with all records
    """
    import json
    result = JsonExporter().export(sample_expenses)
    data = json.loads(result)
    assert len(data) == 3


def test_bdd_given_expenses_when_sort_by_amount_then_descending(sample_expenses):
    """
    BDD Acceptance Test:
    Given a list of expenses with different amounts
    When sorted by amount
    Then expenses are returned in descending order
    """
    result = SortByAmount().sort(sample_expenses)
    amounts = [e.amount for e in result]
    assert amounts == sorted(amounts, reverse=True)


def test_bdd_given_no_expenses_when_export_then_empty_list(sample_expenses):
    """
    BDD Acceptance Test:
    Given an empty expense list
    When exported to JSON
    Then result is an empty JSON array
    """
    import json
    result = JsonExporter().export([])
    assert json.loads(result) == []
