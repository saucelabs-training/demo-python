import pytest
import os
from appium import webdriver
from appium.options.common import AppiumOptions

from views.home_view import HomeView

IOS_APP = 'storage:filename=iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.7.1.ipa'
ANDROID_APP = 'storage:filename=Android.SauceLabs.Mobile.Sample.app.2.7.1.apk'
APPIUM = 'https://ondemand.us-west-1.saucelabs.com:443/wd/hub'


def create_ios_caps():
    IOS_CAPS = {}
    IOS_CAPS['platformName'] = 'iOS'
    IOS_CAPS['appium:deviceName'] = 'iPhone.*'
    IOS_CAPS['appium:automationName'] = 'XCUITest'
    IOS_CAPS['appium:app'] = IOS_APP
    IOS_CAPS['sauce:options'] = {}
    IOS_CAPS['sauce:options']['appiumVersion'] = 'latest'
    IOS_CAPS['sauce:options']['username'] = os.environ.get("SAUCE_USERNAME")
    IOS_CAPS['sauce:options']['accessKey'] = os.environ.get("SAUCE_ACCESS_KEY")
    IOS_CAPS['sauce:options']['build'] = 'SwagLabs pytest'
    IOS_CAPS['sauce:options']['name'] = 'Sign In - iOS'
    return IOS_CAPS


def create_android_caps():
    ANDROID_CAPS = {}
    ANDROID_CAPS['platformName'] = 'Android'
    ANDROID_CAPS['appium:deviceName'] = 'Google.*'
    ANDROID_CAPS['appium:automationName'] = 'UIAutomator2'
    ANDROID_CAPS['appium:app'] = ANDROID_APP
    ANDROID_CAPS['sauce:options'] = {}
    ANDROID_CAPS['sauce:options']['appiumVersion'] = 'latest'
    ANDROID_CAPS['sauce:options']['username'] = os.environ.get("SAUCE_USERNAME")
    ANDROID_CAPS['sauce:options']['accessKey'] = os.environ.get("SAUCE_ACCESS_KEY")
    ANDROID_CAPS['sauce:options']['build'] = 'SwagLabs pytest'
    ANDROID_CAPS['sauce:options']['name'] = 'Sign In - Android'
    return ANDROID_CAPS


def pytest_addoption(parser):
    parser.addoption('--platform', action='store', default='android')


@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ['ios', 'android']:
        raise ValueError('--platform value must be ios or android')
    return plat


@pytest.fixture
def driver(platform):
    ios_caps = create_ios_caps()
    android_caps = create_android_caps()
    if platform == 'ios':
        caps = ios_caps
    else:
        caps = android_caps
    driver = webdriver.Remote(APPIUM, options=AppiumOptions().load_capabilities(caps))
    driver._platform = platform
    yield driver
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView(driver)
