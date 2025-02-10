import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from drivers.webdriver_setup import get_driver
from utils.helpers import wait
import config

class TestDragAndDrop(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(config.BASE_URL)

    def test_drag_and_drop(self):
        self.driver.get(config.BASE_URL + "drag_and_drop")
        wait()
        
        source = self.driver.find_element(By.ID, "column-a")
        target = self.driver.find_element(By.ID, "column-b")

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        wait()

        source_text = self.driver.find_element(By.ID, "column-a").text
        target_text = self.driver.find_element(By.ID, "column-b").text

        self.assertEqual(source_text, "B", "Элемент не перемещен корректно!")
        self.assertEqual(target_text, "A", "Элемент не перемещен корректно!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
