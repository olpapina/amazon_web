from selenium.webdriver.common.by import By

from config.config import TestData
from pages.BasePage import BasePage


class ResultPage(BasePage):
    RESULT_LINKS = (By.XPATH, "//*[contains(@class,'s-title-instructions-style')]")
    CHECKBOX_IPAD = (By.XPATH, "//*[@class='a-size-base a-color-base' and contains(text(),'apple ipad')]")

    def __init__(self, driver):
        super().__init__(driver)

    def check_results(self, found_text):
        elements = self.get_elements(self.RESULT_LINKS)
        text_of_links = []
        for element in elements:
            element_text = element.text
            text_of_links.append(element_text.lower())
        for text in text_of_links:
            assert found_text.lower() in text

    def click_checkbox(self):
        self.do_click(self.CHECKBOX_IPAD)
        return ResultPage(self.driver)