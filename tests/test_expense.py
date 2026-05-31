"""
Tests for Expense model.
Black-box tests: derived from specification (what the system should do).
White-box tests: derived from code structure (branch/path coverage).
"""

from datetime import date
from src.models.expense import Expense, Category, PaymentMethod


# --- BLACK-BOX TESTS (derived from specification) ---

def test_bb_expense_creation_required_fields():
    """BB: Expense must store amount, category, description, payment_method."""
    e = Expense(
        amount=25.50,
        category=Category.FOOD,
        description="Lunch",
        payment_method=PaymentMethod.CARD,
    )
    assert e.amount == 25.50
    assert e.category == Category.FOOD
    assert e.description == "Lunch"
    assert e.payment_method == PaymentMethod.CARD


def test_bb_expense_default_date_is_today():
    """BB: Expense date defaults to today when not specified."""
    e = Expense(25.0, Category.FOOD, "test", PaymentMethod.CASH)
    assert e.date == date.today()


def test_bb_expense_id_is_auto_generated():
    """BB: Each expense gets a unique ID automatically."""
    e1 = Expense(10.0, Category.FOOD, "a", PaymentMethod.CASH)
    e2 = Expense(20.0, Category.FOOD, "b", PaymentMethod.CASH)
    assert e1.id != e2.id


def test_bb_expense_to_dict_has_all_fields():
    """BB: to_dict must include all 6 required fields."""
    e = Expense(100.0, Category.BILLS, "Electricity", PaymentMethod.ONLINE,
                date=date(2024, 1, 15))
    d = e.to_dict()
    assert set(d.keys()) == {"id", "amount", "category", "description",
                             "payment_method", "date"}


def test_bb_expense_from_dict_roundtrip():
    """BB: Expense serialized to dict and back must be equal."""
    original = Expense(50.0, Category.TRANSPORT, "Bus", PaymentMethod.CASH,
                       date=date(2024, 3, 10))
    restored = Expense.from_dict(original.to_dict())
    assert restored.amount == original.amount
    assert restored.category == original.category
    assert restored.date == original.date


# --- WHITE-BOX TESTS (derived from code structure) ---

def test_wb_str_format_contains_key_fields():
    """WB: __str__ must contain id, date, category, amount, description."""
    e = Expense(42.0, Category.HEALTH, "Doctor visit", PaymentMethod.CARD,
                date=date(2024, 5, 1))
    s = str(e)
    assert e.id in s
    assert "health" in s
    assert "42.00" in s
    assert "Doctor visit" in s


def test_wb_category_enum_values():
    """WB: All category enum values match expected strings."""
    assert Category.FOOD.value == "food"
    assert Category.TRANSPORT.value == "transport"
    assert Category.ENTERTAINMENT.value == "entertainment"
    assert Category.BILLS.value == "bills"
    assert Category.HEALTH.value == "health"
    assert Category.OTHER.value == "other"


def test_wb_payment_method_enum_values():
    """WB: PaymentMethod enum covers all expected values."""
    assert PaymentMethod.CASH.value == "cash"
    assert PaymentMethod.CARD.value == "card"
    assert PaymentMethod.ONLINE.value == "online"


def test_wb_from_dict_parses_date_correctly():
    """WB: from_dict must parse ISO date string to date object."""
    data = {
        "id": "abc12345",
        "amount": 99.9,
        "category": "food",
        "description": "Dinner",
        "payment_method": "card",
        "date": "2024-06-15",
    }
    e = Expense.from_dict(data)
    assert e.date == date(2024, 6, 15)


def test_wb_to_dict_date_is_string():
    """WB: to_dict must convert date to ISO string, not leave as date object."""
    e = Expense(10.0, Category.OTHER, "misc", PaymentMethod.CASH,
                date=date(2024, 7, 4))
    d = e.to_dict()
    assert isinstance(d["date"], str)
    assert d["date"] == "2024-07-04"
