from saucebindings.session import SauceSession
from saucebindings.session import SauceOptions


BASE_TEST_URL = 'https://www.saucedemo.com'


class BindingsLibrary(object):

    def __init__(self):
        self.sauce = {}


    def start_session(self, browser_name, test_name):
        opts = SauceOptions(browser_name)
        opts.name = test_name
        self.sauce = SauceSession(options=opts)
        self.sauce.start()


    def open_login_page(self):
        self.sauce.driver.get(BASE_TEST_URL)


    def end_session(self, result):
        if str(result) == 'PASS':
            self.sauce.stop(True)
        else:
            self.sauce.stop(False)

    
    def login_as_standard_user(self):
        self.sauce.driver.find_element_by_id("user-name").send_keys("standard_user")
        self.sauce.driver.find_element_by_id("password").send_keys("secret_sauce")
        self.sauce.driver.find_element_by_css_selector(".btn_action").click()


    def login_as_invalid_user(self):
        self.sauce.driver.find_element_by_id("user-name").send_keys("invalid")
        self.sauce.driver.find_element_by_id("password").send_keys("invalid")
        self.sauce.driver.find_element_by_css_selector(".btn_action").click()

    
    def is_login_error_displayed(self):
        assert self.sauce.driver.find_element_by_css_selector('.error-button').is_displayed()

    
    def is_on_inventory_page(self):
        assert self.sauce.driver.find_element_by_id('shopping_cart_container').is_displayed()
