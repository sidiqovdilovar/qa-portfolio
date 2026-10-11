# Test Cases — saucedemo.com

**Environment:** Chrome [version], desktop · **Status:** Passed / Failed / Blocked
**Traceability:** case IDs are referenced in bug reports (`04_bug_reports.md`).

---

## Detailed test cases

| ID | Title | Preconditions | Steps | Expected result | Priority | Status |
|---|---|---|---|---|---|---|
| TC-01 | Login with valid credentials | Test account `standard_user` / `secret_sauce` exists | 1. Open login page<br>2. Enter valid username<br>3. Enter valid password<br>4. Click "Login" | User is logged in, redirected to product list | High | |
| TC-02 | Login with invalid password | Login page open | 1. Enter valid username<br>2. Enter wrong password<br>3. Click "Login" | Error message "Username and password do not match...", user stays on login page | High | |
| TC-03 | Login with empty fields | Login page open | 1. Leave both fields empty<br>2. Click "Login" | Validation error on both fields, no login attempt | Medium | |
| TC-04 | Locked user cannot log in | Account `locked_out_user` exists | 1. Enter `locked_out_user` + valid password<br>2. Click "Login" | Message "Sorry, this user has been locked out." | High | |
| TC-05 | Logout | User is logged in | 1. Open burger menu<br>2. Click "Logout" | Redirected to login page, session closed | High | |
| TC-06 | Add product to cart | User is logged in | 1. Open product list<br>2. Click "Add to cart" on any product | Button becomes "Remove", cart badge shows "1" | High | |
| TC-07 | Remove product from cart | 1 product in cart | 1. Open cart<br>2. Click "Remove" | Product removed, badge disappears | High | |
| TC-08 | Cart badge counts multiple products | User logged in | 1. Add product A<br>2. Add product B<br>3. Add product C | Badge shows "3"; cart contains all three | Medium | |
| TC-09 | Checkout end-to-end with valid data | Cart has ≥1 product | 1. Open cart → "Checkout"<br>2. Fill First Name, Last Name, Postal Code<br>3. Click "Continue" → "Finish" | Order complete page: "Thank you for your order!"; cart badge cleared | Critical | |
| TC-10 | Checkout with empty First Name | Cart has ≥1 product | 1. Proceed to checkout<br>2. Leave First Name empty, fill others<br>3. Click "Continue" | Error "Error: First Name is required" | High | |
| TC-11 | Sorting by price (low → high) | Logged in, product list open | 1. Select "Price (low to high)" in sort dropdown | Products sorted ascending by price; first item is the cheapest | High | |
| TC-12 | Product page shows correct data | Logged in | 1. Click any product name | Product page shows correct name, price and description matching the list | Medium | |

## Brief test cases

| ID | Title | Steps (short) | Expected result | Priority | Status |
|---|---|---|---|---|---|
| TC-13 | Search existing product | Type "backpack" | Relevant product(s) shown | Medium | |
| TC-14 | Search non-existing product | Type "zxcvbnm123" | "No results" message, no crash | Medium | |
| TC-15 | Search with special characters | Type "!!!@@##" | No crash, correct behavior documented | Low | |
| TC-16 | Empty cart message | Open cart when empty | Cart page opens without errors, correct state shown | Low | |
| TC-17 | Direct URL access without login | Open inventory URL in a fresh browser | Redirect to login page | High | |
| TC-18 | Page refresh keeps session | Refresh page after login | User stays logged in | Medium | |
| TC-19 | Product images load | Check all product images on the list | No broken images | Medium | |
| TC-20 | Prices format | Review all prices | Format `$XX.XX`, no missing decimals | Low | |
| TC-21 | Long input in checkout fields | Enter 100+ characters in First Name | No layout break; behavior documented | Low | |
| TC-22 | Cancel checkout | Checkout page → "Cancel" | Returns to cart, items preserved | Medium | |
| TC-23 | Order history contains the new order | Complete an order → open order history (if available) | New order appears with correct total | Medium | |
| TC-24 | Mobile viewport layout | Open main pages at 375×812 | No horizontal scroll, elements usable | Medium | |
| TC-25 | Console errors on main flow | DevTools → Console during login → add to cart → checkout | No critical JS errors | Medium | |

---

## Results

- **Executed:** __ / 25
- **Passed:** __
- **Failed (bugs):** __
- **Blocked:** __
- Notable observations: [fill after run]
