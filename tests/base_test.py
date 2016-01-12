import os
import unittest
import sys
import new
from appium import webdriver
from sauceclient import SauceClient

devices = [{
    'deviceName':       'iPhone 5',
    'appiumVersion':    '1.4.16',
    'browserName':      '',
    'platformName':     'iOS',
    'platformVersion':  '9.0',
    'deviceOrientation':'portrait',
    },{
    'deviceName':       'iPhone 6',
    'appiumVersion':    '1.4.16',
    'browserName':      '',
    'platformName':     'iOS',
    'platformVersion':  '9.1',
    'deviceOrientation':'portrait',
}]


# This decorator is required to iterate over browsers
def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)

    return decorator


class BaseTest(unittest.TestCase):
    app_path = None
    app = None
    username = None
    access_key = None
    selenium_port = None
    selenium_host = None
    upload = True
    tunnel_id = None
    build_tag = None

    # setUp runs before each test case
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.desired_capabilities['app'] = BaseTest.app

        if BaseTest.tunnel_id:
            self.desired_capabilities['tunnel-identifier'] = BaseTest.tunnel_id
        if BaseTest.build_tag:
            self.desired_capabilities['build'] = BaseTest.build_tag

        self.driver = webdriver.Remote(
                command_executor="http://%s:%s@%s:%s/wd/hub" %
                                 (BaseTest.username,
                                  BaseTest.access_key,
                                  BaseTest.selenium_host,
                                  BaseTest.selenium_port),
                desired_capabilities=self.desired_capabilities)

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()
        sauce_client = SauceClient(BaseTest.username, BaseTest.access_key)
        status = (sys.exc_info() == (None, None, None))
        sauce_client.jobs.update_job(self.driver.session_id, passed=status)
        test_name = "%s_%s" % (type(self).__name__, self.__name__)
        with(open(test_name + '.testlog', 'w')) as outfile:
            outfile.write("SauceOnDemandSessionID=%s job-name=%s\n" % (self.driver.session_id, test_name))

    @classmethod
    def setup_class(cls):
        cls.build_tag = os.environ.get('BUILD_TAG', None)
        cls.tunnel_id = os.environ.get('TUNNEL_IDENTIFIER', None)
        cls.username = os.environ.get('SAUCE_USERNAME', None)
        cls.access_key = os.environ.get('SAUCE_ACCESS_KEY', None)
        cls.app_path = os.environ.get("APP", None)
        if cls.app_path:
            if cls.app_path and (cls.app_path.startswith('http://') or cls.app_path.startswith('http://')):
                cls.app = cls.app_path
                cls.upload = False
            else:
                cls.app = "sauce-storage:%s" % (os.path.basename(cls.app_path))
                cls.upload = True
        else:
            cls.app = "sauce-storage:TestApp8.4.app.zip"
            cls.app_path = os.path.realpath(__file__ + "/../../resources/TestApp8.4.app.zip")
            cls.upload = True

        cls.selenium_port = os.environ.get("SELENIUM_PORT", None)
        if cls.selenium_port:
            cls.selenium_host = "localhost"
        else:
            cls.selenium_host = "ondemand.saucelabs.com"
            cls.selenium_port = "80"
