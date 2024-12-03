import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_buscar(self):
        driver = self.driver
        driver.get("https://promusic.cl")
        self.assertIn("Promusic", driver.title)
        elemento = driver.find_element(By.NAME, "q")
        elemento.send_keys("batería")
        elemento.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No se encontró el elemento:" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        