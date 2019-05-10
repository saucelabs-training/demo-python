# Selenium 3.14+ doesn't enable certificate checking
import pytest
import os
from _pytest.runner import runtestprotocol
from selenium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

@pytest.fixture
@pytest.mark.onboarding
def driver(request):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
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
    browser = webdriver.Remote(remote_url, desired_cap)
    yield browser
    browser.quit()

def test_should_open_safari(driver):
    # Substitute your website URL here
    driver.get("http://www.saucedemo.com")
    actual_title = driver.title
    # Substitute "Swag Labs" for the title of your website. To see the title use dev tools or use:
    # print(driver.title)
    expected_title = "Swag Labs"
    assert expected_title == actual_title