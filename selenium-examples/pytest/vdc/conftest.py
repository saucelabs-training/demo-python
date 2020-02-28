import pytest
from os import environ

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.remote_connection import RemoteConnection

import urllib3
urllib3.disable_warnings()

browsers = [
    {
        "platform": "Windows 10",
        "browserName": "MicrosoftEdge",
        "version": "latest",
        "sauce:options": {}
    }, {
        "platform": "Windows 10",
        "browserName": "firefox",
        "version": "latest-1",
        "sauce:options": {}
    }, {
        "platform": "Windows 10",
        "browserName": "internet explorer",
        "version": "latest",
        "sauce:options": {}
    }, {
        "platform": "OS X 10.13",
        "browserName": "safari",
        "version": "latest-1",
        "sauce:options": {}
    }, {
        "platform": "OS X 10.14",
        "browserName": "chrome",
        "version": "latest",
        "sauce:options": {
            "extendedDebugging": True
        }
    }]


@pytest.fixture(params=browsers)
def driver(request):

    test_name = request.node.name
    build_tag = environ.get('BUILD_TAG', "Python-Pytest-Selenium-VDC")
    username = environ.get('SAUCE_USERNAME', None)
    access_key = environ.get('SAUCE_ACCESS_KEY', None)

    selenium_endpoint = "https://{}:{}@ondemand.saucelabs.com:443/wd/hub".format(username, access_key)

    caps = dict()
    caps.update(request.param)
    caps['sauce:options'].update({'build': build_tag})
    caps['sauce:options'].update({'name': test_name})

    browser = webdriver.Remote(
        command_executor=selenium_endpoint,
        desired_capabilities=caps, 
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


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # this sets the result as a test attribute for Sauce Labs reporting.
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set an report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)

