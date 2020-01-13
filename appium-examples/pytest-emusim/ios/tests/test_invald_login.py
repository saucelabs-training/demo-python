import pytest


def test_blank_credentials(driver):
    driver.find_element_by_accessibility_id("test-Username").send_keys("")
    driver.find_element_by_accessibility_id("test-Password").send_keys("")
    driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert driver.find_element_by_accessibility_id("test-Error message").is_displayed()
