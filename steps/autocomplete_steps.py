from pages.autocomplete_page import AutoCompletePage
from behave import *

autocomplete_page = AutoCompletePage()


@when('widgets: I click Auto Complete')
def step_impl(context):
    autocomplete_page.click_auto_complete_button()


@when('auto-complete: I introduce "{query}"')
def step_impl(context, query):
    autocomplete_page.fill_input_box(query)

@then('auto-complete: I validate that proper color is displayed for "{query}"')
def step_impl(context, query):
    context.autocomplete_page.validate_color_auto_complete(query)
