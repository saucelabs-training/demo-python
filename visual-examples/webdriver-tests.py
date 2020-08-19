import os
import unittest
from selenium import webdriver

class ChromeTest(unittest.TestCase):
  def setUp(self):
    self.capabilities = {
      'browserName': 'chrome',
      'browserVersion': '80.0',
      'sauce:options': {
        'username': os.environ["SAUCE_USERNAME"],
        'accesskey': os.environ["SAUCE_ACCESS_KEY"],
      },
    }

  def test_screener_snapshot(self):
    command_executor = 'https://hub.screener.io/wd/hub'
    desired_capabilities = self.capabilities
    desired_capabilities['sauce:visual'] = {
      'apiKey': os.environ["SCREENER_API_KEY"],
      'projectName': 'org/my-project',
      'viewportSize': '1280x1024',
    }
    driver = webdriver.Remote(command_executor, desired_capabilities)
    driver.get('https://screener.io')
    driver.execute_script('/*@visual.init*/', 'My Visual Test')
    driver.execute_script('/*@visual.snapshot*/', 'Home')
    result = driver.execute_script('/*@visual.end*/')
    assert result['passed'] is True

if __name__ == "__main__":
  unittest.main()
