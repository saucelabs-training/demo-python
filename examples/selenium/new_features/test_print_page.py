from selenium.webdriver.common.print_page_options import PrintOptions


def test_prints_page(driver):
    driver.get("https://www.selenium.dev/")
    print_options = PrintOptions()
    pdf = driver.print_page(print_options)
    assert len(pdf) > 0
