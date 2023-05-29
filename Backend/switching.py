import random, time


from kivy.uix.screenmanager import ScreenManager, NoTransition

from Frontend.popups import (
    popup_empty,
    popup_same_theme,
    popup_settings_error,
)
from Database.database_operations import (
    themes_from_db,
    call_settings,
    output_settings_notes,
)


# log (how pages one(Repetition) or two(Check))
def page_selection(button):
    if call_settings()[2]:
        set_screen("pageStartTwo")
    elif call_settings()[3]:
        set_screen("pageStartOne")
    else:
        set_screen("menu")


def random_or_successively():
    randomly = call_settings()[6]
    successively = call_settings()[7]
    if randomly:
        return show_random_notes()
    elif successively:
        return show_successively_notes()


def show_random_notes():
    word = call_settings()[4]
    translate = call_settings()[5]
    if word and translate:
        return separation_notes_randomly()
    elif word and not translate:
        return shuffle_list(separation_word())
    elif translate and not word:
        return shuffle_list(separation_translate())


def show_successively_notes():
    word = call_settings()[4]
    translate = call_settings()[5]
    if word and translate:
        return separation_notes_successively()
    elif word and not translate:
        return separation_word()
    elif translate and not word:
        return separation_translate()


def separation_word():
    word_list = [word for word in output_settings_notes()[::2]]
    return word_list


def separation_translate():
    translate_list = [word for word in output_settings_notes()[1::2]]
    return translate_list


def separation_notes_successively():
    sorted_list_a = [
        list(word_translate(a, output_settings_notes()))[0]
        if i % 2 == 0
        else list(word_translate(a, output_settings_notes()))[1]
        for i, a in enumerate(output_settings_notes()[::2])
    ]
    sorted_list_b = [
        list(word_translate(a, output_settings_notes()))[0]
        if i % 2 != 0
        else list(word_translate(a, output_settings_notes()))[1]
        for i, a in enumerate(output_settings_notes()[::2])
    ]
    separation_list = sorted_list_a + sorted_list_b
    return separation_list


def separation_notes_randomly():
    sorted_list_random = [
        list(word_translate(a, output_settings_notes()))[0]
        if i % 2 == 0
        else list(word_translate(a, output_settings_notes()))[1]
        for i, a in enumerate(shuffle_list(output_settings_notes()))
    ]
    return sorted_list_random


def shuffle_list(lst):
    random_lst = lst.copy()
    random.shuffle(random_lst)
    return random_lst


# error


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


def word_translate(word, lst):
    """
    word_translate:
        checks whether the selected word is a word or a translation and outputs its pair to it.
    """
    index = lst.index(word)
    if index % 2 == 0:
        return word, lst[index + 1]
    else:
        return lst[index - 1], word


def translation_pair(word, lst):
    index = lst.index(word)
    if index % 2 == 0:
        return lst[index + 1]
    else:
        return lst[index - 1]


def set_screen(name_screen):
    """
    set_screen:
        adds all pages and names them
    """
    sm.current = name_screen


sm = ScreenManager(transition=NoTransition())
