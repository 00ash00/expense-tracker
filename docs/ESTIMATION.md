# Estimation

## User Stories and Estimates

| Story | Description | Estimate (SP) | Actual (hrs) |
|---|---|---|---|
| US-01 | Add a new expense with 4+ fields | 2 | 1.5 |
| US-02 | List all expenses with formatted output | 1 | 0.5 |
| US-03 | Update an existing expense by ID | 2 | 1.0 |
| US-04 | Delete an expense by ID | 1 | 0.5 |
| US-05 | Search expenses by keyword | 2 | 1.0 |
| US-06 | Filter by category and date range | 3 | 2.0 |
| US-07 | Sort by date, amount, category | 3 | 1.5 |
| US-08 | Persist data between sessions | 3 | 2.0 |
| US-09 | Export to JSON and CSV | 3 | 1.5 |
| US-10 | Statistics summary | 2 | 1.0 |
| US-11 | Unit tests (BB + WB, 80%+ coverage) | 5 | 3.0 |
| US-12 | CI pipeline with lint and coverage | 3 | 1.5 |
| US-13 | Design patterns (Strategy + Factory) | 5 | 2.5 |
| US-14 | Documentation (5 docs) | 3 | 2.0 |

**Total estimated:** 38 story points  
**Total actual:** ~22 hours

## Reflection
Estimation was roughly accurate for CRUD features. Testing and documentation
took less time than estimated because patterns emerged naturally. The design
patterns integration was the most complex part — the Factory pattern required
careful abstraction to be genuinely useful rather than artificial.
