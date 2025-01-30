from appium.webdriver.common.appiumby import AppiumBy


def test_standard_user(android_rdc_driver):
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username').send_keys("standard_user")
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Password').send_keys("secret_sauce")
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN').click()

    assert android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-PRODUCTS').is_displayed()