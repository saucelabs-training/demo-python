import os

from selenium import webdriver
from sa11y.analyze import Analyze

import urllib3

urllib3.disable_warnings()


class TestAccessibilityDeque(object):

    def test_analysis(self):
        capabilities = {
            'browserName': 'chrome',
            'sauce:options': {
                'username': os.environ["SAUCE_USERNAME"],
                'accesskey': os.environ["SAUCE_ACCESS_KEY"],
            }
        }
        sauce_url = 'https://ondemand.us-west-1.saucelabs.com/wd/hub'
        driver = webdriver.Remote(sauce_url, capabilities)

        driver.get('https://www.saucedemo.com/')

        Analyze(driver).results()

        driver.quit()
