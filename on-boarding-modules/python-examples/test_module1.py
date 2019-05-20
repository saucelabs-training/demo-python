# Selenium 3.14+ doesn't enable certificate checking
import os
from selenium import webdriver

# This is the only code you need to edit in this script.
# Enter in your Sauce Labs Credentials in order to run this test
sauce_username = "SAUCE_USERNAME"
sauce_access_key = "SAUCE_ACCESS_KEY"
# This variable contains the service address for the Sauce Labs VM hub
remote_url = "https://ondemand.saucelabs.com:443/wd/hub"
tunnel_id = os.environ['CI_TUNNEL_ID']
# The desired_capabilities parameter includes metadata specific to sauce labs
# including: username, accessKey, browserName, platform etc.
# parameter tells us which browsers and OS to spin up.

desired_cap = {
    'platform': 'Mac OS X 10.13',
    'browserName': 'safari',
    'version': '11.1',
    'build': 'Onboarding Sample App - Python',
    'name': '1-first-test',
    'username': sauce_username,
    'accessKey': sauce_access_key,
    # This setting is for using Sauce Connect Proxy tunnel
    # Typically you use this setting if you need to run your tests from behind a secure network firewall
    'tunnelIdentifier': tunnel_id
}

# This creates a webdriver object to send to Sauce Labs including the desired capabilities
driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)
# This command points to the SUT (site under test)
driver.get("https://www.saucedemo.com")
# This if/else statement determines whether or not the page title is correct.
# The driver.execute_script Selenium command executes JavaScript POST commands to Sauce Labs
# In this case we're updating the Sauce Labs Job status based on test pass/fail

if "Swag Labs" not in driver.title:
    driver.execute_script('sauce:job-result=passed')
    raise Exception("Unable to load saucedemo page!")
else:
    driver.execute_script('sauce:job-result=passed')
# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()
