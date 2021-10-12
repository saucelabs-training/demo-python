from selenium.webdriver.common.by import By


# Property and Attribute often return effectively the same value. The biggest difference in Ruby is
# that Attribute always returns a String and Property returns the applicable primitive
# Attribute is defined in html spec: https://dom.spec.whatwg.org/#concept-element-attribute
# Property is defined in ecma spec: https://262.ecma-international.org/5.1/#sec-4.3.26
#
# Element#attribute guesses which value you want from an element's attribute or property value and returns that
#
# Since this doesn't make sense in a specification, w3c defines 2 new endpoints, made available in Selenium as:
# Element#dom_attribute and Element#property
# The old behavior with the existing method is still available, but executes a large javascript blob
# New behavior should be preferred for performance and preciseness

def test_boolean(driver):
    driver.get("http://watir.com/examples/forms_with_input_elements.html")

    element = driver.find_element(by=By.CSS_SELECTOR, value="#new_user_interests_books")

    assert element.get_attribute('checked') == 'true'
    assert element.get_dom_attribute('checked') == 'true'
    assert element.get_property('checked') is True


def test_number(driver):
    driver.get("http://watir.com/examples/forms_with_input_elements.html")
    element = driver.find_element(by=By.CSS_SELECTOR, value="#new_user_interests_books")

    # Note that the name of the property and the attribute may be different
    # another example is `class` vs `className`

    assert element.get_attribute('tabindex') == '1'
    assert element.get_attribute('tabIndex') == '1'
    assert element.get_dom_attribute('tabindex') == '1'
    assert element.get_dom_attribute('tabIndex') == '1'
    assert element.get_property('tabindex') is None
    assert element.get_property('tabIndex') == 1


def test_update_boolean(driver):
    driver.get("http://watir.com/examples/forms_with_input_elements.html")

    element = driver.find_element(by=By.CSS_SELECTOR, value="#new_user_interests_books")
    element.click()

    assert element.get_attribute('checked') is None
    assert element.get_dom_attribute('checked') == 'true'
    assert element.get_property('checked') is False


def test_update_string(driver):
    driver.get("http://watir.com/examples/forms_with_input_elements.html")

    element = driver.find_element(by=By.CSS_SELECTOR, value="#new_user_occupation")

    assert element.get_attribute('value') == "Developer"
    assert element.get_dom_attribute('value') == "Developer"
    assert element.get_property('value') == "Developer"

    element.clear()
    element.send_keys("Engineer")

    assert element.get_attribute('value') == "Engineer"
    assert element.get_dom_attribute('value') == "Developer"
    assert element.get_property('value') == "Engineer"


def test_processed_values(driver):
    driver.get("http://watir.com/examples/non_control_elements.html")

    element = driver.find_element(by=By.CSS_SELECTOR, value="#link_3")

    assert element.get_attribute('href') == "http://watir.com/examples/forms_with_input_elements.html"
    assert element.get_dom_attribute('href') == "forms_with_input_elements.html"
    assert element.get_property('href') == "http://watir.com/examples/forms_with_input_elements.html"


def test_case_sensitive(driver):
    driver.get("http://watir.com/examples/forms_with_input_elements.html")

    element = driver.find_element(by=By.CSS_SELECTOR, value="#new_user_email")

    assert element.get_attribute('nAme') == "new_user_email"
    assert element.get_dom_attribute('nAme') == "new_user_email"
    assert element.get_property('nAme') is None
