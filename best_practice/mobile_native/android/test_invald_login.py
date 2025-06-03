from appium.webdriver.common.appiumby import AppiumBy


def test_blank_credentials(android_rdc_driver):
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='View menu').click()

    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Login Menu Item').click()
    android_rdc_driver.find_element(by=AppiumBy.ID, value='com.saucelabs.mydemoapp.android:id/nameET').send_keys("alice@example.com")
    android_rdc_driver.find_element(by=AppiumBy.ID, value='com.saucelabs.mydemoapp.android:id/passwordET').send_keys("secret_sauce")
    android_rdc_driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Tap to login with given credentials').click()

    error_element = android_rdc_driver.find_element(by=AppiumBy.ID, value='com.saucelabs.mydemoapp.android:id/passwordErrorTV')

    assert error_element.text == "Sorry this user has been locked out."