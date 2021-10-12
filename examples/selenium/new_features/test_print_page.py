from base64 import b64decode

from selenium.webdriver.common.timeouts import Timeouts
from selenium.webdriver.edge.options import Options as EdgeOptions


def test_getting_timeouts(headless_driver):
    headless_driver.get("https://www.saucedemo.com/v1/inventory.html")

    pdf = b64decode(headless_driver.print_page())

    with open("../resources/python_print_page.pdf", 'wb') as f:
        f.write(pdf)
