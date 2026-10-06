from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_valid_credentials_login(rdc_browser):
    wait = WebDriverWait(rdc_browser, 15)
    rdc_browser.get('https://www.saucedemo.com')

    wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('locked_out_user')
    rdc_browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn_action'))).click()

    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.error-button'))).is_displayed()
