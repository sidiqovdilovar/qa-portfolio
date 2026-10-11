# UI Automation — Playwright + pytest (Python)

Automated UI tests for [saucedemo.com](https://www.saucedemo.com) — a public demo shop built specifically for QA practice.

## What is covered (10 tests, all passing)

| File | Tests |
|---|---|
| `test_login.py` | successful login, locked-out user, wrong password, empty-field validation |
| `test_cart.py` | add 1 item, add 2 items (badge count), remove item |
| `test_checkout.py` | end-to-end checkout, required-field validation, cancel flow |

## Stack

- Python 3.10+
- pytest — test runner, fixtures, reporting
- Playwright (sync API) — browser automation (Chromium)

## How to run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Install the browser
playwright install chromium

# 3. Run the tests
pytest -v | tee report.txt

# Optional: run headed (see the browser) and slower
pytest -v --headed
```

## Test data

| User | Password | Purpose |
|---|---|---|
| `standard_user` | `secret_sauce` | positive scenarios |
| `locked_out_user` | `secret_sauce` | negative scenario (blocked account) |
| `problem_user` | `secret_sauce` | has visual/sorting defects (good material for manual bug reports) |
| `performance_glitch_user` | `secret_sauce` | slow login (~5s) |

## Notes for reviewers

- All locators use stable **IDs/classes** (`#user-name`, `.title`, `[data-test="..."]`) — the same approach as in commercial projects (data-test attributes are the most reliable).
- Assertions use Playwright's `expect()` with auto-waiting — no `sleep()` hacks.
- The `page` and `browser` fixtures are defined in `conftest.py`; each test runs in a clean browser context.

## Verified run (2026-10-11)

```
10 passed in 4.90s  —  Chromium 153, viewport 1280x800
```

## Next steps (roadmap)

- [ ] Add 5 more tests: sorting, product details, logout, reset app state, checkout validation
- [ ] Add API tests with `requests` (JSONPlaceholder) to the same suite
- [ ] Add GitHub Actions workflow to run tests on every push
