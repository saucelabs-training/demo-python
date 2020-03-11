import pytest


def test_blank_credentials(android_driver):
    android_driver.find_element_by_accessibility_id("test-Username").send_keys("")
    android_driver.find_element_by_accessibility_id("test-Password").send_keys("")
    android_driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert android_driver.find_element_by_accessibility_id("test-Error message").is_displayed()
