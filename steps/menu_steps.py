from pages.menu_page import MenuPage
from behave import *

menu_page = MenuPage()


# buttons
@when('books: I click Elements')
def step_impl(context):
    menu_page.click_elements_button()

@when('books: I click Buttons')
def step_impl(context):
    menu_page.click_buttons_button()

@then('buttons: I check that the URL is correct')
def step_impl(context):
    menu_page.validate_buttons_url()

# web tables
@when('books: I click Web Tables')
def step_impl(context):
    menu_page.click_web_tables_button()

@then('webtables: I check that the URL is correct')
def step_impl(context):
    menu_page.validate_web_tables_url()

# auto complete
@when('books: I click Widgets')
def step_impl(context):
    menu_page.click_widgets_button()

@when('books: I click Auto Complete')
def step_impl(context):
    menu_page.click_auto_complete_button()

@then('auto-complete: I validate the URL')
def step_impl(context):
    menu_page.validate_auto_complete_url()


