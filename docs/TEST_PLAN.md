# Test Plan

## Strategy
Tests are divided into black-box (specification-based) and white-box (structure-based).

## Black-Box Tests (5)
Derived from the specification without knowledge of internal implementation:
- `test_bb_expense_creation_required_fields` — verifies all 4 required fields are stored
- `test_bb_expense_default_date_is_today` — default date must be today
- `test_bb_expense_id_is_auto_generated` — each expense gets unique ID
- `test_bb_expense_to_dict_has_all_fields` — dict export includes all 6 fields
- `test_bb_expense_from_dict_roundtrip` — serialize → deserialize preserves data

## White-Box Tests (5)
Derived from code structure (branch/path coverage):
- `test_wb_str_format_contains_key_fields` — tests __str__ branch
- `test_wb_category_enum_values` — tests all enum branches
- `test_wb_payment_method_enum_values` — tests all enum branches
- `test_wb_from_dict_parses_date_correctly` — tests date parsing path
- `test_wb_to_dict_date_is_string` — tests serialization branch

## Coverage Target
Minimum 80% line coverage of business logic, measured by pytest-cov.
Actual achieved: 88%.

## Tools
- pytest 9.0
- pytest-cov 7.1
- ruff (static analysis)
