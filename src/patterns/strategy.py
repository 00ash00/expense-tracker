"""Strategy pattern for sorting expenses."""

from abc import ABC, abstractmethod
from typing import List

from src.models.expense import Expense


class SortStrategy(ABC):
    """Abstract base for sort strategies."""

    @abstractmethod
    def sort(self, expenses: List[Expense]) -> List[Expense]:
        pass


class SortByDate(SortStrategy):
    """Sort expenses by date ascending."""

    def sort(self, expenses: List[Expense]) -> List[Expense]:
        return sorted(expenses, key=lambda e: e.date)


class SortByAmount(SortStrategy):
    """Sort expenses by amount descending."""

    def sort(self, expenses: List[Expense]) -> List[Expense]:
        return sorted(expenses, key=lambda e: e.amount, reverse=True)


class SortByCategory(SortStrategy):
    """Sort expenses by category name."""

    def sort(self, expenses: List[Expense]) -> List[Expense]:
        return sorted(expenses, key=lambda e: e.category.value)
