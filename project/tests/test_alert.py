import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver_setup import get_driver
from utils.helpers import wait
import config

class TestAlert(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(config.BASE_URL)

    def test_alert(self):
        self.driver.get(config.BASE_URL + "javascript_alerts")
        wait()
        
        alert_button = self.driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
        alert_button.click()
        wait()

        alert = self.driver.switch_to.alert
        alert.accept()
        wait()

        result_text = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result_text, "You successfully clicked an alert")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
