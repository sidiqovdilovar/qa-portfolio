"""Authentication tests for saucedemo.com.

Covers: successful login, blocked account, wrong password.
"""
from playwright.sync_api import expect

BASE_URL = "https://www.saucedemo.com"


class TestLogin:

    def test_successful_login(self, app):
        """TC-01: valid credentials lead to the product list."""
        app.fill("#user-name", "standard_user")
        app.fill("#password", "secret_sauce")
        app.click("#login-button")

        expect(app).to_have_url(f"{BASE_URL}/inventory.html")
        expect(app.locator(".title")).to_have_text("Products")

    def test_locked_out_user_cannot_login(self, app):
        """TC-04: blocked account shows a clear error and stays on the login page."""
        app.fill("#user-name", "locked_out_user")
        app.fill("#password", "secret_sauce")
        app.click("#login-button")

        error = app.locator("[data-test='error']")
        expect(error).to_be_visible()
        expect(error).to_contain_text("Sorry, this user has been locked out")
        expect(app).to_have_url(BASE_URL + "/")

    def test_wrong_password_shows_error(self, app):
        """TC-02: wrong password is rejected with an error message."""
        app.fill("#user-name", "standard_user")
        app.fill("#password", "wrong_password")
        app.click("#login-button")

        error = app.locator("[data-test='error']")
        expect(error).to_be_visible()
        expect(error).to_contain_text("Username and password do not match")

    def test_empty_credentials_show_validation(self, app):
        """TC-03: empty fields block the login attempt."""
        app.click("#login-button")

        error = app.locator("[data-test='error']")
        expect(error).to_be_visible()
        expect(error).to_contain_text("Username is required")
