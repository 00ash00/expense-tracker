"""Business logic for expense management."""

from datetime import date
from typing import List, Optional

from src.models.expense import Category, Expense, PaymentMethod
from src.patterns.strategy import SortByDate, SortStrategy
from src.storage.json_storage import JsonStorage


class ExpenseService:
    """Manages the collection of expenses."""

    def __init__(self, storage: Optional[JsonStorage] = None):
        self.storage = storage or JsonStorage()
        self.expenses: List[Expense] = self.storage.load()

    def add(self, amount: float, category: str, description: str,
            payment_method: str, expense_date: Optional[date] = None) -> Expense:
        expense = Expense(
            amount=amount,
            category=Category(category),
            description=description,
            payment_method=PaymentMethod(payment_method),
            date=expense_date or date.today(),
        )
        self.expenses.append(expense)
        self.save()
        return expense

    def list_all(self, strategy: Optional[SortStrategy] = None) -> List[Expense]:
        strategy = strategy or SortByDate()
        return strategy.sort(self.expenses)

    def get_by_id(self, expense_id: str) -> Optional[Expense]:
        return next((e for e in self.expenses if e.id == expense_id), None)

    def update(self, expense_id: str, **kwargs) -> Optional[Expense]:
        expense = self.get_by_id(expense_id)
        if not expense:
            return None
        if "amount" in kwargs:
            expense.amount = float(kwargs["amount"])
        if "category" in kwargs:
            expense.category = Category(kwargs["category"])
        if "description" in kwargs:
            expense.description = kwargs["description"]
        if "payment_method" in kwargs:
            expense.payment_method = PaymentMethod(kwargs["payment_method"])
        if "date" in kwargs:
            expense.date = kwargs["date"]
        self.save()
        return expense

    def delete(self, expense_id: str) -> bool:
        expense = self.get_by_id(expense_id)
        if not expense:
            return False
        self.expenses.remove(expense)
        self.save()
        return True

    def search(self, keyword: str) -> List[Expense]:
        kw = keyword.lower()
        return [
            e for e in self.expenses
            if kw in e.description.lower() or kw in e.category.value.lower()
        ]

    def filter_by(self, category: Optional[str] = None,
                  date_from: Optional[date] = None,
                  date_to: Optional[date] = None) -> List[Expense]:
        results = self.expenses
        if category:
            results = [e for e in results if e.category.value == category]
        if date_from:
            results = [e for e in results if e.date >= date_from]
        if date_to:
            results = [e for e in results if e.date <= date_to]
        return results

    def statistics(self) -> dict:
        if not self.expenses:
            return {}
        by_category = {}
        for e in self.expenses:
            by_category[e.category.value] = (
                by_category.get(e.category.value, 0) + e.amount
            )
        total = sum(e.amount for e in self.expenses)
        return {
            "total": round(total, 2),
            "count": len(self.expenses),
            "average": round(total / len(self.expenses), 2),
            "by_category": {k: round(v, 2) for k, v in by_category.items()},
            "largest": max(self.expenses, key=lambda e: e.amount).to_dict(),
        }

    def export(self, fmt: str) -> str:
        from src.patterns.factory import ExporterFactory
        return ExporterFactory.create(fmt).export(self.expenses)

    def save(self) -> None:
        self.storage.save(self.expenses)
