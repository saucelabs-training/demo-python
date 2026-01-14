SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username, password):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def test_inventory_page_loads(remote_browser):
    login(remote_browser, 'standard_user', 'secret_sauce')
    assert remote_browser.url.endswith("/inventory.html")
    assert remote_browser.locator('.inventory_list').is_visible()
    assert remote_browser.locator('.inventory_item').count() > 0

