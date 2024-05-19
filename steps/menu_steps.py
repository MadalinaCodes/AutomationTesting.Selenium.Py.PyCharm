from time import sleep

from pages.menu_page import MenuPage
from behave import *

menu_page = MenuPage()

@when('books: I click Elements')
def step_impl(context):
    menu_page.click_elements_button()
    sleep(1)

@when('books: I click Buttons')
def step_impl(context):
    menu_page.click_buttons_button()
    sleep(1)

@then('buttons: I check that the URL is correct')
def step_impl(context):
    menu_page.validate_buttons_url()
