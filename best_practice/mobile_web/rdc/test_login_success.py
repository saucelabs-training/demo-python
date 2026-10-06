from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_valid_crentials_login(rdc_browser):
    wait = WebDriverWait(rdc_browser, 15)
    rdc_browser.get('https://www.saucedemo.com')

    wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
    rdc_browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn_action'))).click()

    wait.until(EC.url_contains('/inventory.html'))
    assert "/inventory.html" in rdc_browser.current_url
