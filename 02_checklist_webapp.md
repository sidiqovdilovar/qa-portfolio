# Checklist — saucedemo.com (web application)

**Tested version:** [date / build]
**Environment:** Chrome [ver] desktop / mobile viewport 375×812
**Legend:** `[x]` passed · `[!]` failed (bug ID) · `[ ]` not run

---

## 1. Authentication (12)

- [ ] 1.1 Registration with valid data (unique email, strong password)
- [ ] 1.2 Registration with an already registered email → proper error
- [ ] 1.3 Registration with empty required fields → validation messages
- [ ] 1.4 Password field masks input
- [ ] 1.5 Password minimum length / complexity validation
- [ ] 1.6 Login with valid credentials → redirected to account
- [ ] 1.7 Login with wrong password → error message, no login
- [ ] 1.8 Login with non-existent user → error message
- [ ] 1.9 Locked/blocked user cannot log in (saucedemo: `locked_out_user`)
- [ ] 1.10 Logout works from any page
- [ ] 1.11 Direct access to profile URL without login → redirect to login page
- [ ] 1.12 Session persists after page refresh

## 2. Catalog & search (12)

- [ ] 2.1 Product list loads, all items have image, title, price
- [ ] 2.2 Product page opens with correct data (title, price, description, images)
- [ ] 2.3 Sorting by price: low → high
- [ ] 2.4 Sorting by price: high → low
- [ ] 2.5 Sorting by name A→Z / Z→A
- [ ] 2.6 Search with an existing keyword returns relevant products
- [ ] 2.7 Search with a non-existing keyword → "no results" message, no error
- [ ] 2.8 Search with special characters (`!@#$%`, emoji) → no crash
- [ ] 2.9 Search with 200+ characters → no crash, field limit handles input
- [ ] 2.10 Search field trims leading/trailing spaces
- [ ] 2.11 Images load correctly for all products (compare visually)
- [ ] 2.12 Prices displayed with correct currency and 2 decimals

## 3. Cart (12)

- [ ] 3.1 Add one product → cart badge shows 1
- [ ] 3.2 Add several products → badge shows correct total
- [ ] 3.3 Adding the same product twice → quantity/count behaves as specified
- [ ] 3.4 Remove product from cart → badge updates
- [ ] 3.5 Cart total equals sum of item prices (no tax/shipping issues)
- [ ] 3.6 Cart contents persist after page refresh (if account-based)
- [ ] 3.7 Cart is empty state shows proper message
- [ ] 3.8 Product price in cart matches price on catalog page
- [ ] 3.9 "Continue shopping" returns to catalog
- [ ] 3.10 Cart is not shared between different users on the same browser
- [ ] 3.11 Quantity cannot be set to 0 or negative
- [ ] 3.12 Long product name doesn't break cart layout

## 4. Checkout (14)

- [ ] 4.1 Checkout with valid data → order confirmation
- [ ] 4.2 Checkout with empty First Name → validation error
- [ ] 4.3 Checkout with empty Last Name → validation error
- [ ] 4.4 Checkout with empty Postal Code → validation error
- [ ] 4.5 Postal code with letters/symbols → validation behavior documented
- [ ] 4.6 Very long input in fields → layout not broken
- [ ] 4.7 Order summary shows correct items and total
- [ ] 4.8 Cancel checkout returns to cart, contents preserved
- [ ] 4.9 Total on confirmation page matches cart total
- [ ] 4.10 Order confirmation message is clear and correct
- [ ] 4.11 Double-click on "Finish" doesn't create a duplicate order
- [ ] 4.12 Back button after order doesn't repeat the order
- [ ] 4.13 Checkout possible only with non-empty cart
- [ ] 4.14 Tax/fee (if present) is calculated correctly

## 5. Profile & orders (8)

- [ ] 5.1 Order history shows placed orders with correct data
- [ ] 5.2 Personal data can be viewed
- [ ] 5.3 Editing personal data saves and persists after refresh
- [ ] 5.4 Editing with invalid email → validation error
- [ ] 5.5 Password change flow works (if present)
- [ ] 5.6 Empty order history shows proper message
- [ ] 5.7 Order details page opens from history
- [ ] 5.8 Data of another user is not accessible (change ID in URL) — basic check

## 6. UI & cross-browser (10)

- [ ] 6.1 Main pages layout matches design, no overlapping elements
- [ ] 6.2 All buttons are clickable and have hover/disabled states
- [ ] 6.3 Text has no typos/placeholder text (lorem ipsum) visible
- [ ] 6.4 Images are not broken (no 404 icons)
- [ ] 6.5 Error messages are clear, in the right language
- [ ] 6.6 Mobile viewport 375×812: no horizontal scroll, tap targets OK
- [ ] 6.7 Tablet viewport 768×1024 layout OK
- [ ] 6.8 Chrome: all checks above run without console errors
- [ ] 6.9 Firefox: key flows (login, add to cart, checkout) work
- [ ] 6.10 Edge: key flows work

## 7. Basic security & console (8)

- [ ] 7.1 Password is not visible in page source / requests when logged in
- [ ] 7.2 Console has no critical JavaScript errors (Chrome DevTools → Console)
- [ ] 7.3 Network tab: main requests return 200/3xx, no 5xx on normal flow
- [ ] 7.4 Auto-complete does not leak password into other fields
- [ ] 7.5 User cannot access checkout without items by direct URL
- [ ] 7.6 Logout invalidates session (back button doesn't restore account)
- [ ] 7.7 No user data in URL parameters of normal pages
- [ ] 7.8 HTTPS used; browser shows no "not secure" warning

---

**Total: 76 checklist items**

Fill in failures with bug IDs from `04_bug_reports.md`, e.g. `[!] 4.11 — BUG-03`.
