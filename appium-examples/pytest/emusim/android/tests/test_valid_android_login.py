def test_standard_user(android_emusim):
    android_emusim.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
    android_emusim.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
    android_emusim.find_element_by_accessibility_id("test-LOGIN").click()

    assert android_emusim.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()
