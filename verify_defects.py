#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Live verification of the defects reported in 04_bug_reports.md.

Reproduces every defect against the real application and re-captures the screenshots,
so each bug report in this portfolio can be independently verified.

Run:
    pip install -r automation/requirements.txt
    playwright install chromium
    python3 verify_defects.py

Output: screenshots/*.png + screenshots/VERIFICATION_RESULTS.txt
"""
import os
from playwright.sync_api import sync_playwright

BASE = "https://www.saucedemo.com"
OUT = "screenshots"
os.makedirs(OUT, exist_ok=True)
results = []


def note(kind, text):
    results.append(f"{kind} | {text}")
    print(f"{kind} | {text}")


def login(page, user, password="secret_sauce"):
    page.goto(BASE)
    page.fill("#user-name", user)
    page.fill("#password", password)
    page.click("#login-button")


def new_ctx(browser):
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.set_default_timeout(15000)
    return ctx, page


with sync_playwright() as pw:
    browser = pw.chromium.launch()

    # BUG-01 — product images are not displayed
    ctx, page = new_ctx(browser)
    login(page, "problem_user")
    page.wait_for_url(f"{BASE}/inventory.html")
    page.wait_for_timeout(800)
    srcs = page.eval_on_selector_all(".inventory_item_img img", "els => els.map(e => e.getAttribute('src'))")
    loaded = page.evaluate("() => Array.from(document.querySelectorAll('.inventory_item_img img'))"
                           ".filter(i => i.complete && i.naturalWidth > 0).length")
    note("INFO", f"BUG-01: продуктов={len(srcs)}, уникальных src={len(set(srcs))}, "
                 f"загружено={loaded}, пример src={srcs[0] if srcs else '-'}")
    note("BUG ", "BUG-01 подтверждён: все товары показывают один и тот же 404-плейсхолдер."
         if len(set(srcs)) == 1 and len(srcs) > 1
         else "BUG-01 не подтверждён: у товаров разные изображения.")
    page.screenshot(path=f"{OUT}/bug-01_product-images-missing.png", full_page=True)
    ctx.close()

    # BUG-02 — sorting has no effect
    ctx, page = new_ctx(browser)
    login(page, "problem_user")
    page.wait_for_url(f"{BASE}/inventory.html")
    orders = {}
    for mode in ("za", "lohi", "hilo"):
        page.select_option(".product_sort_container", mode)
        page.wait_for_timeout(600)
        orders[mode] = page.eval_on_selector_all(".inventory_item_name", "els => els.map(e => e.textContent)")
    same = orders["za"] == orders["lohi"] == orders["hilo"]
    note("INFO", f"BUG-02: порядок одинаков для всех режимов сортировки = {same}")
    note("BUG ", "BUG-02 подтверждён: сортировка не работает." if same
         else "BUG-02 не подтверждён: сортировка работает.")
    page.screenshot(path=f"{OUT}/bug-02_sorting-not-working.png", full_page=True)
    ctx.close()

    # BUG-03 — Last Name does not accept input
    ctx, page = new_ctx(browser)
    login(page, "problem_user")
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click(".shopping_cart_link")
    page.click('[data-test="checkout"]')
    page.fill('[data-test="firstName"]', "Ivan")
    page.fill('[data-test="lastName"]', "Ivanov")
    page.fill('[data-test="postalCode"]', "12345")
    first, last = page.input_value('[data-test="firstName"]'), page.input_value('[data-test="lastName"]')
    note("INFO", f"BUG-03: first='{first}', last='{last}'")
    note("BUG ", "BUG-03 подтверждён: поле Last Name не принимает ввод." if last != "Ivanov"
         else "BUG-03 не подтверждён: поле принимает ввод.")
    page.screenshot(path=f"{OUT}/bug-03_checkout-lastname-field.png")
    ctx.close()

    # BUG-04 — Add to cart works for only 3 of 6 products
    ctx, page = new_ctx(browser)
    login(page, "problem_user")
    page.wait_for_url(f"{BASE}/inventory.html")
    page.wait_for_timeout(600)
    for i in range(6):
        page.locator(".inventory_item button").nth(i).click()
        page.wait_for_timeout(200)
    page.click(".shopping_cart_link")
    page.wait_for_timeout(400)
    in_cart = page.locator(".cart_item").count()
    note("INFO", f"BUG-04: товаров в корзине после 6 кликов = {in_cart}")
    note("BUG ", f"BUG-04 подтверждён: работают только {in_cart} из 6 кнопок." if in_cart != 6
         else "BUG-04 не подтверждён: все кнопки работают.")
    page.screenshot(path=f"{OUT}/bug-04_add-to-cart-buttons.png", full_page=True)
    ctx.close()

    # RETESTS — suspected issues that should NOT reproduce
    ctx, page = new_ctx(browser)
    login(page, "standard_user")
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click(".shopping_cart_link")
    page.click('[data-test="checkout"]')
    page.fill('[data-test="firstName"]', "Ivan")
    page.fill('[data-test="lastName"]', "Ivanov")
    page.click('[data-test="continue"]')
    page.wait_for_timeout(500)
    err = page.locator('[data-test="error"]')
    note("RETEST", "RT-02: пустой Postal Code -> ошибка показана: "
         f"{err.inner_text().strip() if err.count() else 'НЕТ'}")
    page.screenshot(path=f"{OUT}/retest-01_postal-code-validation.png")
    ctx.close()

    ctx, page = new_ctx(browser)
    login(page, "standard_user")
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click(".shopping_cart_link")
    page.click('[data-test="checkout"]')
    page.fill('[data-test="firstName"]', "Ivan")
    page.fill('[data-test="lastName"]', "Ivanov")
    page.fill('[data-test="postalCode"]', "12345")
    page.click('[data-test="continue"]')
    page.click('[data-test="finish"]', no_wait_after=True)
    page.wait_for_timeout(1200)
    ok = page.locator(".complete-header").count() > 0
    note("RETEST", f"RT-01: заказ оформлен с первого клика Finish = {ok}")
    page.screenshot(path=f"{OUT}/retest-03_finish-button-order-completed.png")
    ctx.close()

    browser.close()

with open(f"{OUT}/VERIFICATION_RESULTS.txt", "w", encoding="utf-8") as f:
    f.write("DEFECT VERIFICATION — saucedemo.com\n2026-10-11 | Chromium (Playwright) | 1440x900\n")
    f.write("=" * 70 + "\n" + "\n".join(results) + "\n")

print("\nГотово. Результаты: " + f"{OUT}/VERIFICATION_RESULTS.txt")
