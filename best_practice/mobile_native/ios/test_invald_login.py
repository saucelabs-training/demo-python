from appium.webdriver.common.appiumby import AppiumBy


def test_blank_credentials(ios_rdc_driver):
    ios_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Username').send_keys("")
    ios_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Password').send_keys("")
    ios_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-LOGIN').click()

    assert ios_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='test-Error message').is_displayed()
