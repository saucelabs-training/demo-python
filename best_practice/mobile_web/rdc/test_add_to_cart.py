def test_add_to_cart(rdc_browser):
    rdc_browser.get('https://www.saucedemo.com/v1/inventory.html')
    rdc_browser.find_element_by_class_name('btn_primary').click()

    assert rdc_browser.find_element_by_class_name('shopping_cart_badge').text == '1'

    rdc_browser.get('https://www.saucedemo.com/v1/cart.html')
    expected = rdc_browser.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(rdc_browser):
    rdc_browser.get('https://www.saucedemo.com/v1/inventory.html')
    rdc_browser.find_element_by_class_name('btn_primary').click()
    rdc_browser.find_element_by_class_name('btn_primary').click()

    assert rdc_browser.find_element_by_class_name('shopping_cart_badge').text == '2'

    rdc_browser.get('https://www.saucedemo.com/v1/cart.html')
    expected = rdc_browser.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 2
