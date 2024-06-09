from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ButtonsPage(BasePage):
    # selectors
    BUTTONS_PAGE_URL = 'https://demoqa.com/buttons'

    DOUBLE_CLICK_ME_BUTTON = '//*[@id="doubleClickBtn"]'
    RIGHT_CLICK_ME_BUTTON = '//*[@id="rightClickBtn"]'
    CLICK_ME_BUTTON = '//*[text()="Click Me"]'

    DOUBLE_CLICK_MESSAGE = '//*[@id="doubleClickMessage"]'
    RIGHT_CLICK_MESSAGE = '//*[@id="rightClickMessage"]'
    DYNAMIC_CLICK_MESSAGE = '//*[@id="dynamicClickMessage"]'


    def open_page(self):
        self.driver.get(self.BUTTONS_PAGE_URL)

    #actions
    def double_click_first_button(self):
        self.action = ActionChains(self.driver)
        self.wait_for_elem(self.DOUBLE_CLICK_ME_BUTTON)
        double_click_button = self.driver.find_element(By.XPATH, self.DOUBLE_CLICK_ME_BUTTON)
        self.action.double_click(double_click_button).perform()

    def right_click_second_button(self):
        self.action = ActionChains(self.driver)
        self.wait_for_elem(self.RIGHT_CLICK_ME_BUTTON)
        right_click = self.driver.find_element(By.XPATH, self.RIGHT_CLICK_ME_BUTTON)
        self.action.context_click(right_click).perform()

    def dynamic_click_third_button(self):
        self.wait_for_elem(self.CLICK_ME_BUTTON)
        self.driver.find_element(By.XPATH, self.CLICK_ME_BUTTON).click()

    # validations
    def validate_first_button_message(self):
        self.wait_for_elem(self.DOUBLE_CLICK_MESSAGE)
        expected_message = 'You have done a double click'
        actual = self.driver.find_element(By.XPATH, self.DOUBLE_CLICK_MESSAGE).text
        self.assertEqual(expected_message, actual, 'You did not use the first button correctly, try double clicking.')

    def validate_second_button_message(self):
        self.wait_for_elem(self.RIGHT_CLICK_MESSAGE)
        expected_message = 'You have done a right click'
        actual = self.driver.find_element(By.XPATH, self.RIGHT_CLICK_MESSAGE).text
        self.assertEqual(expected_message, actual, 'You did not use the second button correctly, try right clicking it.')

    def validate_third_button_message(self):
        self.wait_for_elem(self.DYNAMIC_CLICK_MESSAGE)
        expected_message = 'You have done a dynamic click'
        actual = self.driver.find_element(By.XPATH, self.DYNAMIC_CLICK_MESSAGE).text
        self.assertEqual(expected_message, actual, 'You did not use the third button correctly, try clicking it once.')

