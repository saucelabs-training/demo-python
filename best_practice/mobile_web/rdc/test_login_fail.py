def test_valid_crentials_login(rdc_browser):
    rdc_browser.get('https://www.saucedemo.com/v1')

    rdc_browser.find_element_by_id('user-name').send_keys('locked_out_user')
    rdc_browser.find_element_by_id('password').send_keys('secret_sauce')
    rdc_browser.find_element_by_css_selector('.btn_action').click()

    assert rdc_browser.find_element_by_css_selector('.error-button').is_displayed()
