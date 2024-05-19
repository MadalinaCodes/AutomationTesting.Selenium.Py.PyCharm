from time import sleep

from pages.buttons_page import ButtonsPage
from behave import *

buttons_page = ButtonsPage()

@when('books: I click Elements')
def step_impl(context):
    buttons_page.click_elements_button()
    sleep(1)

@when('books: I click Buttons')
def step_impl(context):
    buttons_page.click_buttons_button()
    sleep(1)

@then('buttons: I check that the URL is correct')
def step_impl(context):
    buttons_page.check_url()

# first button
@when('buttons: I double click the first button')
def step_impl(context):
    buttons_page.double_click_first_button()
    sleep(1)

@then('buttons: I validate that first message is displayed')
def step_impl(context, first_message):
    buttons_page.validate_first_button_message(first_message)

# second button
@when('buttons: I right click the second button')
def step_impl(context):
    buttons_page.right_click_second_button()
    sleep(1)

@then('buttons: I validate that second message is displayed')
def step_impl(context):
    buttons_page.validate_second_button_message()

# third button
@when('buttons: I click on the third button')
def step_impl(context):
    buttons_page.dynamic_click_third_button()
    sleep(1)

@then('buttons: I validate that third message is displayed')
def step_impl(context):
    buttons_page.validate_third_button_message()