from pages.buttons_page import ButtonsPage
from behave import *



buttons_page = ButtonsPage()


@given('buttons: I am a user on buttons page')
def step_impl(context):
    buttons_page.open_page()



# first button
@when('buttons: I double click the first button')
def step_impl(context):
    buttons_page.double_click_first_button()


@then('buttons: I validate that first message is displayed')
def step_impl(context):
    buttons_page.validate_first_button_message()

# second button
@when('buttons: I right click the second button')
def step_impl(context):
    buttons_page.right_click_second_button()


@then('buttons: I validate that second message is displayed')
def step_impl(context):
    buttons_page.validate_second_button_message()

# third button
@when('buttons: I click on the third button')
def step_impl(context):
    buttons_page.dynamic_click_third_button()

@then('buttons: I validate that third message is displayed')
def step_impl(context):
    buttons_page.validate_third_button_message()