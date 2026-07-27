import pytest
from os import environ

from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium import webdriver as appiumdriver

import urllib3

urllib3.disable_warnings()


def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


@pytest.fixture
def android_rdc_driver(request, data_center):

    username_cap = environ['SAUCE_USERNAME']
    access_key_cap = environ['SAUCE_ACCESS_KEY']

    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.device_name = 'Google.*'
    options.automation_name = 'UiAutomator2'
    options.app = 'https://github.com/saucelabs/my-demo-app-android/releases/download/2.2.0/mda-2.2.0-25.apk'
    sauce_options = {
        'username': username_cap,
        'accessKey': access_key_cap,
        'build': 'RDC-Android-Python-Best-Practice',
        'name': request.node.name,
        'appiumVersion': 'latest',
    }
    options.set_capability('sauce:options', sauce_options)

    if data_center and data_center.lower() == 'eu':
        sauce_url = 'https://ondemand.eu-central-1.saucelabs.com/wd/hub'
    else:
        sauce_url = 'https://ondemand.us-west-1.saucelabs.com/wd/hub'

    driver = appiumdriver.Remote(sauce_url, options=options)
    yield driver
    sauce_result = "failed" if request.node.rep_call.failed else "passed"
    driver.execute_script("sauce:job-result={}".format(sauce_result))
    driver.quit()


@pytest.fixture
def ios_rdc_driver(request, data_center):

    username_cap = environ['SAUCE_USERNAME']
    access_key_cap = environ['SAUCE_ACCESS_KEY']

    options = XCUITestOptions()
    options.platform_name = 'iOS'
    options.device_name = 'iPhone.*'
    options.app = 'https://github.com/saucelabs/sample-app-mobile/releases/download/2.7.1/iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.7.1.ipa'
    sauce_options = {
        'username': username_cap,
        'accessKey': access_key_cap,
        'build': 'RDC-iOS-Python-Best-Practice',
        'name': request.node.name,
        'appiumVersion': 'latest',
    }
    options.set_capability('sauce:options', sauce_options)

    if data_center and data_center.lower() == 'eu':
        sauce_url = "https://ondemand.eu-central-1.saucelabs.com/wd/hub"
    else:
        sauce_url = "https://ondemand.us-west-1.saucelabs.com/wd/hub"

    driver = appiumdriver.Remote(sauce_url, options=options)
    yield driver
    sauce_result = "failed" if request.node.rep_call.failed else "passed"
    driver.execute_script("sauce:job-result={}".format(sauce_result))
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for Sauce Labs reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
