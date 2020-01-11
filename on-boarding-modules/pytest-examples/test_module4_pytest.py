import pytest
import os
from selenium import webdriver
from _pytest.runner import runtestprotocol

@pytest.fixture
def driver(request):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

    sauceOptions = {
        'screenResolution': '1280x768',
        'seleniumVersion': '3.141.59',
        # best practices involve setting a build number for version control
        'build': 'Onboarding Sample App - Python + Pytest',
        'name': '4-best-practices',
        'username': sauce_username,
        'accessKey': sauce_access_key,
        # tags to filter test reporting.
        'tags': ['instant-sauce', 'pytest', 'module4'],
        # setting sauce-runner specific parameters such as timeouts helps
        # manage test execution speed.
        'maxDuration': 1800,
        'commandTimeout': 300,
        'idleTimeout': 1000,
    }

    chromeOpts = {
        'platformName': 'Windows 10',
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'goog:chromeOptions': {'w3c': True},
        'sauce:options': sauceOptions
    }

    browser = webdriver.Remote(command_executor=remote_url, desired_capabilities=chromeOpts)
    yield browser
    browser.quit()


def test_should_open_chrome(driver):
    driver.get("https://www.saucedemo.com")
    actual_title = driver.title
    expected_title = "Swag Labs"
    assert expected_title == actual_title
