# Selenium 3.14+ doesn't enable certificate checking
import pytest
import os
from _pytest.runner import runtestprotocol
from selenium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
@pytest.fixture
@pytest.mark.skip("Sauce Credentials null")
def driver(request):
    # Enter your Sauce Labs Username here
    sauce_username = "SAUCE_USERNAME"
    # Enter your Sauce Labs Access Key here
    sauce_access_key = "SAUCE_ACCESS_KEY"
    remote_url = "https://ondemand.saucelabs.com:443/wd/hub"
    desired_cap = {
        'platform': 'Mac OS X 10.13',
        'browserName': 'safari',
        'version': '11.1',
        'build': 'Onboarding Sample App - Python-pytest',
        'name': '2-user-site',
        'username': sauce_username,
        'accessKey': sauce_access_key
    }
    if sauce_access_key == "SAUCE_ACCESS_KEY":
        pytest.skip("please enter your access key to complete this test")
    if sauce_username == "SAUCE_USERNAME":
        pytest.skip("please enter your sauce access key to run this test")
    browser = webdriver.Remote(remote_url, desired_cap)
    yield browser
    browser.quit()


def test_should_open_safari(driver):
    driver.get("http://www.saucedemo.com")
    actual_title = driver.title
    expected_title = "Swag Labs"
    assert expected_title == actual_title