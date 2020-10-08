import pytest
from time import sleep


def test_standard_user(android_driver):
    sleep(5)
    android_driver.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
    android_driver.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
    android_driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert android_driver.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()
