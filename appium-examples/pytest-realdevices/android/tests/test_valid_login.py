import pytest
from time import sleep


def test_standard_user(driver):
    sleep(5)
    driver.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
    driver.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
    driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert driver.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()
