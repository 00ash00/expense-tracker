# Expense Tracker CLI

![CI](https://github.com/00ash00/expense-tracker/actions/workflows/ci.yml/badge.svg)

A personal expense tracker command-line application built with Python.

## Features
- Add, list, update, delete expenses
- Search by keyword, filter by category and date range
- Sort by date, amount, or category
- Export to JSON or CSV
- Statistics summary
- Persistent JSON storage

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python -m src.main add --amount 25.50 --category food --description "Lunch" --payment card
python -m src.main list --sort amount
python -m src.main search coffee
python -m src.main filter --category food --from-date 2024-01-01
python -m src.main stats
python -m src.main export --format csv --output expenses.csv
python -m src.main update <ID> --amount 30.0
python -m src.main delete <ID>
```

## Run Tests

```bash
pytest --cov=src --cov-report=term-missing -v
```

## Design Patterns
- **Strategy** — swappable sorting algorithms (`SortByDate`, `SortByAmount`, `SortByCategory`)
- **Factory Method** — pluggable exporters (`JsonExporter`, `CsvExporter`)

## Project Structure
