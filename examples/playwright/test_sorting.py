SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username="standard_user", password="secret_sauce"):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def test_sort_by_name_a_to_z(page):
    login(page)

    page.select_option('[data-test="product-sort-container"]', "az")

    assert page.locator('[data-test="inventory-item-name"]').first.inner_text() == "Sauce Labs Backpack"

def test_sort_by_name_z_to_a(page):
    login(page)

    page.select_option('[data-test="product-sort-container"]', "za")

    assert page.locator('[data-test="inventory-item-name"]').first.inner_text() == "Test.allTheThings() T-Shirt (Red)"

def test_sort_by_price_low_to_high(page):
    login(page)

    page.select_option('[data-test="product-sort-container"]', "lohi")

    assert page.locator('[data-test="inventory-item-price"]').first.inner_text() == "$7.99"

def test_sort_by_price_high_to_low(page):
    login(page)

    page.select_option('[data-test="product-sort-container"]', "hilo")

    assert page.locator('[data-test="inventory-item-price"]').first.inner_text() == "$49.99"
