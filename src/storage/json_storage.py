"""JSON file-based storage for expenses."""

import json
from pathlib import Path
from typing import List

from src.models.expense import Expense


class JsonStorage:
    """Persists expenses to a JSON file."""

    def __init__(self, filepath: str = "expenses.json"):
        self.filepath = Path(filepath)

    def load(self) -> List[Expense]:
        if not self.filepath.exists():
            return []
        with open(self.filepath, "r") as f:
            data = json.load(f)
        return [Expense.from_dict(d) for d in data]

    def save(self, expenses: List[Expense]) -> None:
        with open(self.filepath, "w") as f:
            json.dump([e.to_dict() for e in expenses], f, indent=2)
