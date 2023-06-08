from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class ChangeLocationPage(BasePage):
    COUNTRY_DROP_DOWN = (By.ID, "GLUXCountryListDropdown")
    DROP_BELARUS = (By.ID, "GLUXCountryList_26")
    DROP_POLAND = (By.ID, "GLUXCountryList_178")
    COUNTRY_VALUE = (By.ID, "GLUXCountryValue")
    DONE_BUTTON = (By.XPATH, "//*[contains(text(),'Done')]")

    def __init__(self, driver):
        super().__init__(driver)

    def select_location(self):
        current_country = self.get_element_text(self.COUNTRY_VALUE)
        if current_country == "Belarus":
            self.do_click(self.COUNTRY_DROP_DOWN)
            self.do_click(self.DROP_POLAND)
            self.do_click(self.DONE_BUTTON)
        else:
            self.do_click(self.COUNTRY_DROP_DOWN)
            self.do_click(self.DROP_BELARUS)
            self.do_click(self.DONE_BUTTON)
