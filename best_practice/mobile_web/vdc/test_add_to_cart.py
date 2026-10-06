from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ADD_TO_CART = (By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
CART_ITEM = (By.CLASS_NAME, 'inventory_item_name')
CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')


def test_add_to_cart(mobile_web_driver):
    wait = WebDriverWait(mobile_web_driver, 15)
    login(mobile_web_driver)
    scroll_and_click(mobile_web_driver, ADD_TO_CART)

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    assert mobile_web_driver.find_element(*CART_BADGE).text == '1'

    scroll_and_click(mobile_web_driver, CART_LINK)
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 1


def test_add_two_to_cart(mobile_web_driver):
    wait = WebDriverWait(mobile_web_driver, 15)
    login(mobile_web_driver)
    scroll_and_click(mobile_web_driver, ADD_TO_CART)
    # Wait for the cart to update so the next lookup finds a different product
    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '1'))
    scroll_and_click(mobile_web_driver, ADD_TO_CART)

    wait.until(EC.text_to_be_present_in_element(CART_BADGE, '2'))
    assert mobile_web_driver.find_element(*CART_BADGE).text == '2'

    scroll_and_click(mobile_web_driver, CART_LINK)
    expected = wait.until(EC.visibility_of_all_elements_located(CART_ITEM))
    assert len(expected) == 2


def scroll_and_click(driver, locator):
    # iOS Safari reports elements outside the viewport as not visible,
    # so bring the element into view before waiting for it to be clickable
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located(locator))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    wait.until(EC.element_to_be_clickable(element)).click()


def login(driver):
    # Log in through the UI so the app routes to the inventory without a full page
    # load; the iOS simulators sometimes lose the Safari page after one
    wait = WebDriverWait(driver, 15)
    driver.get('https://www.saucedemo.com')
    wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn_action'))).click()
    wait.until(EC.url_contains('/inventory.html'))
