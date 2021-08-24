import os

from selenium import webdriver
from sa11y.analyze import Analyze

import urllib3

urllib3.disable_warnings()


class TestAccessibilitySa11y(object):

    def test_analysis(self):
        try:
            username = os.environ['SAUCE_USERNAME']
        except KeyError:
            raise KeyError('No SAUCE_USERNAME environment variable found. Please set one.')

        try:
            access_key = os.environ['SAUCE_ACCESS_KEY']
        except KeyError:
            raise KeyError('No SAUCE_ACCESS_KEY environment variable found. Please set one.')


        capabilities = {
            'browserName': 'chrome',
            'sauce:options': {
                'username': username,
                'accesskey': access_key
            }
        }
        sauce_url = 'https://ondemand.us-west-1.saucelabs.com/wd/hub'
        driver = webdriver.Remote(sauce_url, capabilities)

        driver.get('https://www.saucedemo.com/')

        Analyze(driver).results()

        driver.quit()
