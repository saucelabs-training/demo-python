from selenium.webdriver.common.by import By


def test_valid_crentials_login(mobile_web_driver):
    mobile_web_driver.get('https://www.saucedemo.com')

    mobile_web_driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    mobile_web_driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    mobile_web_driver.find_element(By.CSS_SELECTOR, '.btn_action').click()

    assert mobile_web_driver.find_element(By.CSS_SELECTOR, '.error-button').is_displayed()
