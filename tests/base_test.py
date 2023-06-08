import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed")
