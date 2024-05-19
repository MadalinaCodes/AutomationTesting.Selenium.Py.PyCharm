from browser import Browser # din fisierul browsser importam clasa Browser
from pages.books_page import BooksPage
from pages.buttons_page import ButtonsPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser() # punem acel Browser intr-un context al aplicatiei, frameworkul behave instalat la inceput are nevoie de acest context, before_all si after_all sunt functii predefinite in behave
    # context.login_page = LoginPage()
    # context.books_page = BooksPage()
    # context.home_page = HomePage()
    # context.buttons_page = ButtonsPage()

def after_all(context):
    context.browser.close()

"""
ce fac aceste 2 fisiere?
 -browser.py- 
creeaza clasa Browser cu initializarea browserului si a waiturilor
si in -context.py- 
avem 2 metode
una care se apeleaza inainte de fiecare test
si alta care se apeleaza dupa fiecare test
"""