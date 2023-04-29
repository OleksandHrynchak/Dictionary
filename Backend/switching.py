from kivy.uix.screenmanager import ScreenManager, NoTransition

from Frontend.popups import ErrorPopup
from Database.database_operations import themes_from_db


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


def popup_empty():
    popup = ErrorPopup(
        title="The field is not filled",
        title_size=18,
        size_hint=(.8, .6),
        pos_hint={'x': .1, 'y': .2},
        separator_height=3,
        separator_color=[.0, .84, .64],
    )
    popup.open()


def popup_same_theme():
    popup = ErrorPopup(
        title="Repetition error",
        title_size=18,
        size_hint=(.8, .6),
        pos_hint={'x': .1, 'y': .2},
        separator_height=3,
        separator_color=[.0, .84, .64],
    )
    popup.open()
    popup.lable_warning.text = "This theme already exists"


def field_empty(word):
    """
    field_empty:
        checks if the field is not empty.
    """
    test_theme = word.strip()
    if test_theme:
        return True
    else:
        return False


def fields_empty(word, translate, function):
    """
    fields_empty: 
        checks if the fields are not empty.
    """
    test_word = word.strip()
    test_translate = translate.strip()
    if test_word and test_translate:
        function(word, translate)
    else:
        # brings up an error window
        popup_empty()


def same_theme(word):
    """
    same_theme:
        checks whether the selected word is not a list item.
        themes_from_db retrieves themes from the database.
    """
    if not word in themes_from_db():
        return True
    else:
        return False


def check_themes(word, function):
    """
    check_themes:
        field_empty checks if the field is not empty.
        same_theme checks whether the selected word is not a list item.
        performs the function if the field is not empty and the searched word is not in the list.
    """
    if not field_empty(word):
        popup_empty()
        return
    elif not same_theme(word):
        popup_same_theme()
        return
    else:
        function(word)
        return
# error\


def word_translate(word, lst):
    """
    word_translate:
        checks whether the selected word is a word or a translation and outputs its pair to it.
    """
    index = lst.index(word)
    if index % 2 == 0:
        return word, lst[index+1]
    else:
        return lst[index-1], word


def set_screen(name_screen):
    """
    set_screen:
        adds all pages and names them
    """
    sm.current = name_screen


sm = ScreenManager(transition=NoTransition())
