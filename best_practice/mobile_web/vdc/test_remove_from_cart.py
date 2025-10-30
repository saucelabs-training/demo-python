from selenium.webdriver.common.by import By


def test_add_and_remove_from_cart(mobile_web_driver):
    set_cookie(mobile_web_driver)
    mobile_web_driver.get('https://www.saucedemo.com/inventory.html')
    mobile_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()
    mobile_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()
    mobile_web_driver.find_element(By.CLASS_NAME, 'btn_secondary').click()

    assert mobile_web_driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    mobile_web_driver.get('https://www.saucedemo.com/cart.html')
    expected = mobile_web_driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
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
