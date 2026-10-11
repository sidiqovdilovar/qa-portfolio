# Test Plan — saucedemo.com manual testing

| Field | Value |
|---|---|
| Project | QA practice: manual testing of saucedemo.com |
| Author | Sidiqov Dilovar, Junior QA |
| Version | 1.0 |
| Date | [2026-10-12] |

---

## 1. Objective

Verify core user flows of the e-commerce web application (registration, login, catalog, search, cart, checkout, profile) and confirm the application behaves according to expected behavior. Identify, reproduce and document defects.

## 2. Scope

**In scope (features to test):**
- Authentication: registration, login, logout, password validation
- Catalog: product list, product page, sorting, filtering
- Search: by keyword, empty results, special characters
- Cart: add, remove, change quantity, price calculation
- Checkout: address form, validation, order confirmation
- Profile: order history, personal data
- UI: layout, text, images, messages (desktop + mobile viewport)
- Cross-browser: Chrome, Firefox, Edge (latest versions)

**Out of scope:**
- Performance and load testing
- Security / penetration testing (only basic checks: password masking, direct URL access)
- Payment system internals (test data only, no real payments)

## 3. Test approach

| Item | Description |
|---|---|
| Testing types | Functional, regression, smoke, UI, exploratory, basic API checks (Postman) |
| Test design techniques | Equivalence partitioning, boundary values, pairwise, state transition |
| Documentation | Checklist (76 items), test cases (25), bug reports |
| Environment | [Windows 11 / macOS], Chrome [version], screen 1920×1080 and mobile 375×812 |
| Test data | Public demo accounts, e.g. `standard_user` / `secret_sauce` on saucedemo.com |

## 4. Entry criteria

- Application is accessible and unstable crashes do not block testing
- Test accounts available
- Checklist and test cases prepared

## 5. Exit criteria

- All planned checklists and test cases executed
- All critical/high severity bugs documented with reproduction steps
- Test summary prepared

## 6. Risks

| Risk | Mitigation |
|---|---|
| Third-party site may change (it is not our build) | Fix the tested version/date in bug reports |
| Some flows require payment data | Use test/demo data, document limitations |
| Limited time | Prioritize smoke + checkout + auth critical paths first |

## 7. Deliverables

- Checklist — `02_checklist_webapp.md`
- Test cases — `03_test-cases.md`
- Bug reports — `04_bug_reports.md`
- Screenshots — `screenshots/`
- API run results — `05_api_findings.md`

## 8. Results summary (fill after the run)

- Checklist items executed: [76] / 76
- Test cases: [25] executed, [__] passed, [__] failed
- Bugs found: [__] (critical: [__], high: [__], medium: [__], low: [__])
- Conclusion: [e.g. "Core flows work; checkout has 2 high-severity defects, documented in bug reports."]
