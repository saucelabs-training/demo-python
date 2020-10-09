def test_standard_user(ios_up_driver):
    ios_up_driver.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
    ios_up_driver.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
    ios_up_driver.find_element_by_accessibility_id("test-LOGIN").click()

    assert ios_up_driver.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()
