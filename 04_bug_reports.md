# Bug Reports — saucedemo.com

**All defects below were reproduced live** with browser automation (Chromium, Playwright) on **2026-10-11**.
Each report has a screenshot in [`screenshots/`](screenshots/) and a raw verification log in
[`screenshots/VERIFICATION_RESULTS.txt`](screenshots/VERIFICATION_RESULTS.txt).

**Environment:** Chromium 153 (Playwright) · viewport 1440×900 · tested 2026-10-11

**Summary:** 4 defects confirmed · 3 previously suspected issues did **not** reproduce on retest (documented below)

| ID | Title | Module | Severity | Priority | Status |
|---|---|---|---|---|---|
| BUG-01 | Product images are not displayed in the catalogue | Catalog | High | P1 | Confirmed |
| BUG-02 | Sorting options have no effect on product order | Catalog | Medium | P2 | Confirmed |
| BUG-03 | Checkout: "Last Name" field does not accept input | Checkout | Critical | P1 | Confirmed |
| BUG-04 | "Add to cart" works for only 3 of 6 products | Cart | High | P1 | Confirmed |

---

## BUG-01 — All products show the same 404 placeholder image instead of their own photos

| Field | Value |
|---|---|
| ID | BUG-01 |
| Module | Catalog |
| Severity | High |
| Priority | P1 |
| Reproducibility | 100% (6/6 products) |
| Account | `problem_user` / `secret_sauce` |
| Test case | TC-19 (product images load) |
| Evidence | [`screenshots/bug-01_product-images-missing.png`](screenshots/bug-01_product-images-missing.png) |

**Steps to reproduce:**
1. Open https://www.saucedemo.com and log in as `problem_user`
2. Inspect the product images in the catalogue (DevTools → Elements, or the automated check below)

**Expected result:** each product shows its own photo, matching the product name
(as it does for `standard_user`).

**Actual result:** every one of the 6 products points to the same file —
`/assets/sl-404-Cq1a9k9X.jpg` — a **404 placeholder**, so the catalogue displays the identical
generic image six times instead of the real product photos.

**Verification (automated):**

| Account | Unique image sources | Example `src` |
|---|---|---|
| `problem_user` | **1** (used 6 times) | `/assets/sl-404-Cq1a9k9X.jpg` |
| `standard_user` | 6 (correct) | `/assets/sauce-backpack-1200x1500-….jpg`, `/assets/bike-light-1200x1500-….jpg`, … |

The image itself loads (600×546 px) — so this is **not** a broken link but a wrong asset:
the application serves a placeholder file for every product.

**Impact:** users cannot visually identify products — directly affects purchase decisions.

---

## BUG-02 — Sorting options have no effect on product order

| Field | Value |
|---|---|
| ID | BUG-02 |
| Module | Catalog |
| Severity | Medium |
| Priority | P2 |
| Reproducibility | 100% (4/4 sort options) |
| Account | `problem_user` / `secret_sauce` |
| Test case | TC-11 (sorting by price) |
| Evidence | [`screenshots/bug-02_sorting-not-working.png`](screenshots/bug-02_sorting-not-working.png) |

**Steps to reproduce:**
1. Log in as `problem_user`
2. Select any option in the sort dropdown: **Name (Z to A)**, **Price (low to high)**, **Price (high to low)**

**Expected result:** the product list re-orders according to the selected option.

**Actual result:** the order never changes. Captured prices after selecting "Price (low to high)":

```
29.99, 9.99, 15.99, 49.99, 7.99, 15.99   ← not ascending
```

All four options return the identical default order — sorting is effectively non-functional.

**Impact:** users cannot find products by price or name — a core e-commerce function is broken.

---

## BUG-03 — Checkout: "Last Name" field does not accept input

| Field | Value |
|---|---|
| ID | BUG-03 |
| Module | Checkout |
| Severity | Critical |
| Priority | P1 |
| Reproducibility | 100% (3/3 attempts) |
| Account | `problem_user` / `secret_sauce` |
| Test case | TC-09 (checkout end-to-end) |
| Evidence | [`screenshots/bug-03_checkout-lastname-field.png`](screenshots/bug-03_checkout-lastname-field.png) |

**Steps to reproduce:**
1. Log in as `problem_user`, add any product to the cart
2. Go to cart → **Checkout**
3. Enter `Ivan` in First Name, `Ivanov` in Last Name, `12345` in Postal Code
4. Read the field values back

**Expected result:** First Name = `Ivan`, Last Name = `Ivanov`.

**Actual result:** the Last Name field stays empty, and the value typed into it is written into
First Name instead:

```
first = 'Ivanov', last = '', postal = '12345'
```

**Impact:** the user cannot enter a last name at all — the order cannot be completed correctly.
This is the most severe defect of the run: it blocks the purchase funnel.

---

## BUG-04 — "Add to cart" works for only 3 of 6 products

| Field | Value |
|---|---|
| ID | BUG-04 |
| Module | Cart |
| Severity | High |
| Priority | P1 |
| Reproducibility | 100% (verified product by product) |
| Account | `problem_user` / `secret_sauce` |
| Test case | TC-06 (add product to cart) |
| Evidence | [`screenshots/bug-04_add-to-cart-buttons.png`](screenshots/bug-04_add-to-cart-buttons.png) |

**Steps to reproduce:**
1. Log in as `problem_user`
2. Click **Add to cart** on each of the 6 products in turn
3. Open the cart

**Expected result:** 6 clicks → 6 items in the cart, counter shows `6`.

**Actual result:** after clicking all 6 buttons the counter shows `3` and the cart contains
3 items. Buttons for products #3, #4 and #6 do not react — the button label does not change
from "Add to cart" to "Remove":

| Product index | Before click | After click |
|---|---|---|
| 1 | Add to cart | Remove ✅ |
| 2 | Add to cart | Remove ✅ |
| 3 | Add to cart | **Add to cart** ❌ |
| 4 | Add to cart | **Add to cart** ❌ |
| 5 | Add to cart | Remove ✅ |
| 6 | Add to cart | **Add to cart** ❌ |

**Impact:** half of the catalogue cannot be purchased — direct loss of revenue.

---

## Retest: issues that did NOT reproduce (documented for completeness)

A good bug report also records what was checked and **did not** fail — this prevents wasted
engineering time. These items were suspected, tested on the live build, and closed as
"cannot reproduce":

| # | Suspected issue | Account | Result | Evidence |
|---|---|---|---|---|
| RT-01 | "Finish" button requires a double click | `standard_user` | ❌ Not reproduced — order completes on the first click | [`retest-03_finish-button-order-completed.png`](screenshots/retest-03_finish-button-order-completed.png) |
| RT-02 | Empty "Postal Code" is not validated | `standard_user` | ❌ Not reproduced — error shown: *"Error: Postal Code is required"* | [`retest-01_postal-code-validation.png`](screenshots/retest-01_postal-code-validation.png) |
| RT-03 | Login is slower than 2 seconds | `performance_glitch_user` | ❌ Not reproduced — login took 0.05 s on this run | [`retest-02_slow-login.png`](screenshots/retest-02_slow-login.png) |

**Additional observation (not a defect):** for `standard_user` the cart counter persists after a
page reload — expected behaviour for a session-based cart, confirmed as working as designed.

---

## How these reports were produced

Every defect was reproduced with an automated Playwright script — the same tool used in
[`automation/`](automation/). Scripts, logs and screenshots are committed, so any report can be
re-verified by anyone:

```bash
pip install -r automation/requirements.txt
playwright install chromium
python verify_defects.py   # reproduces all defects and re-captures screenshots
```
