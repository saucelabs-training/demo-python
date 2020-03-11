import pytest
import os
import requests
import json
import re

from appium import webdriver


def pytest_addoption(parser):
    parser.addoption("--dc", action="store", default='us', help="Set Sauce Labs Data Center (US or EU)")


@pytest.fixture
def data_center(request):
    return request.config.getoption('--dc')


@pytest.fixture
def ios_driver(request, data_center):
    
    caps = {
        'platformName':     'iOS',
        'platformVersion':  '12.1.4',
        'deviceOrientation':'portrait',
        'privateDevicesOnly': False 
    }

    rdc_key = os.environ['TESTOBJECT_SAMPLE_IOS']
    caps['testobject_api_key'] = rdc_key
    test_name = request.node.name
    caps['name'] = test_name

    if data_center and data_center.lower() == 'eu':
        sauce_url = "https://appium.testobject.com/wd/hub"
    else:   
        sauce_url = "https://us1.appium.testobject.com/wd/hub"

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
def android_driver(request, data_center):
    
    caps = {
        'deviceName': 'Google.*',
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceOrientation':'portrait',
        'privateDevicesOnly': False 
    }

    rdc_key = os.environ['TESTOBJECT_SAMPLE_ANDROID']
    caps['testobject_api_key'] = rdc_key
    test_name = request.node.name
    caps['name'] = test_name

    if data_center and data_center.lower() == 'eu':
        sauce_url = "https://appium.testobject.com/wd/hub"
    else:   
        sauce_url = "https://us1.appium.testobject.com/wd/hub"

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
