# Design Patterns

## Pattern 1: Strategy (Behavioral)

### What
`SortStrategy` abstract base class with three concrete implementations:
`SortByDate`, `SortByAmount`, `SortByCategory`.

### Why
The application needs to sort expenses by different fields. Without Strategy,
`list_all()` would contain a large `if/elif` block that would grow with every
new sort option. Strategy decouples the sorting algorithm from the service,
making it easy to add new sort criteria without modifying existing code
(Open/Closed Principle).

### Files
`src/patterns/strategy.py`, used in `src/services/expense_service.py`

### UML
---

## Pattern 2: Factory Method (Creational)

### What
`ExporterFactory.create(fmt)` returns the right `Exporter` subclass
(`JsonExporter` or `CsvExporter`) based on a format string.

### Why
The export feature must support multiple formats (JSON, CSV) and potentially
more in the future. Without Factory, the CLI command would contain format
branching logic and be tightly coupled to concrete exporter classes.
`ExporterFactory` centralizes creation, so adding a new format (e.g., XLSX)
requires only adding one line to `_exporters` dict, not touching callers.

### Files
`src/patterns/factory.py`, used in `src/services/expense_service.py`

### UML
