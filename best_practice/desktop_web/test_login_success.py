def test_valid_crentials_login(desktop_web_driver):
    desktop_web_driver.get('https://www.saucedemo.com/v1')

    desktop_web_driver.find_element_by_id('user-name').send_keys('standard_user')
    desktop_web_driver.find_element_by_id('password').send_keys('secret_sauce')
    desktop_web_driver.find_element_by_css_selector('.btn_action').click()

    assert "/inventory.html" in desktop_web_driver.current_url
