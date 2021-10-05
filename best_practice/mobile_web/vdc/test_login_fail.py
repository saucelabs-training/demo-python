def test_valid_crentials_login(mobile_web_driver):
    mobile_web_driver.get('https://www.saucedemo.com/v1')

    mobile_web_driver.find_element_by_id('user-name').send_keys('locked_out_user')
    mobile_web_driver.find_element_by_id('password').send_keys('secret_sauce')
    mobile_web_driver.find_element_by_css_selector('.btn_action').click()

    assert mobile_web_driver.find_element_by_css_selector('.error-button').is_displayed()
