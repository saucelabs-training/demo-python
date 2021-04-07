import pytest
import os
import json
import re

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')

@pytest.fixture
def ios_to_driver(request, data_center):
    
    caps = {
        'platformName':     'iOS',
        'deviceOrientation':'portrait',
        'privateDevicesOnly': False, 
        'phoneOnly': True
    }

    rdc_key = os.environ['TESTOBJECT_SAMPLE_IOS']
    caps['testobject_api_key'] = rdc_key
    test_name = request.node.name
    caps['name'] = test_name

    if data_center and data_center.lower() == 'eu':
        sauce_url = "http://appium.testobject.com/wd/hub"
    else:   
        sauce_url = "http://us1.appium.testobject.com/wd/hub"

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)
    
    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    # creates one file per test non ideal but xdist is awful
    if driver:
        print("SauceOnDemandSessionID={} job-name={}\n".format(driver.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield driver
    driver.quit()


@pytest.fixture
def android_to_driver(request, data_center):
    
    caps = {
        'deviceName': 'Google.*',
        'platformName': 'Android',
        'deviceOrientation':'portrait',
        'privateDevicesOnly': False 
    }

    rdc_key = os.environ['TESTOBJECT_SAMPLE_ANDROID']
    caps['testobject_api_key'] = rdc_key
    test_name = request.node.name
    caps['name'] = test_name

    if data_center and data_center().lower() == 'eu':
        sauce_url = "http://appium.testobject.com/wd/hub"
    else:   
        sauce_url = "http://us1.appium.testobject.com/wd/hub"

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)
    
    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    # creates one file per test non ideal but xdist is awful
    if driver:
        print("SauceOnDemandSessionID={} job-name={}\n".format(driver.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield driver
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