def test_blank_credentials(android_emulator):
    android_emulator.find_element_by_accessibility_id("test-Username").send_keys("")
    android_emulator.find_element_by_accessibility_id("test-Password").send_keys("")
    android_emulator.find_element_by_accessibility_id("test-LOGIN").click()

    assert android_emulator.find_element_by_accessibility_id("test-Error message").is_displayed()
