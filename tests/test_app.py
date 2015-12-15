import base_test

@base_test.on_platforms(base_test.devices)
class SubTest1(base_test.BaseTest):

    def test_sum1(self):
        # populate text fields with values
        field_one = self.driver.find_element_by_accessibility_id("TextField1")
        field_one.send_keys("12")

        field_two = self.driver.find_elements_by_class_name("UIATextField")[1]
        field_two.send_keys("8")

        # trigger computation by using the button
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click();

        # is sum equal?
        sum = self.driver.find_element_by_class_name("UIAStaticText").text;
        assert int(sum) == 20, "ERROR MESSAGE"

    def test_sum2(self):
        # populate text fields with values
        field_one = self.driver.find_element_by_accessibility_id("TextField1")
        field_one.send_keys("12")

        field_two = self.driver.find_elements_by_class_name("UIATextField")[1]
        field_two.send_keys("8")

        # trigger computation by using the button
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click();

        # is sum equal?
        sum = self.driver.find_element_by_class_name("UIAStaticText").text;
        assert int(sum) == 20, "ERROR MESSAGE"
