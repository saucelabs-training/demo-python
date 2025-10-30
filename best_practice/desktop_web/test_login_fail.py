from selenium.webdriver.common.by import By


def test_valid_credentials_login(desktop_web_driver):
    desktop_web_driver.get('https://www.saucedemo.com')

    desktop_web_driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    desktop_web_driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    desktop_web_driver.find_element(By.CSS_SELECTOR, '.btn_action').click()

    assert desktop_web_driver.find_element(By.CSS_SELECTOR, '.error-button').is_displayed()
