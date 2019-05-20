# Selenium 3.14+ doesn't enable certificate checking
import unittest
import os
from selenium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

sauce_username = os.environ["SAUCE_USERNAME"]
sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"


class Module4Test(unittest.TestCase):

    def setUp(self):
        sauceOptions = {
            'screenResolution': '1280x768',
            'seleniumVersion': '3.141.59',
            'build': 'Onboarding Sample App - Python + UnitTest',
            'name': '4-best-practices',
            'username': sauce_username,
            'accessKey': sauce_access_key,
            # tags to filter test reporting.
            'tags': ['instant-sauce', 'ruby-rspec', 'module4'],
            # setting sauce-runner specific parameters such as timeouts helps
            # manage test execution speed.
            'maxDuration': 1800,
            'commandTimeout': 300,
            'idleTimeout': 1000,
            # this setting is only if you need to run your tests from behind a secure network firewall
            'tunnelIdentifier': 'demo-python-tunnel'
        }
        # In ChromeOpts, we define browser and/or WebDriver capabilities such as
        # the browser name, browser version, platform name, platform version
        chromeOpts = {
            'platformName': 'Windows 10',
            'browserName': 'chrome',
            'browserVersion': 'latest',
            'goog:chromeOptions': {'w3c': True},
            'sauce:options': sauceOptions
        }
        self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=chromeOpts)

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