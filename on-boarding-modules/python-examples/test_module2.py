# Selenium 3.14+ doesn't enable certificate checking
import os
from selenium import webdriver

sauce_username = os.environ["SAUCE_USERNAME"]
sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
remote_url = "https://ondemand.saucelabs.com/wd/hub"
tunnel_id = os.environ['CI_TUNNEL_ID']

desired_cap = {
    'platform': 'Mac OS X 10.13',
    'browserName': 'safari',
    'version': '11.1',
    'build': 'Onboarding Sample App - Python',
    'name': '2-user-site',
    'username': sauce_username,
    'accessKey': sauce_access_key,
    'accept_untrusted_certs': True,
    # This setting is for using Sauce Connect Proxy tunnel
    # Typically you use this setting if you need to run your tests from behind a secure network firewall
    'tunnelIdentifier': tunnel_id
}
driver = webdriver.Remote(command_executor=remote_url, desired_capabilities=desired_cap)
# Substitute 'http://www.saucedemo.com for your own application
driver.get("https://www.saucedemo.com")

# Once you substitute the SUT Url, you'll need to change the logic below to reflect your site title
if "Swag Labs" not in driver.title:
    driver.execute_script('sauce:job-result=passed')
    raise Exception("Unable to load saucedemo page!")
else:
    driver.execute_script('sauce:job-result=passed')

driver.quit()
