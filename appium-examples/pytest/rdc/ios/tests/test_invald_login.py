def test_blank_credentials(ios_up_driver):
    ios_up_driver.find_element_by_accessibility_id("test-Username").send_keys("")
    ios_up_driver.find_element_by_accessibility_id("test-Password").send_keys("")
    ios_up_driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert ios_up_driver.find_element_by_accessibility_id("test-Error message").is_displayed()
