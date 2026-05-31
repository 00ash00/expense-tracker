# Self-Assessment Rubric

## Week 1 — Git, Version Control, Build Tools (15 pts)
**Score: 14/15**
- [x] Public GitHub repository with descriptive README.md
- [x] .gitignore appropriate for Python
- [x] pyproject.toml as build tool configuration
- [x] Branching strategy: main + feature branches (feature/export, feature/statistics)
- [x] Conventional Commits convention (feat:, test:, refactor:, docs:, ci:, fix:, chore:)
- [x] 23 meaningful commits across the project
- [x] CHANGELOG.md tracking versions (0.1.0, 0.2.0, 0.3.0)

## Week 2 — Unit Testing (15 pts)
**Score: 14/15**
- [x] pytest test suite with 34 tests
- [x] 88% line coverage (exceeds 70% minimum)
- [x] 5 black-box tests in tests/test_expense.py
- [x] 5 white-box tests in tests/test_expense.py
- [x] docs/TEST_PLAN.md with testing strategy

## Week 3 — TDD/BDD/Reviews (15 pts)
**Score: 13/15**
- [x] TDD red-green-refactor cycle for search feature (3 commits)
- [x] docs/TDD_EVIDENCE.md documenting the cycle
- [x] 3 BDD acceptance tests in Given-When-Then format
- [x] PR #1 (feature/export) with 3 self-review comments
- [x] PR #2 (feature/statistics) with 3 self-review comments
- [x] docs/ESTIMATION.md with story points and reflection

## Week 4 — CI/CD, Static Analysis (15 pts)
**Score: 14/15**
- [x] GitHub Actions pipeline (.github/workflows/ci.yml)
- [x] Triggers on push and pull request
- [x] ruff linting with zero violations in final submission
- [x] pytest with coverage enforcement (80% threshold)
- [x] Evidence of pipeline failure fixed (ruff import violations)
- [x] CI badge in README.md

## Week 5 — Design Patterns (15 pts)
**Score: 13/15**
- [x] Strategy pattern (Behavioral): SortByDate, SortByAmount, SortByCategory
- [x] Factory Method (Creational): ExporterFactory, JsonExporter, CsvExporter
- [x] docs/DESIGN_PATTERNS.md with justification and UML
- [x] Patterns genuinely useful, not artificially forced

## Week 6 — Refactoring, Metrics (15 pts)
**Score: 12/15**
- [x] 3 code smells: Long Method, Magic Numbers, Feature Envy
- [x] Refactoring techniques: Extract Method, Replace Magic Number, Move Method
- [x] Cyclomatic complexity before/after measured with radon
- [x] docs/REFACTORING_REPORT.md with comparison and reflection

## Documentation (10 pts)
**Score: 8/10**
- [x] docs/TEST_PLAN.md
- [x] docs/TDD_EVIDENCE.md
- [x] docs/ESTIMATION.md
- [x] docs/DESIGN_PATTERNS.md
- [x] docs/REFACTORING_REPORT.md
- [x] README.md with setup, usage, CI badge

## Total: 88/100
