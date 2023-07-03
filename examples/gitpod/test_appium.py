import os
import json
import time

from selenium import webdriver

class TestSelenium(object):

    def test_appium_with_gitpod(self):
        test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        gitpod_workspace_id = os.environ.get('GITPOD_WORKSPACE_ID', None)
        region = os.environ.get('REGION', 'us-west-1')
        app = os.environ.get('APP_NAME', None)
        if app:
            app = "storage:filename=" + app
        else:
            app = None
        if gitpod_workspace_id:
            tags = ['gitpod']
        else:
            tags = []
        capabilities = {
            'browserName': os.environ.get('BROWSER_NAME', None),
            'platformName': os.environ.get('PLATFORM_NAME', 'Android'),
            'appium:app': app,
            'appium:deviceName': os.environ.get('DEVICE_NAME', 'Google.*'),
            'appium:platformVersion': os.environ.get('PLATFORM_VERSION', ''),
            'appium:automationName': os.environ.get('AUTOMATION_NAME', 'uiautomator2'),
            'sauce:options': {
                'username': os.environ["SAUCE_USERNAME"],
                'accesskey': os.environ["SAUCE_ACCESS_KEY"],
                'build': os.environ.get('BUILD', None),
                'name': os.environ.get('JOB_NAME', test_name),
                'tags': tags,
            }
        }
        sauce_url = f'https://ondemand.{region}.saucelabs.com:443/wd/hub'
        driver = webdriver.Remote(sauce_url, capabilities)

        # Replace this with commands and assertions
        if os.environ.get('BROWSER_NAME', None):
            driver.get('https://www.saucedemo.com/')
        time.sleep(5)

        # Report pass/fail to Sauce Labs
        # sauce_result = "failed"
        sauce_result = "passed"
        driver.execute_script("sauce:job-result={}".format(sauce_result))

        driver.quit()
