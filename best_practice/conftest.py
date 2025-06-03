import pytest
from os import environ

from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
from appium.options.ios import XCUITestOptions
from selenium import webdriver
from appium import webdriver as appiumdriver
from selenium.common.exceptions import WebDriverException

import urllib3

urllib3.disable_warnings()

emusim_browsers = [
    {
        "deviceName": "iPhone X Simulator",
        "browserName": "Safari",
        "deviceOrientation": "portrait",
        "platformVersion": "13.4",
        "platformName": "iOS"
    }, {
        "deviceName": "iPhone 11 Simulator",
        "browserName": "Safari",
        "deviceOrientation": "portrait",
        "platformVersion": "13.4",
        "platformName": "iOS"
    }, {
        "deviceName": "Google Pixel 3 XL GoogleAPI Emulator",
        "browserName": "Chrome",
        "deviceOrientation": "portrait",
        "platformVersion": "10.0",
        "platformName": "Android"
    },{
        "deviceName": "Samsung Galaxy S9 WQHD GoogleAPI Emulator",
        "browserName": "Chrome",
        "deviceOrientation": "portrait",
        "platformVersion": "9.0",
        "platformName": "Android"
    }]


desktop_browsers = [
    {
        "platformName": "Windows 10",
        "browserName": "MicrosoftEdge",
        "platformVersion": "latest",
        "sauce:options": {}
    }, {
        "platformName": "Windows 10",
        "browserName": "firefox",
        "platformVersion": "latest-1",
        "sauce:options": {}
    }, {
        "platformName": "Windows 10",
        "browserName": "internet explorer",
        "platformVersion": "latest",
        "sauce:options": {}
    }, {
        "platformName": "OS X 10.14",
        "browserName": "safari",
        "platformVersion": "latest-1",
        "sauce:options": {}
    }, {
        "platformName": "OS X 10.14",
        "browserName": "chrome",
        "platformVersion": "latest",
        "sauce:options": {
            "extendedDebugging": True
        }
    }]


def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


@pytest.fixture(params=emusim_browsers)
def mobile_web_driver(request, data_center):

    test_name = request.node.name
    build_tag = environ.get('BUILD_TAG', "Sauce-Best-Practices-Python-Mobile-Web")
   
    username = environ['SAUCE_USERNAME']
    access_key = environ['SAUCE_ACCESS_KEY']
        
    if data_center and data_center.lower() == 'eu':
        selenium_endpoint = "https://@ondemand.eu-central-1.saucelabs.com/wd/hub"
    else:
        selenium_endpoint = "https://@ondemand.us-west-1.saucelabs.com/wd/hub"

    sauce_options = {
        'username': username,
        'accessKey': access_key,
        'build': build_tag,
        'name': test_name,
    }
    options = AppiumOptions()
    options.set_capability('sauce:options', sauce_options)
    options.platform_name = request.param['platformName']
    options.browser_name = request.param['browserName']
    options.platform_version = request.param['platformVersion']
    options.device_name = request.param['deviceName']
    options.device_orientation = request.param['deviceOrientation']

    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=options,
        keep_alive=True
    )

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    if browser is not None:
        print("SauceOnDemandSessionID={} job-name={}".format(browser.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield browser

    # Teardown starts here
    # report results
    # use the test result to send the pass/fail status to Sauce Labs
    sauce_result = "failed" if request.node.rep_call.failed else "passed"
    browser.execute_script("sauce:job-result={}".format(sauce_result))
    browser.quit()

@pytest.fixture(params=desktop_browsers)
def desktop_web_driver(request, data_center):

    test_name = request.node.name
    build_tag = environ.get('BUILD_TAG', "Sauce-Best-Practices-Python-Desktop-Web")
    
    username = environ['SAUCE_USERNAME']
    access_key = environ['SAUCE_ACCESS_KEY']
    
    if data_center and data_center.lower() == 'eu':
        selenium_endpoint = "https://{}:{}@ondemand.eu-central-1.saucelabs.com/wd/hub".format(username, access_key)
    else:
        selenium_endpoint = "https://{}:{}@ondemand.us-west-1.saucelabs.com/wd/hub".format(username, access_key)

    caps = dict()
    caps.update(request.param)
    caps['sauce:options'].update({'build': build_tag})
    caps['sauce:options'].update({'name': test_name})

    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        options=webdriver.ChromeOptions(),
        keep_alive=True
    )

    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    if browser is not None:
        print("SauceOnDemandSessionID={} job-name={}".format(browser.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield browser

    # Teardown starts here
    # report results
    # use the test result to send the pass/fail status to Sauce Labs
    sauce_result = "failed" if request.node.rep_call.failed else "passed"
    browser.execute_script("sauce:job-result={}".format(sauce_result))
    browser.quit()

@pytest.fixture
def rdc_browser(request, data_center):

    username = environ['SAUCE_USERNAME']
    access_key = environ['SAUCE_ACCESS_KEY']

    sauce_options = {
        'username': username,
        'accessKey': access_key,
        'build': 'RDC-Android-Web-Python-Best-Practice',
        'name': request.node.name,
    }
    options = XCUITestOptions()
    options.set_capability('sauce:options', sauce_options)
    options.platform_name = 'iOS'
    options.browser_name = 'Safari'
    options.device_name = 'iPhone.*'

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

