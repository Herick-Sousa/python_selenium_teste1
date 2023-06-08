from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    def __init__(self, driver):

        self.driver = driver
        self.user_dropdown = (By.XPATH, "//*[@class ='oxd-userdropdown-tab']")

    def user_is_visible(self):
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(self.user_dropdown))
        return self.driver.find_element(*self.user_dropdown).is_displayed()
