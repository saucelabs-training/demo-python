import pytest
import os
import requests
import json

from appium import webdriver


def update_job(session_id, result):
    result_json = json.dumps({"passed": result})
    endpoint = 'https://app.testobject.com/api/rest/v2/appium/session/{}/test'.format(session_id)
    requests.put(endpoint, json=result_json)

@pytest.yield_fixture(scope='function')
def driver(request):
    
    SAUCE_USERNAME = os.environ['SAUCE_USERNAME']
    SAUCE_ACCESS_KEY = os.environ['SAUCE_ACCESS_KEY']

    caps = {
        'appiumVersion':    '1.9.1',
        'browserName':      '',
        'platformName':     'iOS',
        'platformVersion':  '12.1.4',
        'deviceOrientation':'portrait',
        'phoneOnly': False,
        'tabletOnly': False,
        'privateDevicesOnly': False 
    }

    caps['app'] = "sauce-storage:SwagLabsMobileApp.ipa"
    caps['build'] = "Appium-Python-iOS-Sample"
    caps['testobject_api_key'] = os.environ['TESTOBJECT_API_KEY']

    sauce_url = "http://us1.appium.testobject.com/wd/hub"

    browser = webdriver.Remote(sauce_url, desired_capabilities=caps)
    
    yield browser
    # Teardown starts here
    # report results
    # use the test result to send the pass/fail status to Sauce Labs
    status = "failed" if request.node.rep_call.failed else "passed"
    # sauce_client = SauceClient(SAUCE_USERNAME, SAUCE_ACCESS_KEY)
    update_job(browser.session_id, status)
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
    return rep
