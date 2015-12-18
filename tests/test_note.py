from .base_test import *
from .sauceutils import *


@on_platforms(browsers)
class SubTest1(BaseTest):

    @classmethod
    def setup_class(cls):
        BaseTest.setup_class()
        upload_app(cls.app_path, cls.username, cls.access_key)

        # verify google title
        # click to make a new note in the app

    def test_note(self):
        self.driver.find_element_by_accessibility_id('New note').click()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys('Here is a new note from Python')
        self.driver.find_element_by_accessibility_id('Save').click()
        notes = self.driver.find_elements_by_class_name('android.widget.TextView')
        self.assertEqual(notes[2].text, 'Here is a new note from Python')


if __name__ == '__main__':
    unittest.main()
