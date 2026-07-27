SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def test_login_valid(page):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', 'standard_user')
    page.fill('input[data-test="password"]', 'secret_sauce')
    page.click('input[data-test="login-button"]')
    assert page.url.endswith("/inventory.html")

def test_login_invalid(page):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', 'locked_out_user')
    page.fill('input[data-test="password"]', 'wrong_password')
    page.click('input[data-test="login-button"]')
    assert page.locator('h3[data-test="error"]').is_visible()
