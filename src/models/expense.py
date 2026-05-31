"""Expense data model."""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
import uuid


class Category(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    ENTERTAINMENT = "entertainment"
    BILLS = "bills"
    HEALTH = "health"
    OTHER = "other"


class PaymentMethod(Enum):
    CASH = "cash"
    CARD = "card"
    ONLINE = "online"


@dataclass
class Expense:
    """Represents a single expense record."""

    amount: float
    category: Category
    description: str
    payment_method: PaymentMethod
    date: date = field(default_factory=date.today)
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category.value,
            "description": self.description,
            "payment_method": self.payment_method.value,
            "date": self.date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            id=data["id"],
            amount=float(data["amount"]),
            category=Category(data["category"]),
            description=data["description"],
            payment_method=PaymentMethod(data["payment_method"]),
            date=date.fromisoformat(data["date"]),
        )

    def __str__(self) -> str:
        return (
            f"[{self.id}] {self.date} | {self.category.value:<15} | "
            f"${self.amount:>8.2f} | {self.payment_method.value:<6} | {self.description}"
        )
