"""Factory pattern for export formats."""

import csv
import json
import io
from abc import ABC, abstractmethod
from typing import List

from src.models.expense import Expense


class Exporter(ABC):
    """Abstract base for exporters."""

    @abstractmethod
    def export(self, expenses: List[Expense]) -> str:
        pass


class JsonExporter(Exporter):
    """Exports expenses to JSON format."""

    def export(self, expenses: List[Expense]) -> str:
        return json.dumps([e.to_dict() for e in expenses], indent=2)


class CsvExporter(Exporter):
    """Exports expenses to CSV format."""

    def export(self, expenses: List[Expense]) -> str:
        output = io.StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=["id", "amount", "category", "description",
                        "payment_method", "date"]
        )
        writer.writeheader()
        writer.writerows([e.to_dict() for e in expenses])
        return output.getvalue()


class ExporterFactory:
    """Factory that creates the right exporter by format name."""

    _exporters = {
        "json": JsonExporter,
        "csv": CsvExporter,
    }

    @classmethod
    def create(cls, fmt: str) -> Exporter:
        fmt = fmt.lower()
        if fmt not in cls._exporters:
            raise ValueError(f"Unknown format: {fmt}. Choose from: {list(cls._exporters)}")
        return cls._exporters[fmt]()
