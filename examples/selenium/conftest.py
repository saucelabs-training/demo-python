import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions

import pytest

import urllib3

urllib3.disable_warnings()

browsers = [
    'internet explorer',
    'chrome',
    'firefox',
]

def browser_options(browsers):
    if browsers == 'chrome':
        return ChromeOptions()
    elif browsers == 'firefox':
        return FirefoxOptions()
    elif browsers == 'internet explorer':
        return IEOptions()

@pytest.fixture(params=browsers)
def driver(request):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]

    options = browser_options(request.param)
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'

    sauce_options = {'username': sauce_username,
                     'accessKey': sauce_access_key,
                     'name': request.node.name}

    options.set_capability('sauce:options', sauce_options)
    sauce_url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

    driver = webdriver.Remote(command_executor=sauce_url,
                               options=options)

    yield driver

    sauce_result = "failed" if request.session.testsfailed == 1 else "passed"
    if driver is not None:
        driver.execute_script("sauce:job-result={}".format(sauce_result))
        driver.quit()
