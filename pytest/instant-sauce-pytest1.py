# Selenium 3.14+ doesn't enable certificate checking
from selenium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.13",
    'browserName': "safari",
    'version': "11.1",
    'build': "Onboarding Sample App - Python",
    'name': "1-first-test",
}
username = "SAUCE_USERNAME"
access_key = "SAUCE_ACCESS_KEY"
driver = webdriver.Remote(
   command_executor='https://{}:{}@ondemand.saucelabs.com:443/wd/hub'.format(username, access_key),
   desired_capabilities=desired_cap)

# This is your test logic. You can add multiple tests here.
driver.get("http://www.saucedemo.com")
if "Swag Labs" not in driver.title:
    raise Exception("Unable to load saucedemo page!")
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()