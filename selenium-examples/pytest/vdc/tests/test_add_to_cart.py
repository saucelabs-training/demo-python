import pytest


def test_add_to_cart(vdc_driver):
    vdc_driver.get('https://www.saucedemo.com/inventory.html')
    vdc_driver.find_element_by_class_name('btn_primary').click()

    assert vdc_driver.find_element_by_class_name('shopping_cart_badge').text == '1'

    vdc_driver.get('https://www.saucedemo.com/cart.html')
    expected = vdc_driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(vdc_driver):
    vdc_driver.get('https://www.saucedemo.com/inventory.html')
    vdc_driver.find_element_by_class_name('btn_primary').click()
    vdc_driver.find_element_by_class_name('btn_primary').click()

    assert vdc_driver.find_element_by_class_name('shopping_cart_badge').text == '2'

    vdc_driver.get('https://www.saucedemo.com/cart.html')
    expected = vdc_driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 2
