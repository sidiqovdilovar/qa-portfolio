"""Checkout tests for saucedemo.com.

Covers: full successful checkout flow and validation of the address form.
"""
from playwright.sync_api import expect


class TestCheckout:

    def _go_to_checkout(self, page):
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        page.locator(".shopping_cart_link").click()
        page.locator("[data-test='checkout']").click()

    def test_full_checkout_flow(self, logged_in_app):
        """TC-09: end-to-end order placement shows the confirmation page."""
        page = logged_in_app
        self._go_to_checkout(page)

        page.fill("[data-test='firstName']", "Ivan")
        page.fill("[data-test='lastName']", "Ivanov")
        page.fill("[data-test='postalCode']", "123456")
        page.click("[data-test='continue']")
        page.click("[data-test='finish']")

        expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")
        expect(page.locator(".shopping_cart_badge")).to_have_count(0)

    def test_checkout_requires_first_name(self, logged_in_app):
        """TC-10: empty First Name blocks the checkout with a validation error."""
        page = logged_in_app
        self._go_to_checkout(page)

        page.fill("[data-test='lastName']", "Ivanov")
        page.fill("[data-test='postalCode']", "123456")
        page.click("[data-test='continue']")

        error = page.locator("[data-test='error']")
        expect(error).to_be_visible()
        expect(error).to_contain_text("First Name is required")

    def test_cancel_checkout_keeps_cart(self, logged_in_app):
        """TC-22: cancelling checkout returns to the cart with items preserved."""
        page = logged_in_app
        self._go_to_checkout(page)
        page.click("[data-test='cancel']")

        expect(page.locator(".cart_item")).to_have_count(1)
        expect(page.locator(".shopping_cart_badge")).to_have_text("1")
