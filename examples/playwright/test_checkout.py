SAUCE_DEMO_URL = "https://www.saucedemo.com/"

def login(page, username="standard_user", password="secret_sauce"):
    page.goto(SAUCE_DEMO_URL)
    page.fill('input[data-test="username"]', username)
    page.fill('input[data-test="password"]', password)
    page.click('input[data-test="login-button"]')

def add_backpack_and_go_to_checkout(page):
    page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
    page.click('.shopping_cart_link')
    page.click('[data-test="checkout"]')

def test_complete_checkout(page):
    login(page)
    add_backpack_and_go_to_checkout(page)

    page.fill('[data-test="firstName"]', "John")
    page.fill('[data-test="lastName"]', "Doe")
    page.fill('[data-test="postalCode"]', "12345")
    page.click('[data-test="continue"]')

    assert page.url == SAUCE_DEMO_URL + "checkout-step-two.html"

    page.click('[data-test="finish"]')

    assert page.locator('.complete-header').inner_text() == "Thank you for your order!"

def test_checkout_with_missing_first_name(page):
    login(page)
    add_backpack_and_go_to_checkout(page)

    # Leave first name empty
    page.fill('[data-test="lastName"]', "Doe")
    page.fill('[data-test="postalCode"]', "12345")
    page.click('[data-test="continue"]')

    assert "Error: First Name is required" in page.locator('[data-test="error"]').inner_text()

def test_checkout_with_missing_last_name(page):
    login(page)
    add_backpack_and_go_to_checkout(page)

    page.fill('[data-test="firstName"]', "John")
    # Leave last name empty
    page.fill('[data-test="postalCode"]', "12345")
    page.click('[data-test="continue"]')

    assert "Error: Last Name is required" in page.locator('[data-test="error"]').inner_text()

def test_checkout_with_missing_postal_code(page):
    login(page)
    add_backpack_and_go_to_checkout(page)

    page.fill('[data-test="firstName"]', "John")
    page.fill('[data-test="lastName"]', "Doe")
    # Leave postal code empty
    page.click('[data-test="continue"]')

    assert "Error: Postal Code is required" in page.locator('[data-test="error"]').inner_text()

def test_cancel_checkout(page):
    login(page)
    add_backpack_and_go_to_checkout(page)

    page.click('[data-test="cancel"]')

    assert page.url == SAUCE_DEMO_URL + "cart.html"
