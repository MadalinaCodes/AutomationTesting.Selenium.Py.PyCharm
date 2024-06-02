# from selenium.webdriver.common.by import By
# from pages.base_page import BasePage
#
#
# class AutoCompletePage(BasePage):
#     # selectors
#     WIDGETS_BUTTON = '//*[text()="Widgets"]'
#     AUTO_COMPLETE_BUTTON = '//span[text()="Auto Complete"]'
#     AUTO_COMPLETE_PAGE_URL = 'https://demoqa.com/auto-complete'
#
#     INPUT_BOX = '//*[@id="autoCompleteMultipleContainer"]/div'
#
#     White = '//*[text()="White"]'
#     Yellow = '//*[text()="Yellow"]'
#     Purple = '//*[text()="Purple"]'
#     Violet = '//*[text()="Violet"]'
#     Indigo = '//*[text()="Indigo"]'
#     Magenta = '//*[text()="Magenta"]'
#
#     Gray = '//*[text()="Gray"]'
#     Orange = '//*[text()="Orange"]'
#     Beige = '//*[text()="Beige"]'
#
#     array = ['W', 'Y', 'P', 'V', 'I', 'M']
#     for letter in array:
#         if
#
#
#     # actions
#     def click_widgets_button(self):
#         self.wait_for_elem(self.WIDGETS_BUTTON)
#         self.driver.find_element(By.XPATH, self.WIDGETS_BUTTON).click()
#
#     def click_auto_complete_button(self):
#         self.wait_for_elem(self.AUTO_COMPLETE_BUTTON)
#         self.driver.find_element(By.XPATH, self.AUTO_COMPLETE_BUTTON).click()
#
#     def check_auto_complete_url(self):
#         assert self.driver.current_url == self.AUTO_COMPLETE_PAGE_URL
#
#     # validations
#     def validate_auto_complete_url(self):
#         expected = 'https://demoqa.com/auto-complete'
#         actual = self.driver.current_url
#         self.assertEqual(expected, actual, 'Url is incorrect')
#
#
#     # query actions
#     def fill_input_box(self, query):
#         self.wait_for_elem(self.INPUT_BOX)
#         search = self.driver.find_element(By.XPATH, self.INPUT_BOX)
#         search.send_keys(query)


#     def validate_auto_complete(self, expected_color):
#         self.wait_for_elem(self.White)
#         actual_color = self.driver.find_element(By.XPATH, self.White).text
#         self.assertEqual(expected_color, actual_color, 'This color is not in the suggestions')
#
#
#     # colordict = {'White': 'W',
#     #              'Yellow': 'Y',
#     #              'Purple': 'P',
#     #              'Violet': 'V',
#     #              'Indigo': 'I',
#     #              'Magenta': 'M',
#     #              'Gray': 'Gr',
#     #              'Orange': 'O',
#     #              'Beige': 'B'}
#
#     # d = {'hello': 4.56, 'bye bye': 3.21}
#     #
#     # driver.get("https://justnotepad.com/")
#     #
#     # for key, value in colordict.items():
#     #     textbox = driver.find_element(By.ID, "editable_text")
#     #     textbox.send_keys(f"{key}:{value}\n")
#
#     def insert_color_letters(self, colordict):
#         for key, value in colordict.items():
#             self.wait_for_elem(self.SEARCH_BOX)
#             self.driver.find_element(By.XPATH, self.SEARCH_BOX).send_keys(value)
#
#     # colordict = {'W': White,
#     #              'Y': Yellow,
#     #              'P': Purple,
#     #              'V': Violet,
#     #              'I': Indigo,
#     #              'M': Magenta,
#     #              'Gr': Gray,
#     #              'O': Orange,
#     #              'B': Beige}
#
#     # # Dicționarul cu datele formularului
#     # form_data = {
#     #     'first_name': 'John',
#     #     'last_name': 'Doe',
#     #     'email': 'john.doe@example.com',
#     #     'phone': '1234567890'
#     # }
#     #
#     # # Completarea formularului folosind datele din dicționar
#     # driver.find_element_by_id('first_name').send_keys(form_data['first_name'])
#     # driver.find_element_by_id('last_name').send_keys(form_data['last_name'])
#     # driver.find_element_by_id('email').send_keys(form_data['email'])
#
#     # def insert_color_letters(self, colordict):
#     #     self.wait_for_elem(self.SEARCH_BOX)
#     #     self.driver.find_element(By.XPATH, self.SEARCH_BOX).send_keys(colordict['White'])
#     #
#
#     # def validate_color_auto_complete(self, expected_color):
#     #     self.wait_for_elem(self.White)
#     #     actual_color = self.driver.find_element(By.XPATH, self.White).text
#     #     self.assertEqual(expected_color, actual_color, 'This color does not appear in the suggestions')
