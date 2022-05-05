import os


def browsers(browserName, browserVersion, platformName):
    sauceOptions = {
        "browserName": browserName,
        "browserVersion": browserVersion,
        "platformName": platformName,
        "username": os.environ['SAUCE_USERNAME'],
        "accessKey": os.environ['SAUCE_ACCESS_KEY'], 
        # "name": "my test name on Sauce Labs
    }
    
    caps = {
        "browserName": browserName,
        "browserVersion": browserVersion,
        "platformName": platformName,
        "sauce:options": sauceOptions
    }

    return caps