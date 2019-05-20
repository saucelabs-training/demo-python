# Selenium 3.14+ doesn't enable certificate checking
import unittest
import os
from selenium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sauce_username = os.environ["SAUCE_USERNAME"]
sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"


class Module2Test(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'platform': 'Mac OS X 10.13',
            'browserName': 'safari',
            'version': "11.1",
            'build': 'Onboarding Sample App - Python + UnitTest',
            'name': '2-user-test',
            'username': sauce_username,
            'accessKey': sauce_access_key,

            # This setting is for using Sauce Connect Proxy tunnel
            # Typically you use this setting if you need to run your tests from behind a secure network firewall
            'tunnelIdentifier': 'demo-python-tunnel'
        }
        self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)

    def test_should_open_chrome(self):
        # Substitute 'http://www.saucedemo.com' for your own application URL
        self.driver.get("http://www.saucedemo.com")
        assert ("Swag Labs" in self.driver.title)

    def tearDown(self):
        if self.driver.title == 'Swag Labs':
            self.driver.execute_script('sauce:job-result=passed')
        else:
            self.driver.execute_script('sauce:job-result=failed')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()