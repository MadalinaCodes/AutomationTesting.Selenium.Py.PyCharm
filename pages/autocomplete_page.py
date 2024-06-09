from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AutoCompletePage(BasePage):
    # selectors
    AUTO_COMPLETE_BUTTON = '//span[text()="Auto Complete"]'
    AUTO_COMPLETE_PAGE_URL = 'https://demoqa.com/auto-complete'

    INPUT_BOX = '//*[@id="autoCompleteMultipleInput"]'

    AUTOCOMPLETE_VALUE = "auto-complete__multi-value__label"


    def fill_input_box(self, query):
        self.wait_for_elem(self.INPUT_BOX)
        search = self.driver.find_element(By.XPATH, self.INPUT_BOX)
        search.send_keys(query)
        search.send_keys(Keys.ENTER)


    # actions
    def click_auto_complete_button(self):
        self.wait_for_elem(self.AUTO_COMPLETE_BUTTON)
        self.driver.find_element(By.XPATH, self.AUTO_COMPLETE_BUTTON).click()

    def check_auto_complete_url(self):
        assert self.driver.current_url == self.AUTO_COMPLETE_PAGE_URL


    # validations
    def validate_auto_complete_url(self):
        expected = 'https://demoqa.com/auto-complete'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')

    def validate_color_auto_complete(self, query):
        colordict = {'Yellow': 'Y',
                     'Purple': 'P',
                     'Magenta': 'M',
                     'Green': 'Gr'}

        expected_color = ''
        for key in colordict.keys():
            if colordict[f'{key}'] == query:
                expected_color = key

        autocomplete_color = self.driver.find_element(By.CLASS_NAME, self.AUTOCOMPLETE_VALUE).text
        assert expected_color == autocomplete_color
