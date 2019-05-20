# Selenium 3.14+ doesn't enable certificate checking
import pytest
from selenium import webdriver
from _pytest.runner import runtestprotocol
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# @pytest-examples.fixture
@pytest.mark.skip(reason="Update Sauce Creds")
def driver(request):
    sauce_username = "SAUCE_USERNAME"
    sauce_access_key = "SAUCE_ACCESS_KEY"
    remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

    # the desired_capabilities parameter tells us which browsers and OS to spin up.
    desired_cap = {
        'platform': 'Mac OS X 10.13',
        'browserName': 'safari',
        'version': "11.1",
        'build': 'Onboarding Sample App - Python + Pytest',
        'name': '1-first-test',
        'username': sauce_username,
        'accessKey': sauce_access_key,

        # This setting is for using Sauce Connect Proxy tunnel
        # Typically you use this setting if you need to run your tests from behind a secure network firewall
        'tunnelIdentifier': 'demo-python-tunnel'
    }

    # This creates a webdriver object to send to Sauce Labs including the desired capabilities
    browser = webdriver.Remote(remote_url, desired_capabilities=desired_cap)
    yield browser
    # This is where you tell Sauce Labs to stop running tests on your behalf.
    # It's important so that you aren't billed after your test finishes.
    browser.quit()

# Here is our actual test code. In this test we open the saucedemo app in chrome and assert that the title is correct.
@pytest.mark.skip(reason="Update Sauce Creds")
def test_should_open_chrome(driver):
    driver.get("http://www.saucedemo.com")
    actual_title = driver.title
    expected_title = "Swag Labs"
    assert expected_title == actual_title