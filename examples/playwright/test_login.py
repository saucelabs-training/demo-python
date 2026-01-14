SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def test_login_valid(remote_browser):
    remote_browser.goto(SAUCE_DEMO_URL)
    remote_browser.fill('input[data-test="username"]', 'standard_user')
    remote_browser.fill('input[data-test="password"]', 'secret_sauce')
    remote_browser.click('input[data-test="login-button"]')
    assert remote_browser.url.endswith("/inventory.html")

def test_login_invalid(remote_browser):
    remote_browser.goto(SAUCE_DEMO_URL)
    remote_browser.fill('input[data-test="username"]', 'locked_out_user')
    remote_browser.fill('input[data-test="password"]', 'wrong_password')
    remote_browser.click('input[data-test="login-button"]')
    assert remote_browser.locator('h3[data-test="error"]').is_visible()

