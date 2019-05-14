# In the following examples we implement the pytest and seleniumbase test frameworks
# pytest docs: https://docs.pytest.org/en/latest/contents.html
# seleniumbase docs: https://github.com/seleniumbase/SeleniumBase
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
    # use sauce:options to handle all saucelabs.com-specific capabilities such as:
    # username, accesskey, build number, test name, timeouts etc.
    sauceOptions = {
        'screenResolution': '1280x768',
        'seleniumVersion': '3.141.59',
        'build': 'Onboarding Sample App - Python-pytest',
        'name': '3-cross-browser',
        # remove line below if not using Sauce Connect
        'tunnelIdentifier': 'demo-python-tunnel',
        'username': sauce_username,
        'accessKey': sauce_access_key
    }
    # In ChromeOpts, we define browser and/or WebDriver capabilities such as
    # the browser name, browser version, platform name, platform version
    chromeOpts =  {
        'platformName': 'Windows 10',
        'browserName': 'chrome',
        'browserVersion': '71.0',
        'goog:chromeOptions': {'w3c': True},
        'sauce:options': sauceOptions
    }

    browser = webdriver.Remote(remote_url, chromeOpts)
    yield browser
    browser.quit()

# Here is our actual test code. In this test we open the saucedemo app in chrome and assert that the title is correct.
def test_should_open_chrome(driver):
    driver.get("https://www.saucedemo.com")
    actual_title = driver.title
    expected_title = "Swag Labs"
    assert expected_title == actual_title