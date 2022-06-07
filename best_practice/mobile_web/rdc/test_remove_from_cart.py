from selenium.webdriver.common.by import By


def test_add_and_remove_from_cart(rdc_browser):
    rdc_browser.get('https://www.saucedemo.com/v1/inventory.html')
    rdc_browser.find_element(By.CLASS_NAME, 'btn_primary').click()
    rdc_browser.find_element(By.CLASS_NAME, 'btn_primary').click()
    rdc_browser.find_element(By.CLASS_NAME, 'btn_secondary').click()

    assert rdc_browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1'

    rdc_browser.get('https://www.saucedemo.com/v1/cart.html')
    expected = rdc_browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert len(expected) == 1
