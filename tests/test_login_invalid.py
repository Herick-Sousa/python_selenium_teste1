import unittest

from tests.base_test import BaseTest
from pages.loginPage import LoginPage


class LoginInvalidTest(BaseTest):
    def test_login_invalid(self):
        loginpage = LoginPage(self.driver)
        loginpage.login("InvalidUser", "InvalidPassword")
        self.assertTrue(loginpage.error_msg_is_visible())


if __name__ == '__main__':
    unittest.main()
