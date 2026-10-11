# Screenshots — evidence for every reported defect

All captures were made on **2026-10-11** with Chromium 153 (Playwright), viewport 1440×900,
against the live saucedemo.com application. Raw verification logs are stored next to them.

## Confirmed defects

| File | Defect |
|---|---|
| `bug-01_product-images-missing.png` | All products show the same 404 placeholder image (`problem_user`) |
| `bug-02_sorting-not-working.png` | Sorting options have no effect (`problem_user`) |
| `bug-03_checkout-lastname-field.png` | Checkout: Last Name field does not accept input (`problem_user`) |
| `bug-04_add-to-cart-buttons.png` | Add to cart works for only 3 of 6 products (`problem_user`) |

## Retests (suspected issues that did NOT reproduce)

| File | What was retested |
|---|---|
| `retest-01_postal-code-validation.png` | Empty Postal Code → validation error is shown correctly |
| `retest-02_slow-login.png` | Login time for `performance_glitch_user` — within normal range |
| `retest-03_finish-button-order-completed.png` | Order completes on the first "Finish" click |

## Reference captures

| File | What it shows |
|---|---|
| `catalog-standard-user.png` | Healthy catalogue for comparison (`standard_user`) |
| `cart-two-items.png` | Cart with two items added |
| `login-locked-out-error.png` | Error message for the blocked account |

## Logs

| File | Content |
|---|---|
| `VERIFICATION_RESULTS.txt` | Defect verification run — what was confirmed and what was not |
| `EXPLORATORY_RESULTS.txt` | First exploratory session (checkout fields, console errors) |
| `EXPLORATORY_RESULTS_2.txt` | Second session (cart buttons per product, sorting modes) |
