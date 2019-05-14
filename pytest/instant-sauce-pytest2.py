# Selenium 3.14+ doesn't enable certificate checking
import os
from selenium import webdriver
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# This is the only code you need to edit in your existing scripts.
# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.13",
    'browserName': "safari",
    'version': "11.1",
    'build': "Onboarding Sample App - Python",
    'name': "2-user-site",
}
username = os.environ["SAUCE_USERNAME"]
access_key = os.environ["SAUCE_ACCESS_KEY"]
driver = webdriver.Remote(
   command_executor='http://{}:{}@ondemand.saucelabs.com/wd/hub'.format(username, access_key),
   desired_capabilities=desired_cap)

# Substitute 'http://www.saucedemo.com for your own application
driver.get("http://www.saucedemo.com")
if "Swag Labs" not in driver.title:
    raise Exception("Unable to load saucedemo page!")
driver.quit()
