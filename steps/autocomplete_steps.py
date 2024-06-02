# from pages.autocomplete_page import AutoCompletePage
# from behave import *
#
# autocomplete_page = AutoCompletePage()
#
#
# @when('books: I click Widgets')
# def step_impl(context):
#     autocomplete_page.click_widgets_button()
#
#
# @when('books: I click Auto Complete')
# def step_impl(context):
#     autocomplete_page.click_auto_complete_button()
#
#
# @then('auto-complete: I check that the URL is correct')
# def step_impl(context):
#     autocomplete_page.validate_auto_complete_url()
#
#
# @when('auto-complete: I introduce "{query}"')
# def step_impl(context, query):
#     autocomplete_page.fill_input_box(query)
#
#
# @then('auto-complete: I validate that the "{suggestion}" is displayed')
# def step_impl(context, suggestion):
#     autocomplete_page.validate_auto_complete(suggestion)
#
# # @when('auto-complete: I introduce w')
# # def step_impl(context):
# #     autocomplete_page.insert_color_letters('w')
# #
# #
# # @then('auto-complete: I validate that the color name is displayed')
# # def step_impl(context):
# #     autocomplete_page.validate_color_auto_complete('White')
