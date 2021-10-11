import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_valid_crentials_login(driver):
    driver.get('http://www.saucedemo.com/v1')

    username_locator = (By.CSS_SELECTOR, '#user-name')
    password_locator = (By.CSS_SELECTOR, '#password')
    submit_locator = (By.CSS_SELECTOR, '.btn_action')

    wait = WebDriverWait(driver, 10)
    wait.until(lambda x: driver.find_element(by=username_locator[0], value=username_locator[1]).is_displayed)

    username_element = driver.find_element(by=username_locator[0], value=username_locator[1])
    password_element = driver.find_element(by=password_locator[0], value=password_locator[1])
    submit_element = driver.find_element(by=submit_locator[0], value=submit_locator[1])

    username_element.send_keys('standard_user')
    password_element.send_keys('secret_sauce')
    submit_element.click()

    assert "/inventory.html" in driver.current_url
