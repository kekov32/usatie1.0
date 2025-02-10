import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver_setup import get_driver
from utils.helpers import wait
import config

class TestFormSubmission(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(config.BASE_URL)

    def test_form_submission(self):
        self.driver.get(config.BASE_URL + "inputs")
        wait()
        
        input_field = self.driver.find_element(By.XPATH, "//input[@type='number']")
        input_field.send_keys("12345")
        wait()

        self.assertEqual(input_field.get_attribute("value"), "12345", "Значение не введено корректно!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
