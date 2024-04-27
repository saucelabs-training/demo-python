import pytest
from selenium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from views.base_view import BaseView


class HomeView(BaseView):
    USERNAME_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'test-Username')
    PASSWORD_FIELD = (AppiumBy.ACCESSIBILITY_ID, 'test-Password')
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'test-LOGIN')
    DISPLAY_PRODUCTS = (AppiumBy.ACCESSIBILITY_ID, 'test-PRODUCTS')

    def sign_in(self):
        self.wait_for(self.USERNAME_FIELD).send_keys('standard_user')
        self.wait_for(self.PASSWORD_FIELD).send_keys('secret_sauce')
        self.wait_for(self.LOGIN_BUTTON).click()
        try:
            if self.wait_for(self.DISPLAY_PRODUCTS).is_displayed():
                status = "passed"
            else:
                status = "failed"
        except Exception as e:
            print(f"Error finding DISPLAY_PRODUCTS element: {e}")
            status = "failed"
        self.driver.execute_script("sauce:job-result={}".format(status))

        assert self.wait_for(self.DISPLAY_PRODUCTS).is_displayed()
