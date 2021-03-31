def test_blank_credentials(android_rdc_driver):
    android_rdc_driver.find_element_by_accessibility_id("test-Username").send_keys("")
    android_rdc_driver.find_element_by_accessibility_id("test-Password").send_keys("")
    android_rdc_driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert android_rdc_driver.find_element_by_accessibility_id("test-Error message").is_displayed()
