def test_standard_user(ios_rdc_driver):
    ios_rdc_driver.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
    ios_rdc_driver.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
    ios_rdc_driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert ios_rdc_driver.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()
