from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADD_TO_CART = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
REMOVE_FROM_CART = (By.CSS_SELECTOR, '[data-test^="remove"]')
CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
CART_ITEM = (By.CLASS_NAME, 'inventory_item_name')


def test_add_and_remove_from_cart(rdc_browser):
    wait = WebDriverWait(rdc_browser, 15)
    set_cookie(rdc_browser)
    rdc_browser.get('https://www.saucedemo.com/inventory.html')
    wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '2'))
    wait.until(EC.element_to_be_clickable(REMOVE_FROM_CART)).click()

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    assert rdc_browser.find_element(*CART_BADGE).text == '1'

    rdc_browser.get('https://www.saucedemo.com/cart.html')
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 1


def set_cookie(driver):
    driver.get("https://www.saucedemo.com/")
    cookie = {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/"
    }
    driver.add_cookie(cookie)
