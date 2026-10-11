"""Shopping cart tests for saucedemo.com.

Covers: adding one/two products, cart badge counter, removing a product.
"""
from playwright.sync_api import expect


class TestCart:

    def test_add_one_product_to_cart(self, logged_in_app):
        """TC-06: after adding a product the button flips and the badge shows 1."""
        page = logged_in_app
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

        expect(page.locator(".shopping_cart_badge")).to_have_text("1")
        expect(page.locator("[data-test='remove-sauce-labs-backpack']")).to_be_visible()

    def test_add_two_products_badge_shows_two(self, logged_in_app):
        """TC-08: badge counts every added product."""
        page = logged_in_app
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        page.locator("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()

        expect(page.locator(".shopping_cart_badge")).to_have_text("2")

    def test_remove_product_from_cart(self, logged_in_app):
        """TC-07: removed product disappears and the badge is cleared."""
        page = logged_in_app
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
        page.locator("[data-test='remove-sauce-labs-backpack']").click()

        expect(page.locator(".shopping_cart_badge")).to_have_count(0)
