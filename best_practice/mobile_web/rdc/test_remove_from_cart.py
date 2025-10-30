from selenium.webdriver.common.by import By


def test_add_and_remove_from_cart(rdc_browser):
    rdc_browser.get("https://www.saucedemo.com/")
    cookie = {
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com",
        "path": "/"
    }
    rdc_browser.add_cookie(cookie)
    rdc_browser.get('https://www.saucedemo.com/inventory.html')
    rdc_browser.find_element(By.CLASS_NAME, 'btn_primary').click()
    rdc_browser.find_element(By.CLASS_NAME, 'btn_primary').click()
    rdc_browser.find_element(By.CLASS_NAME, 'btn_secondary').click()

    assert rdc_browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    rdc_browser.get('https://www.saucedemo.com/cart.html')
    expected = rdc_browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(expected) == 1
