# Selenium 3.14+ doesn't enable certificate checking
import unittest
import os
from selenium import webdriver


# This is the only code you need to edit in this script.
# Enter in your Sauce Labs Credentials in order to run this test
sauce_username = "SAUCE_USERNAME"
sauce_access_key = "SAUCE_ACCESS_KEY"
# This variable contains the service address for the Sauce Labs VM hub
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"

class Module1Test(unittest.TestCase):

    def setUp(self):
        # the desired_capabilities parameter tells us which browsers and OS to spin up.
        desired_cap = {
            'platform': 'Mac OS X 10.13',
            'browserName': 'safari',
            'version': "11.1",
            'build': 'Onboarding Sample App - Python + UnitTest',
            'name': '1-first-test',
            'username': sauce_username,
            'accessKey': sauce_access_key
        }

        # This creates a webdriver object to send to Sauce Labs including the desired capabilities
        self.driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)

    # Here is our actual test code. In this test we open the saucedemo app in chrome
    # and assert that the title is correct.
    @unittest.skip("You need to input Sauce Credentials")
    def test_should_open_chrome(self):
        self.driver.get("https://www.saucedemo.com")
        assert ("Swag Labs" in self.driver.title)

    # Here we send the results to Sauce Labs and tear down our driver session
    def tearDown(self):
        if self.driver.title == 'Swag Labs':
            # we use the JavaScript Executor to send results to Sauce Labs Service Hub
            self.driver.execute_script('sauce:job-result=passed')
        else:
            self.driver.execute_script('sauce:job-result=failed')
        # This is where you tell Sauce Labs to stop running tests on your behalf.
        # It's important so that you aren't billed after your test finishes.
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
