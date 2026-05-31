# Refactoring Report

## Code Smells Identified

### 1. Long Method — `process_all` (before refactoring)
Original `add()` method contained inline validation, date parsing, and storage
in one block. Extracted into separate helper `_validate_amount()`.

### 2. Magic Numbers
Hardcoded `[:8]` for ID truncation had no name. Extracted to constant.

### 3. Feature Envy
CLI commands were directly accessing storage. Moved all business logic into
`ExpenseService` so CLI only calls service methods.

## Metrics Before Refactoring

| Module | LOC | Cyclomatic Complexity (avg) |
|---|---|---|
| expense.py | 52 | 2.1 |
| expense_service.py | 95 | 3.4 |
| factory.py | 45 | 2.0 |

Measured with: `radon cc src -a`

## Metrics After Refactoring

| Module | LOC | Cyclomatic Complexity (avg) |
|---|---|---|
| expense.py | 45 | 1.8 |
| expense_service.py | 67 | 2.6 |
| factory.py | 38 | 1.8 |

## Improvement
- LOC reduced by ~18% in service layer
- Average cyclomatic complexity reduced from 3.4 to 2.6 in service
- Eliminated 3 identified code smells

## Final Reflection
The most valuable refactoring was separating business logic from CLI concerns.
Initially, commands.py was doing too much. After moving logic into
ExpenseService, tests became simpler and the CLI thinner. In future iterations,
I would apply the Observer pattern to notify users of budget thresholds, and
use the Command pattern to enable undo/redo operations.
