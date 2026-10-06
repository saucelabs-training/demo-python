from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADD_TO_CART = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
CART_ITEM = (By.CLASS_NAME, 'inventory_item_name')


def test_add_to_cart(mobile_web_driver):
    wait = WebDriverWait(mobile_web_driver, 15)
    open_inventory(mobile_web_driver).click()

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    assert mobile_web_driver.find_element(*CART_BADGE).text == '1'

    mobile_web_driver.get('https://www.saucedemo.com/cart.html')
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 1


def test_add_two_to_cart(mobile_web_driver):
    wait = WebDriverWait(mobile_web_driver, 15)
    open_inventory(mobile_web_driver).click()
    # Wait for the cart to update so the next lookup finds a different product
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '2'))
    assert mobile_web_driver.find_element(*CART_BADGE).text == '2'

    mobile_web_driver.get('https://www.saucedemo.com/cart.html')
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 2


def open_inventory(driver):
    # The iOS simulators intermittently render inventory.html without any
    # products, so inject the session cookie and load the page again once
    for _ in range(2):
        set_cookie(driver)
        driver.get('https://www.saucedemo.com/inventory.html')
        try:
            return WebDriverWait(driver, 15).until(EC.element_to_be_clickable(ADD_TO_CART))
        except TimeoutException:
            pass
    raise TimeoutException("No add to cart button found, page was {}".format(driver.current_url))


def set_cookie(driver):
    driver.get("https://www.saucedemo.com/")
    cookie = {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/"
    }
    driver.add_cookie(cookie)
