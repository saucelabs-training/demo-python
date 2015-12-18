from .base_test import *
from .sauceutils import *


@on_platforms(devices)
class SubTest1(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()
        if cls.upload:
            upload_app(cls.app_path, cls.username, cls.access_key)

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


if __name__ == '__main__':
    unittest.main()