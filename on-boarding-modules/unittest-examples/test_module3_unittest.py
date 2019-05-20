# Selenium 3.14+ doesn't enable certificate checking
import unittest
import os
from selenium import webdriver

sauce_username = os.environ["SAUCE_USERNAME"]
sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"
tunnel_id = os.environ['CI_TUNNEL_ID']


class Module3Test(unittest.TestCase):

    def setUp(self):
        sauceOptions = {
            'screenResolution': '1280x768',
            'seleniumVersion': '3.141.59',
            'build': 'Onboarding Sample App - Python + UnitTest',
            'name': '3-cross-browser',
            'username': sauce_username,
            'accessKey': sauce_access_key,
            # this setting is only if you need to run your tests from behind a secure network firewall
            'tunnelIdentifier': tunnel_id
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
        self.driver.get("https://www.saucedemo.com")
        assert ("Swag Labs" in self.driver.title)

    def tearDown(self):
        if self.driver.title == 'Swag Labs':
            self.driver.execute_script('sauce:job-result=passed')
        else:
            self.driver.execute_script('sauce:job-result=failed')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()