def test_valid_crentials_login(mobile_web_driver):
    mobile_web_driver.get('https://www.saucedemo.com/v1')

    mobile_web_driver.find_element_by_id('user-name').send_keys('standard_user')
    mobile_web_driver.find_element_by_id('password').send_keys('secret_sauce')
    mobile_web_driver.find_element_by_css_selector('.btn_action').click()

    assert "/inventory.html" in mobile_web_driver.current_url
