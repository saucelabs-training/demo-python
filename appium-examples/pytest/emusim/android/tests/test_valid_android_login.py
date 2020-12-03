def test_standard_user(android_emulator):
    android_emulator.find_element_by_accessibility_id("test-Username").send_keys("standard_user")
    android_emulator.find_element_by_accessibility_id("test-Password").send_keys("secret_sauce")
    android_emulator.find_element_by_accessibility_id("test-LOGIN").click()

    assert android_emulator.find_element_by_accessibility_id("test-PRODUCTS").is_displayed()
