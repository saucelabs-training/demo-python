import pytest
import os
from selenium import webdriver
from _pytest.runner import runtestprotocol
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

@pytest.fixture
@pytest.mark.onboarding
def driver(request):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    remote_url = "https://ondemand.saucelabs.com/wd/hub"

    sauceOptions = {
        'screenResolution': '1280x768',
        'seleniumVersion': '3.141.59',
        'build': 'Onboarding Sample App - Python-pytest',
        'name': '4-best-practices',
        # remove line below if not using Sauce Connect
        'tunnelIdentifier': 'demo-python-tunnel',
        'username': sauce_username,
        'accessKey': sauce_access_key,
        # best practices involve setting a build number for version control
        # tags to filter test reporting.
        'tags': ['instant-sauce', 'pytest', 'module4'],
        # setting sauce-runner specific parameters such as timeouts helps
        # manage test execution speed.
        'maxDuration': 1800,
        'commandTimeout': 300,
        'idleTimeout': 1000
    }

    chromeOpts = {
        'platformName':'Windows 10',
        'browserName': 'chrome',
        'browserVersion': '71.0',
        'goog:chromeOptions': {'w3c': True},
        'sauce:options': sauceOptions
    }

    browser = webdriver.Remote(remote_url, chromeOpts)
    yield browser
    browser.quit()

def test_should_open_chrome(driver):
    driver.get("https://www.saucedemo.com")
    actual_title = driver.title
    expected_title = "Swag Labs"
    assert expected_title == actual_title
