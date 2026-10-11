"""Shared pytest fixtures: browser (session scope) and page (function scope).

Each test gets a fresh browser context, so cookies and local storage
never leak between tests.
"""
import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture()
def page(browser):
    context = browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()
    page.set_default_timeout(10_000)
    yield page
    context.close()


@pytest.fixture()
def app(page):
    """Opens the login page and returns it ready for actions."""
    page.goto(BASE_URL)
    return page


@pytest.fixture()
def logged_in_app(app):
    """Logs in as standard_user and lands on the product list."""
    app.fill("#user-name", "standard_user")
    app.fill("#password", "secret_sauce")
    app.click("#login-button")
    app.wait_for_url(f"{BASE_URL}/inventory.html")
    return app
