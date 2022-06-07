from selenium.webdriver.common.by import By


def test_add_to_cart(desktop_web_driver):
    desktop_web_driver.get('https://www.saucedemo.com/v1/inventory.html')
    desktop_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()

    assert desktop_web_driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    desktop_web_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = desktop_web_driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(desktop_web_driver):
    desktop_web_driver.get('https://www.saucedemo.com/v1/inventory.html')
    desktop_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()
    desktop_web_driver.find_element(By.CLASS_NAME, 'btn_primary').click()

    assert desktop_web_driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '2'

    desktop_web_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = desktop_web_driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(expected) == 2
