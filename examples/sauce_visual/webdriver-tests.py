import os
from selenium import webdriver


def test_screener_snapshot():
    capabilities = {
      'browserName': 'chrome',
      'browserVersion': '80.0',
      'sauce:options': {
        'username': os.environ["SAUCE_USERNAME"],
        'accesskey': os.environ["SAUCE_ACCESS_KEY"],
      },
      'sauce:visual': {
        'apiKey': os.environ["SCREENER_API_KEY"],
        'projectName': 'org/my-project',
        'viewportSize': '1280x1024',
      }
    }

    command_executor = 'https://hub.screener.io/wd/hub'
    
    driver = webdriver.Remote(command_executor, capabilities)
    driver.get('https://screener.io')
    driver.execute_script('/*@visual.init*/', 'My Visual Test')
    driver.execute_script('/*@visual.snapshot*/', 'Home')
    result = driver.execute_script('/*@visual.end*/')
    
    assert result['passed'] is True
