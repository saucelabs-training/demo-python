import pytest


def test_add_to_cart(emusim_driver):
    emusim_driver.get('https://www.saucedemo.com/v1/inventory.html')
    emusim_driver.find_element_by_class_name('btn_primary').click()

    assert emusim_driver.find_element_by_class_name('shopping_cart_badge').text == '1'

    emusim_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = emusim_driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 1

def test_add_two_to_cart(emusim_driver):
    emusim_driver.get('https://www.saucedemo.com/v1/inventory.html')
    emusim_driver.find_element_by_class_name('btn_primary').click()
    emusim_driver.find_element_by_class_name('btn_primary').click()

    assert emusim_driver.find_element_by_class_name('shopping_cart_badge').text == '2'

    emusim_driver.get('https://www.saucedemo.com/v1/cart.html')
    expected = emusim_driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 2
