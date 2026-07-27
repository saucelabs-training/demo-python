SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username, password):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def test_login_valid(page):
    login(page, 'standard_user', 'secret_sauce')
    assert page.url == SAUCE_DEMO_URL + "inventory.html"

def test_login_locked_out_user(page):
    login(page, 'locked_out_user', 'secret_sauce')
    assert "Sorry, this user has been locked out" in page.locator('[data-test="error"]').inner_text()

def test_login_invalid_credentials(page):
    login(page, 'invalid_user', 'invalid_password')
    assert "Username and password do not match" in page.locator('[data-test="error"]').inner_text()

def test_logout(page):
    login(page, 'standard_user', 'secret_sauce')

    page.click('#react-burger-menu-btn')
    page.click('#logout_sidebar_link')

    assert page.url == SAUCE_DEMO_URL
