# TDD Evidence

Feature developed using TDD: **search by keyword**

## Red-Green-Refactor Cycle

### Step 1 — Red (failing test)
Commit: `test: add failing test for search by keyword`
```python
def test_search_by_description(service):
    service.add(10.0, "food", "Coffee at Starbucks", "card")
    results = service.search("starbucks")
    assert len(results) == 1
```
Test fails: `AttributeError: 'ExpenseService' object has no attribute 'search'`

### Step 2 — Green (minimal implementation)
Commit: `feat: implement search method to pass test`
```python
def search(self, keyword: str) -> List[Expense]:
    kw = keyword.lower()
    return [e for e in self.expenses if kw in e.description.lower()]
```

### Step 3 — Refactor
Commit: `refactor: extend search to also match category`
```python
def search(self, keyword: str) -> List[Expense]:
    kw = keyword.lower()
    return [
        e for e in self.expenses
        if kw in e.description.lower() or kw in e.category.value.lower()
    ]
```
