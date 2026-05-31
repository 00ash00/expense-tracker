"""Tests for ExpenseService business logic."""

import pytest
from datetime import date
from unittest.mock import MagicMock

from src.models.expense import Category
from src.services.expense_service import ExpenseService


@pytest.fixture
def service():
    """Create a service with mock storage (no file I/O)."""
    mock_storage = MagicMock()
    mock_storage.load.return_value = []
    svc = ExpenseService(storage=mock_storage)
    return svc


def test_add_expense(service):
    expense = service.add(50.0, "food", "Pizza", "card")
    assert expense.amount == 50.0
    assert expense.category == Category.FOOD
    assert len(service.expenses) == 1


def test_add_multiple_expenses(service):
    service.add(10.0, "food", "Coffee", "cash")
    service.add(20.0, "transport", "Bus", "card")
    assert len(service.expenses) == 2


def test_list_all_empty(service):
    assert service.list_all() == []


def test_delete_existing(service):
    e = service.add(30.0, "bills", "Internet", "online")
    result = service.delete(e.id)
    assert result is True
    assert len(service.expenses) == 0


def test_delete_nonexistent(service):
    result = service.delete("nonexistent")
    assert result is False


def test_update_amount(service):
    e = service.add(100.0, "health", "Gym", "card")
    updated = service.update(e.id, amount=150.0)
    assert updated.amount == 150.0


def test_update_nonexistent(service):
    result = service.update("bad-id", amount=50.0)
    assert result is None


def test_search_by_description(service):
    service.add(10.0, "food", "Coffee at Starbucks", "card")
    service.add(20.0, "transport", "Bus ticket", "cash")
    results = service.search("starbucks")
    assert len(results) == 1
    assert results[0].description == "Coffee at Starbucks"


def test_search_no_results(service):
    service.add(10.0, "food", "Pizza", "card")
    assert service.search("xyz") == []


def test_filter_by_category(service):
    service.add(10.0, "food", "Lunch", "cash")
    service.add(50.0, "bills", "Electricity", "online")
    results = service.filter_by(category="food")
    assert len(results) == 1
    assert results[0].category == Category.FOOD


def test_filter_by_date_range(service):
    service.add(10.0, "food", "Jan lunch", "cash",
                expense_date=date(2024, 1, 15))
    service.add(20.0, "food", "Mar lunch", "cash",
                expense_date=date(2024, 3, 15))
    results = service.filter_by(date_from=date(2024, 2, 1),
                                date_to=date(2024, 12, 31))
    assert len(results) == 1


def test_statistics_empty(service):
    assert service.statistics() == {}


def test_statistics_basic(service):
    service.add(100.0, "food", "Groceries", "card")
    service.add(50.0, "transport", "Taxi", "cash")
    stats = service.statistics()
    assert stats["total"] == 150.0
    assert stats["count"] == 2
    assert stats["average"] == 75.0
