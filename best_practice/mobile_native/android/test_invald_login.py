from appium.webdriver.common.appiumby import AppiumBy


def test_blank_credentials(android_rdc_driver):
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username').send_keys("")
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Password').send_keys("")
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN').click()

    assert android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Error message').is_displayed()
