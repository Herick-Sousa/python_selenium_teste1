import unittest

from tests.base_test import BaseTest
from pages.loginPage import LoginPage
from pages.homePage import HomePage


class LoginSuccessfulTest(BaseTest):
    def test_login_valid(self):
        loginpage = LoginPage(self.driver)
        homepage = HomePage(self.driver)
        loginpage.login("Admin", "admin123")
        self.assertTrue(homepage.user_is_visible())


if __name__ == '__main__':
    unittest.main()
