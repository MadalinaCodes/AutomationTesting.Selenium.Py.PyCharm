from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MenuPage(BasePage):
    # selectors
    ELEMENTS_BUTTON = '//*[text()="Elements"]'
    BUTTONS_BUTTON = '//span[text()="Buttons"]'
    BUTTONS_PAGE_URL = 'https://demoqa.com/buttons'

    WEB_TABLES_BUTTON = '//span[text()="Web Tables"]'
    WEB_TABLES_URL = 'https://demoqa.com/webtables'

    WIDGETS_BUTTON = '//*[text()="Widgets"]'
    AUTO_COMPLETE_BUTTON = '//span[text()="Auto Complete"]'
    AUTO_COMPLETE_PAGE_URL = 'https://demoqa.com/auto-complete'

    # buttons actions
    def click_elements_button(self):
        self.wait_for_elem(self.ELEMENTS_BUTTON)
        self.driver.find_element(By.XPATH, self.ELEMENTS_BUTTON).click()

    def click_buttons_button(self):
        self.wait_for_elem(self.BUTTONS_BUTTON)
        self.driver.find_element(By.XPATH, self.BUTTONS_BUTTON).click()

    def check_buttons_url(self):
        assert self.driver.current_url == self.BUTTONS_PAGE_URL

    # buttons validations
    def validate_buttons_url(self):
        expected = 'https://demoqa.com/buttons'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')


    # web tables actions

    def click_elements_button(self):
        self.wait_for_elem(self.ELEMENTS_BUTTON)
        self.driver.find_element(By.XPATH, self.ELEMENTS_BUTTON).click()

    def click_web_tables_button(self):
        self.wait_for_elem(self.WEB_TABLES_BUTTON)
        self.driver.find_element(By.XPATH, self.WEB_TABLES_BUTTON).click()

    def check_web_tables_url(self):
        assert self.driver.current_url == self.WEB_TABLES_URL

    # web tables validations
    def validate_web_tables_url(self):
        expected = 'https://demoqa.com/webtables'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')


    # # auto complete actions
    # def click_widgets_button(self):
    #     self.wait_for_elem(self.WIDGETS_BUTTON)
    #     self.driver.find_element(By.XPATH, self.WIDGETS_BUTTON).click()
    #
    # def click_auto_complete_button(self):
    #     self.wait_for_elem(self.AUTO_COMPLETE_BUTTON)
    #     self.driver.find_element(By.XPATH, self.AUTO_COMPLETE_BUTTON).click()
    #
    # def check_auto_complete_url(self):
    #     assert self.driver.current_url == self.AUTO_COMPLETE_PAGE_URL
    #
    # # auto complete validations
    # def validate_auto_complete_url(self):
    #     expected = 'https://demoqa.com/auto-complete'
    #     actual = self.driver.current_url
    #     self.assertEqual(expected, actual, 'Url is incorrect')