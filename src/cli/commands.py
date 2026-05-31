"""CLI commands for the expense tracker."""

import sys
from datetime import datetime

import click
from rich.console import Console
from rich.table import Table

from src.patterns.strategy import SortByAmount, SortByCategory, SortByDate
from src.services.expense_service import ExpenseService

console = Console()
service = ExpenseService()

SORT_STRATEGIES = {
    "date": SortByDate(),
    "amount": SortByAmount(),
    "category": SortByCategory(),
}


@click.group()
def cli():
    """Personal Expense Tracker CLI."""
    pass


@cli.command()
@click.option("--amount", required=True, type=float, help="Amount spent")
@click.option("--category", required=True,
              type=click.Choice(["food", "transport", "entertainment",
                                 "bills", "health", "other"]),
              help="Expense category")
@click.option("--description", required=True, help="Description")
@click.option("--payment", default="card",
              type=click.Choice(["cash", "card", "online"]),
              help="Payment method")
@click.option("--date", "expense_date", default=None,
              help="Date (YYYY-MM-DD), default today")
def add(amount, category, description, payment, expense_date):
    """Add a new expense."""
    parsed_date = None
    if expense_date:
        try:
            parsed_date = datetime.strptime(expense_date, "%Y-%m-%d").date()
        except ValueError:
            console.print("[red]Invalid date format. Use YYYY-MM-DD.[/red]")
            sys.exit(1)
    expense = service.add(amount, category, description, payment, parsed_date)
    console.print(f"[green]Added:[/green] {expense}")


@cli.command("list")
@click.option("--sort", default="date",
              type=click.Choice(["date", "amount", "category"]),
              help="Sort by field")
def list_expenses(sort):
    """List all expenses."""
    expenses = service.list_all(SORT_STRATEGIES[sort])
    if not expenses:
        console.print("[yellow]No expenses found.[/yellow]")
        return
    table = Table(title="Expenses")
    table.add_column("ID", style="cyan")
    table.add_column("Date")
    table.add_column("Category")
    table.add_column("Amount", justify="right")
    table.add_column("Payment")
    table.add_column("Description")
    for e in expenses:
        table.add_row(e.id, str(e.date), e.category.value,
                      f"${e.amount:.2f}", e.payment_method.value, e.description)
    console.print(table)


@cli.command()
@click.argument("expense_id")
@click.option("--amount", type=float)
@click.option("--category",
              type=click.Choice(["food", "transport", "entertainment",
                                 "bills", "health", "other"]))
@click.option("--description")
@click.option("--payment", type=click.Choice(["cash", "card", "online"]))
def update(expense_id, amount, category, description, payment):
    """Update an expense by ID."""
    kwargs = {}
    if amount is not None:
        kwargs["amount"] = amount
    if category:
        kwargs["category"] = category
    if description:
        kwargs["description"] = description
    if payment:
        kwargs["payment_method"] = payment
    result = service.update(expense_id, **kwargs)
    if result:
        console.print(f"[green]Updated:[/green] {result}")
    else:
        console.print(f"[red]Expense {expense_id} not found.[/red]")


@cli.command()
@click.argument("expense_id")
def delete(expense_id):
    """Delete an expense by ID."""
    if service.delete(expense_id):
        console.print(f"[green]Deleted expense {expense_id}.[/green]")
    else:
        console.print(f"[red]Expense {expense_id} not found.[/red]")


@cli.command()
@click.argument("keyword")
def search(keyword):
    """Search expenses by keyword."""
    results = service.search(keyword)
    if not results:
        console.print("[yellow]No matching expenses.[/yellow]")
        return
    for e in results:
        console.print(str(e))


@cli.command("filter")
@click.option("--category",
              type=click.Choice(["food", "transport", "entertainment",
                                 "bills", "health", "other"]))
@click.option("--from-date", "date_from", default=None)
@click.option("--to-date", "date_to", default=None)
def filter_expenses(category, date_from, date_to):
    """Filter expenses by category and/or date range."""
    parsed_from = (datetime.strptime(date_from, "%Y-%m-%d").date()
                   if date_from else None)
    parsed_to = (datetime.strptime(date_to, "%Y-%m-%d").date()
                 if date_to else None)
    results = service.filter_by(category, parsed_from, parsed_to)
    if not results:
        console.print("[yellow]No matching expenses.[/yellow]")
        return
    for e in results:
        console.print(str(e))


@cli.command()
def stats():
    """Show expense statistics."""
    s = service.statistics()
    if not s:
        console.print("[yellow]No expenses yet.[/yellow]")
        return
    console.print(f"[bold]Total:[/bold] ${s['total']:.2f}")
    console.print(f"[bold]Count:[/bold] {s['count']}")
    console.print(f"[bold]Average:[/bold] ${s['average']:.2f}")
    console.print("\n[bold]By category:[/bold]")
    for cat, total in s["by_category"].items():
        console.print(f"  {cat:<15} ${total:.2f}")
    largest = s["largest"]
    console.print(
        f"\n[bold]Largest expense:[/bold] ${largest['amount']:.2f} "
        f"— {largest['description']}"
    )


@cli.command()
@click.option("--format", "fmt", default="json",
              type=click.Choice(["json", "csv"]),
              help="Export format")
@click.option("--output", default=None, help="Output file path")
def export(fmt, output):
    """Export expenses to JSON or CSV."""
    content = service.export(fmt)
    if output:
        with open(output, "w") as f:
            f.write(content)
        console.print(f"[green]Exported to {output}[/green]")
    else:
        console.print(content)
