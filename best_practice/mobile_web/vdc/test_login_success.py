from selenium.webdriver.common.by import By


def test_valid_credentials_login(mobile_web_driver):
    mobile_web_driver.get('https://www.saucedemo.com/v1')

    mobile_web_driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    mobile_web_driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    mobile_web_driver.find_element(By.CSS_SELECTOR, '.btn_action').click()

    assert "/inventory.html" in mobile_web_driver.current_url
