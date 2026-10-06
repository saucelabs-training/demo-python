from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADD_TO_CART = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
REMOVE_FROM_CART = (By.CSS_SELECTOR, '[data-test^="remove"]')
CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
CART_ITEM = (By.CLASS_NAME, 'inventory_item_name')


def test_add_and_remove_from_cart(mobile_web_driver):
    wait = WebDriverWait(mobile_web_driver, 15)
    set_cookie(mobile_web_driver)
    mobile_web_driver.get('https://www.saucedemo.com/inventory.html')
    scroll_and_click(mobile_web_driver, ADD_TO_CART)
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    scroll_and_click(mobile_web_driver, ADD_TO_CART)
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '2'))
    scroll_and_click(mobile_web_driver, REMOVE_FROM_CART)

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    assert mobile_web_driver.find_element(*CART_BADGE).text == '1'

    mobile_web_driver.get('https://www.saucedemo.com/cart.html')
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 1


def scroll_and_click(driver, locator):
    # iOS Safari reports elements outside the viewport as not visible,
    # so bring the element into view before waiting for it to be clickable
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    wait.until(EC.element_to_be_clickable(element)).click()


def set_cookie(driver):
    driver.get("https://www.saucedemo.com/")
    cookie = {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/"
    }
    driver.add_cookie(cookie)
