from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_london(driver):
    driver.get('https://www.diemol.com/selenium-4-demo/relative-locators-demo.html')

    element = driver.find_elements(locate_with(By.TAG_NAME, "li")
                                   .to_left_of({By.ID: "berlin"})
                                   .below({By.ID: "warsaw"}))[0]

    driver.execute_script("arguments[0].style.filter='blur(8px)'", element)
    assert element.get_attribute('id') == 'london'
