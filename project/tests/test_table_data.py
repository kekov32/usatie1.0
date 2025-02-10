import unittest
from selenium.webdriver.common.by import By
from drivers.webdriver_setup import get_driver
from utils.helpers import wait
import config

class TestTableData(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get(config.BASE_URL)

    def test_table_data(self):
        self.driver.get(config.BASE_URL + "tables")
        wait()
        
        rows = self.driver.find_elements(By.XPATH, "//table[@id='table1']//tr")
        wait()

        self.assertGreater(len(rows), 1, "Таблица пустая!")

        first_row_cells = rows[1].find_elements(By.TAG_NAME, "td")
        self.assertGreater(len(first_row_cells), 0, "Первая строка таблицы пустая!")

        last_name = first_row_cells[0].text
        self.assertTrue(last_name, "Фамилия в первой строке не найдена!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
