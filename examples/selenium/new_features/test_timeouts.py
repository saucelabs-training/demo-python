from selenium.webdriver.common.timeouts import Timeouts
from selenium.webdriver.edge.options import Options as EdgeOptions


def test_getting_timeouts(driver):
    timeouts = Timeouts()
    timeouts.implicit_wait = 1
    driver.timeouts = timeouts

    assert driver.timeouts.implicit_wait == 1
    assert driver.timeouts.page_load == 300
    assert driver.timeouts.script == 30
