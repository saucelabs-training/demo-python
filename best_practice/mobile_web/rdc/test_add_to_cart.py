from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADD_TO_CART = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
CART_ITEM = (By.CLASS_NAME, 'inventory_item_name')


def test_add_to_cart(rdc_browser):
    wait = WebDriverWait(rdc_browser, 15)
    set_cookie(rdc_browser)
    rdc_browser.get('https://www.saucedemo.com/inventory.html')
    scroll_and_click(rdc_browser, ADD_TO_CART)

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    assert rdc_browser.find_element(*CART_BADGE).text == '1'

    rdc_browser.get('https://www.saucedemo.com/cart.html')
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 1


def test_add_two_to_cart(rdc_browser):
    wait = WebDriverWait(rdc_browser, 15)
    set_cookie(rdc_browser)
    rdc_browser.get('https://www.saucedemo.com/inventory.html')
    scroll_and_click(rdc_browser, ADD_TO_CART)
    # Wait for the cart to update so the next lookup finds a different product
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    scroll_and_click(rdc_browser, ADD_TO_CART)

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '2'))
    assert rdc_browser.find_element(*CART_BADGE).text == '2'

    rdc_browser.get('https://www.saucedemo.com/cart.html')
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 2


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
