import pytest
import os
import requests
import json
import re

from appium import webdriver
import testobject

# def update_job(sauce_username, result):
#     result_json = json.dumps({"passed": result})
#     requests.put(
#         'https://app.saucelabs.com/rest/v1/storage/' + sauce_username + '/swaglabs-demo-debug.apk?overwrite=true',
#         headers = { 'Content-Type': 'application/json',},
#         data = '{"passed": true}'
#     )
#     #endpoint = 'https://app.testobject.com/api/rest/appium/v2/session/{}/test/'.format(session_id)
#     #requests.put(endpoint, data=result_json)
from selenium.common.exceptions import WebDriverException


@pytest.yield_fixture(scope='function')
def driver(request, test_name='pytest-appium-android'):
    sauce_username = os.environ["SAUCE_USERNAME"]
    sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
    sauce_url = "https://ondemand.saucelabs.com:443/wd/hub"

    
    caps = {
        'appiumVersion':    '1.9.1',
        'browserName':      '',
        'platformName':     'Android',
        'platformVersion':  '8.1',
        'deviceOrientation':'portrait',
        'username': sauce_username,
        'accessKey': sauce_access_key,
        'phoneOnly': False,
        'tabletOnly': False,
        'privateDevicesOnly': False,
        'app': 'https://github.com/saucelabs-training/demo-python/blob/master/appium-examples/pytest-realdevices/android/resources/Android.SauceLabs.Mobile.Sample.app.2.1.0.apk?raw=true',
        'name': test_name,
        'build': 'Python PyTest Emusim Demo'
    }

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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for Sauce Labs reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
