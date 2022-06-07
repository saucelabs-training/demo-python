import pytest
from os import environ

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.remote_connection import RemoteConnection

import urllib3

urllib3.disable_warnings()

browsers = [
    {
        "platform": "Linux",
        "browserName": "firefox",
        "version": "latest"

    }, {
        "platform": "Linux",
        "browserName": "firefox",
        "version": "latest-1"

    }, {
        "platform": "Linux",
        "browserName": "firefox",
        "version": "latest"

    }, {
        "platform": "Linux",
        "browserName": "chrome",
        "version": "latest-1",
    }]


def pytest_generate_tests(metafunc):
    if 'driver' in metafunc.fixturenames:
        metafunc.parametrize('browser_config',
                             browsers,
                             ids=_generate_param_ids('broswerConfig', browsers),
                             scope='function')


def _generate_param_ids(name, values):
    return [("<%s:%s>" % (name, value)).replace('.', '_') for value in values]


@pytest.yield_fixture(scope='function')
def driver(request, browser_config):
    desired_caps = dict()
    desired_caps.update(browser_config)
    test_name = request.node.name
    build_tag = environ.get('BUILD_TAG', "local run")
    username = environ['SAUCE_USERNAME']
    access_key = environ['SAUCE_ACCESS_KEY']

    # for headless testing you must use the east coast data center endpoint
    selenium_endpoint = "https://ondemand.us-east-1.saucelabs.com/wd/hub"
    desired_caps['build'] = build_tag
    desired_caps['name'] = test_name
    desired_caps['username'] = username
    desired_caps['accessKey'] = access_key

    executor = RemoteConnection(selenium_endpoint, resolve_ip=False)
    browser = webdriver.Remote(executor, desired_capabilities=desired_caps)

    yield browser
    # Teardown starts here
    # report results
    # use the test result to send the pass/fail status to Sauce Labs
    browser.quit()

@pytest.mark.usefixtures("driver")
def test_valid_crentials_login(driver):
    driver.get('http://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('locked_out_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, '.btn_action').click()

    assert driver.find_element(By.CSS_SELECTOR'.error-button').is_displayed()


@pytest.mark.usefixtures("driver")
def test_valid_crentials_login(driver):
    driver.get('http://www.saucedemo.com')

    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, '.btn_action').click()

    assert "/inventory.html" in driver.current_url
