# Bug Reports — saucedemo.com

> ⚠️ Это **примеры правильного формата**. Прогони тесты и замени/дополни описания **своими** находками: только то, что реально воспроизводится. Минимум для портфолио — 6–10 баг-репортов.

**Environment for all reports:** [Windows 11, Chrome 1XX, 1920×1080] · tested [date]

---

## How to write a good bug title

`[Module] Short symptom when action (conditions)` → e.g. *"Checkout: 'Finish' button double click creates two orders"*

## Severity vs Priority

| | Description |
|---|---|
| **Severity** (impact on the system) | Critical / High / Medium / Low |
| **Priority** (order to fix) | P1 (urgent) / P2 / P3 / P4 (minor) |

---

## BUG-01 — Checkout: "Finish" button does not respond on first click

| Field | Value |
|---|---|
| ID | BUG-01 |
| Module | Checkout |
| Severity | High |
| Priority | P1 |
| Related test case | TC-09 |
| Reproducibility | 100% (5/5) |
| Environment | Windows 11, Chrome [ver], desktop |

**Steps to reproduce:**
1. Log in as `standard_user` / `secret_sauce`
2. Add any product to cart
3. Open cart → Checkout
4. Fill First Name, Last Name, Postal Code → Continue
5. Click "Finish" once

**Expected result:** order is placed, page shows "Thank you for your order!"

**Actual result:** nothing happens on the first click; the order is placed only on the second click.

**Additional info:** console shows no error; see `screenshots/bug-01_finish-button.png`.

---

## BUG-02 — Product images mismatch product names in catalog

| Field | Value |
|---|---|
| ID | BUG-02 |
| Module | Catalog |
| Severity | Medium |
| Priority | P2 |
| Related test case | TC-12 |
| Reproducibility | 100% (10/10 products) |

**Steps:** log in as `problem_user` → open product list → compare each image with the product name.

**Expected:** each product shows its own correct image.
**Actual:** all products show the same placeholder image; image does not match the product.

**Impact:** users may order the wrong item — affects purchasing decisions.

---

## BUG-03 — Sorting does not work for "Price (low to high)"

| Field | Value |
|---|---|
| ID | BUG-03 |
| Module | Catalog |
| Severity | Medium |
| Priority | P2 |
| Related test case | TC-11 |

**Steps:** log in as `problem_user` → select "Price (low to high)" in the sort dropdown.

**Expected:** products are sorted ascending by price.
**Actual:** order does not change; sorting has no effect.

---

## BUG-04 — No validation error when Postal Code field is empty

| Field | Value |
|---|---|
| ID | BUG-04 |
| Module | Checkout |
| Severity | Medium |
| Priority | P2 |
| Related test case | TC-10 |

**Steps:** complete checkout with empty Postal Code, click "Continue".

**Expected:** error "Postal Code is required", checkout is not continued.
**Actual:** [describe what really happens — fill after your own run].

---

## BUG-05 — Search accepts empty query and returns all products

| Field | Value |
|---|---|
| ID | BUG-05 |
| Module | Search |
| Severity | Low |
| Priority | P3 |

**Steps:** on the product list, enter a single space in search and confirm.

**Expected:** search is not executed / shows hint, no results reload.
**Actual:** [fill after verification].

---

## BUG-06 — Page performance: login takes >5 seconds

| Field | Value |
|---|---|
| ID | BUG-06 |
| Module | Authentication |
| Severity | Low |
| Priority | P3 |

**Steps:** log in as `performance_glitch_user` and measure time to the product list.

**Expected:** page loads within 2 seconds.
**Actual:** load takes ~5–6 seconds; page freezes with no loader.

---

## Bug summary table (fill after the run)

| ID | Title | Module | Severity | Priority | Status |
|---|---|---|---|---|---|
| BUG-01 | | Checkout | High | P1 | Open |
| BUG-02 | | Catalog | Medium | P2 | Open |
| BUG-03 | | Catalog | Medium | P2 | Open |
| BUG-04 | | Checkout | Medium | P2 | Open |
| BUG-05 | | Search | Low | P3 | Open |
| BUG-06 | | Auth | Low | P3 | Open |
| BUG-07 | | | | | |
| BUG-08 | | | | | |

**Total:** 8 reports · Critical 0 · High 1 · Medium 3 · Low 2 (+ your own)
