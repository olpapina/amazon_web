from config.config import TestData
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_LoginPage(BaseTest):

    def test_login_page_title(self):
        self.homePage = HomePage(self.driver)
        self.homePage.click_dont_change()
        self.loginPage = self.homePage.click_sign_in()
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME)
        self.loginPage.is_problem_message()

    def test_sign_up_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_create_account_link_exist()
        assert flag
