from config.config import TestData
from pages.HomePage import HomePage
from tests.test_base import BaseTest


class Test_AppStore_Redirect(BaseTest):

    def test_e2e_appstore_page(self):
        self.homePage = HomePage(self.driver)
        self.menu = self.homePage.click_menu()
        self.menu.click_appstore()

        self.appstorePage = self.menu.click_download_appstore()
        title = self.appstorePage.get_appstore_page_title(TestData.APPSTORE_TITLE)
        assert title == TestData.APPSTORE_TITLE
