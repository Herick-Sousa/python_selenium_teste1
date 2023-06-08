from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//*[@type='submit']")
        self.error_msg = (By.XPATH, "//*[@role='alert']")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_on_login_button()

    def enter_username(self, username):
        WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def error_msg_is_visible(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.error_msg))
        return self.driver.find_element(*self.error_msg).is_displayed()
