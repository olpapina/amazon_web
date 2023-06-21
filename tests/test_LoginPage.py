from config.config import TestData
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.test_base import BaseTest


class Test_LoginPage(BaseTest):

    def test_login_page_title(self):
        self.homePage = HomePage(self.driver)
        self.popUpPage = self.homePage.get_pop_up()
        self.popUpPage.click_dont_change()
        self.signInPopUpPage = self.homePage.get_sign_in()
        self.loginPage = self.signInPopUpPage.click_sign_in()
        title = self.loginPage.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_problem_message(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME)
        flag = self.loginPage.is_problem_message()
        text_message_title = self.loginPage.get_problem_message_text()
        text_message_reason = self.loginPage.get_problem_message_reason()
        assert flag
        assert text_message_title == TestData.PROBLEM_MESSAGE_TITLE
        assert text_message_reason == TestData.PROBLEM_MESSAGE_REASON

    def test_sign_up_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_create_account_link_exist()
        assert flag
