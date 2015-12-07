import os
import unittest
import sys
import new
from appium import webdriver
from sauceclient import SauceClient

devices = [{
    'deviceName':       'iPhone 5',
    'appiumVersion':    '1.4.11',
    'browserName':      '',
    'platformName':     'iOS',
    'platformVersion':  '8.4',
    'deviceOrientation':'portrait',
    'app':              'https://s3.amazonaws.com/appium/TestApp8.4.app.zip'
},{
    'deviceName':       'iPhone 6',
    'appiumVersion':    '1.4.11',
    'browserName':      '',
    'platformName':     'iOS',
    'platformVersion':  '8.4',
    'deviceOrientation':'portrait',
    'app':              'https://s3.amazonaws.com/appium/TestApp8.4.app.zip'
}]

username = os.environ['SAUCE_USERNAME']
access_key = os.environ['SAUCE_ACCESS_KEY']

# This decorator is required to iterate over devices
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator

@on_platforms(devices)
class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.driver = webdriver.Remote(
           command_executor="http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (username, access_key),
           desired_capabilities=self.desired_capabilities)

    # click to make a new note in the app
    def test_sum1(self):
        # populate text fields with values
        field_one = self.driver.find_element_by_accessibility_id("TextField1")
        field_one.send_keys("12")

        field_two = self.driver.find_elements_by_class_name("UIATextField")[1]
        field_two.send_keys("8")

        # trigger computation by using the button
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click();

        # is sum equal?
        sum = self.driver.find_element_by_class_name("UIAStaticText").text;
        assert int(sum) == 20, "ERROR MESSAGE"

    def test_sum2(self):
        # populate text fields with values
        field_one = self.driver.find_element_by_accessibility_id("TextField1")
        field_one.send_keys("12")

        field_two = self.driver.find_elements_by_class_name("UIATextField")[1]
        field_two.send_keys("8")

        # trigger computation by using the button
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click();

        # is sum equal?
        sum = self.driver.find_element_by_class_name("UIAStaticText").text;
        assert int(sum) == 20, "ERROR MESSAGE"

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()
        sauce_client = SauceClient(username, access_key)
        status = (sys.exc_info() == (None, None, None))
        sauce_client.jobs.update_job(self.driver.session_id, passed=status)
