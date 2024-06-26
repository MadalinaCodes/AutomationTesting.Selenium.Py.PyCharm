from browser import Browser # din fisierul browsser importam clasa Browser
from pages.autocomplete_page import AutoCompletePage


def before_all(context):
    context.browser = Browser() # punem acel Browser intr-un context al aplicatiei, frameworkul behave instalat la inceput are nevoie de acest context, before_all si after_all sunt functii predefinite in behave
    context.autocomplete_page = AutoCompletePage()

def after_all(context):
    context.browser.close()

"""
ce fac aceste 2 fisiere?
 -browser.py- 
creeaza clasa Browser cu initializarea browserului si a waiturilor
si in -environment.py- 
avem 2 metode
una care se apeleaza inainte de fiecare test
si alta care se apeleaza dupa fiecare test
"""