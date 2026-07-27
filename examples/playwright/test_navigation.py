import re

SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username="standard_user", password="secret_sauce"):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def test_navigate_to_product_details(page):
    login(page)

    page.click('[data-test="item-4-title-link"]')

    assert re.search(r"inventory-item\.html\?id=4", page.url)
    assert page.locator('[data-test="inventory-item-name"]').inner_text() == "Sauce Labs Backpack"

def test_navigate_back_to_products(page):
    login(page)

    page.click('[data-test="item-4-title-link"]')
    page.click('[data-test="back-to-products"]')

    assert page.url == SAUCE_DEMO_URL + "inventory.html"

def test_navigate_to_cart(page):
    login(page)

    page.click('.shopping_cart_link')

    assert page.url == SAUCE_DEMO_URL + "cart.html"

def test_navigate_using_burger_menu(page):
    login(page)

    page.click('#react-burger-menu-btn')
    page.click('#about_sidebar_link')

    assert page.url == "https://saucelabs.com/"

def test_reset_app_state(page):
    login(page)

    # Add items to cart
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')

    assert page.locator('.shopping_cart_badge').inner_text() == "2"

    # Reset app state
    page.click('#react-burger-menu-btn')
    page.click('#reset_sidebar_link')

    # Verify cart is empty
    assert page.locator('.shopping_cart_badge').count() == 0
