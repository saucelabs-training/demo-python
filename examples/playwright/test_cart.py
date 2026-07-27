SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username="standard_user", password="secret_sauce"):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def test_add_item_to_cart_from_inventory(page):
    login(page)

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')

    assert page.locator('.shopping_cart_badge').inner_text() == "1"

def test_add_multiple_items_to_cart(page):
    login(page)

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
    page.click('[data-test="add-to-cart-sauce-labs-onesie"]')

    assert page.locator('.shopping_cart_badge').inner_text() == "3"

def test_remove_item_from_inventory(page):
    login(page)

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('[data-test="remove-sauce-labs-backpack"]')

    assert page.locator('.shopping_cart_badge').count() == 0

def test_remove_item_from_cart(page):
    login(page)

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('.shopping_cart_link')
    page.click('[data-test="remove-sauce-labs-backpack"]')

    assert page.locator('.shopping_cart_badge').count() == 0

def test_continue_shopping_from_cart(page):
    login(page)

    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('.shopping_cart_link')
    page.click('[data-test="continue-shopping"]')

    assert page.url == SAUCE_DEMO_URL + "inventory.html"
