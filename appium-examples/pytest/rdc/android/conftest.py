import pytest
import os
import requests
import json
import re

from appium import webdriver


@pytest.fixture
def driver(request):
    
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

    sauce_url = "http://us1.appium.testobject.com/wd/hub"

    browser = webdriver.Remote(sauce_url, desired_capabilities=caps)
    
    # This is specifically for SauceLabs plugin.
    # In case test fails after selenium session creation having this here will help track it down.
    # creates one file per test non ideal but xdist is awful
    if browser:
        print("SauceOnDemandSessionID={} job-name={}\n".format(browser.session_id, test_name))
    else:
        raise WebDriverException("Never created!")

    yield browser
    
    browser.quit()
