from config.config import TestData
from pages.HomePage import HomePage
from tests.test_base import BaseTest


class Test_Search_Filter(BaseTest):

    def test_search_result(self):
        self.homePage = HomePage(self.driver)
        self.searchBlock = self.homePage.get_search_block()
        self.resultPage = self.searchBlock.do_search()
        self.resultPage.check_results(TestData.SEARCH_TEXT)
        self.resultPage_filtered = self.resultPage.click_checkbox()
        self.resultPage_filtered.check_results(TestData.FILTER_TEXT)
