import pytest


def test_add_and_remove_from_cart(driver):
    driver.get('http://www.saucedemo.com/inventory.html')
    driver.find_element_by_class_name('btn_primary').click()
    driver.find_element_by_class_name('btn_primary').click()
    driver.find_element_by_class_name('btn_secondary').click()

    assert driver.find_element_by_class_name('shopping_cart_badge').text == '1'

    driver.get('http://www.saucedemo.com/cart.html')
    expected = driver.find_elements_by_class_name('inventory_item_name')
    assert len(expected) == 1
