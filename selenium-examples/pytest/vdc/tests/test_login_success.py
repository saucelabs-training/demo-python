import pytest


def test_valid_crentials_login(driver):
    driver.get('http://www.saucedemo.com')

    driver.find_element_by_id('user-name').send_keys('standard_user')
    driver.find_element_by_id('password').send_keys('secret_sauce')
    driver.find_element_by_css_selector('.btn_action').click()

    assert "/inventory.html" in driver.current_url
