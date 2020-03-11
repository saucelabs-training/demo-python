import pytest


def test_valid_crentials_login(emusim_driver):
    emusim_driver.get('https://www.saucedemo.com')

    emusim_driver.find_element_by_id('user-name').send_keys('standard_user')
    emusim_driver.find_element_by_id('password').send_keys('secret_sauce')
    emusim_driver.find_element_by_css_selector('.btn_action').click()

    assert "/inventory.html" in emusim_driver.current_url
