from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle

from Frontend.popups import NotFilledPopup


def set_screen(name_screen):
    sm.current = name_screen


# log (how pages one(Repetition) or two(Check))
def page_one(Check, activeone):
    if activeone == True:
        global pagecheck
        pagecheck = True
    elif activeone == False:
        pagecheck = False


def page_two(Repetition, activetwo):
    if activetwo == True:
        global pagerepetition
        pagerepetition = True
    elif activetwo == False:
        pagerepetition = False


def one_or_two(any):
    if pagecheck:
        set_screen('pageStartOne')
    elif pagerepetition:
        set_screen('pageStartTwo')
    else:
        set_screen('menu')
# /log

# error


def popup_problems():
    popup = NotFilledPopup(
        title="Поле не заповнено",
        title_size=18,
        size_hint=(.8, .6),
        pos_hint={'x': .1, 'y': .2},
        separator_height=3,
        separator_color=[.0, .84, .64],
    )
    popup.open()


def field_empty(theme, function):
    test_theme = theme.strip()
    if test_theme:
        function(theme)
    else:
        popup_problems()


def fields_empty(word, translate, function):
    test_word = word.strip()
    test_translate = translate.strip()
    if test_word and test_translate:
        function(None)
    else:
        popup_problems()

    # $$$$$$$
# /error


sm = ScreenManager(transition=NoTransition())
