import pytest
import os
from selenium import webdriver

# skipping the first file
collect_ignore = ["test_module1_pytest.py"]

# Here we use a test runner method to handle all postrequisite test execution steps such as:
# sending the test results to saucelabs.com and tearing down the current WebDriver (browser) session
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    driver = item.funcargs.get('driver')

    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call":
        driver.execute_script('sauce:job-result={}'.format(rep.outcome))
