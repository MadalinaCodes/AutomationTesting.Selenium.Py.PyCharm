from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class MenuPage(BasePage):
    # selectors
    ELEMENTS_BUTTON = '//*[text()="Elements"]'
    BUTTONS_BUTTON = '//*[text()="Buttons"][1]'
    BUTTONS_PAGE_URL = 'https://demoqa.com/buttons'

    BOOK_STORE_API = '//span[text()="Book Store API"]'
    BOOK_STORE_API_URL = 'https://demoqa.com/swagger/'

    #actions
    def click_elements_button(self):
        self.wait_for_elem(self.ELEMENTS_BUTTON)
        self.driver.find_element(By.XPATH, self.ELEMENTS_BUTTON).click()

    def click_buttons_button(self):
        self.wait_for_elem(self.BUTTONS_BUTTON)
        self.driver.find_element(By.XPATH, self.BUTTONS_BUTTON).click()

    def check_buttons_url(self):
        assert self.driver.current_url == self.BUTTONS_PAGE_URL

    # validations
    def validate_buttons_url(self):
        sleep(1)
        expected = 'https://demoqa.com/buttons'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')
