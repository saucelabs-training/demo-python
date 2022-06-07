from selenium.webdriver.common.by import By

def test_valid_credentials_login(rdc_browser):
    rdc_browser.get('https://www.saucedemo.com/v1')

    rdc_browser.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    rdc_browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    rdc_browser.find_element(By.CSS_SELECTOR, '.btn_action').click()

    assert rdc_browser.find_element(By.CSS_SELECTOR, '.error-button').is_displayed()
