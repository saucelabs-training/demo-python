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
def ios_up_driver(request, data_center):
    caps = {
        'username': os.environ['SAUCE_USERNAME'],
        'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        'deviceName': 'iPhone.*',
        'platformName': 'iOS',
        'name': request.node.name,
        'app': 'storage:filename=iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.3.0.ipa'
    }

    if data_center and data_center.lower() == 'eu':
        sauce_url = "http://ondemand.eu-central-1.saucelabs.com/wd/hub"
    else:   
        sauce_url = "http://ondemand.us-west-1.saucelabs.com/wd/hub"

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)
    yield driver
    driver.quit()


@pytest.fixture
def ios_simulator(request, data_center):
    caps = {
        'username': os.environ['SAUCE_USERNAME'],
        'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        'deviceName': 'iPhone XS Simulator',
        'appiumVersion': '1.17.1',
        'platformName': 'iOS',
        'platformVersion': "13.4",
        'deviceOrientation': "portrait",
        'name': request.node.name,
        'app': 'storage:filename=iOS.Simulator.SauceLabs.Mobile.Sample.app.2.7.0.zip'
    }

    if data_center and data_center.lower() == 'eu':
        sauce_url = "http://ondemand.eu-central-1.saucelabs.com/wd/hub"
    else:   
        sauce_url = "http://ondemand.us-west-1.saucelabs.com/wd/hub"

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)
    yield driver
    driver.quit()


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


@pytest.fixture
def android_up_driver(request, data_center):
    caps = {
        'username': os.environ['SAUCE_USERNAME'],
        'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        'deviceName': 'Google.*',
        'platformName': 'Android',
        'name': request.node.name,
        'app': 'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.3.0.apk'
    }

    if data_center and data_center.lower() == 'eu':
        sauce_url = 'http://ondemand.eu-central-1.saucelabs.com/wd/hub'
    else:
        sauce_url = 'http://ondemand.us-west-1.saucelabs.com/wd/hub'

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)
    yield driver
    driver.quit()


@pytest.fixture
def android_emusim(request, data_center):
    caps = {
        'username': os.environ['SAUCE_USERNAME'],
        'accessKey': os.environ['SAUCE_ACCESS_KEY'],
        'deviceName': 'Android GoogleAPI Emulator',
        'platformName': 'Android',
        'platformVersion': '10.0',
        'deviceOrientation': 'portrait',
        'name': request.node.name,
        'appiumVersion': '1.17.1',
        'appWaitActivity': 'com.swaglabsmobileapp.MainActivity',
        'app': 'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.3.0.apk'

    }

    if data_center and data_center.lower() == 'eu':
        sauce_url = 'http://ondemand.eu-central-1.saucelabs.com/wd/hub'
    else:
        sauce_url = 'http://ondemand.us-west-1.saucelabs.com/wd/hub'

    driver = webdriver.Remote(sauce_url, desired_capabilities=caps)
    yield driver
    driver.quit()