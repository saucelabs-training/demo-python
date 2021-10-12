from selenium.webdriver.edge.options import Options as EdgeOptions


def test_new_window(driver):
    driver.switch_to.new_window('window')
    driver.set_window_position(100, 400)

    assert len(driver.window_handles) == 2


def test_new_tab(driver):
    driver.switch_to.new_window('tab')

    assert len(driver.window_handles) == 2