from playwright.sync_api import expect

SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username, password):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def test_inventory_page_loads(page):
    login(page, 'standard_user', 'secret_sauce')
    assert page.url.endswith("/inventory.html")
    expect(page.locator('.inventory_list')).to_be_visible()
    assert page.locator('.inventory_item').count() > 0
