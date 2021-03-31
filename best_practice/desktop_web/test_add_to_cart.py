def test_add_to_cart(desktop_web_driver):
    desktop_web_driver.get('https://www.saucedemo.com/v1/inventory.html')
    desktop_web_driver.find_element_by_class_name('btn_primary').click()

    assert desktop_web_driver.find_element_by_class_name('shopping_cart_badge').text == '1'

    desktop_web_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = desktop_web_driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(desktop_web_driver):
    desktop_web_driver.get('https://www.saucedemo.com/v1/inventory.html')
    desktop_web_driver.find_element_by_class_name('btn_primary').click()
    desktop_web_driver.find_element_by_class_name('btn_primary').click()

    assert desktop_web_driver.find_element_by_class_name('shopping_cart_badge').text == '2'

    desktop_web_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = desktop_web_driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 2
