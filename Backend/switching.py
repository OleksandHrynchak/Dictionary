import random


from kivy.uix.screenmanager import ScreenManager, NoTransition

from Frontend.popups import popup_empty, popup_same_theme
from Database.SQLite3.database_operations import (
    themes_from_db,
    call_settings,
    output_settings_notes,
)

"""from Database.MySQL.database_operations import (
    themes_from_db,
    call_settings,
    output_settings_notes,
)"""


# log (how pages one(Repetition) or two(Check))
def page_selection(button):
    """
    page_selection:
        opens the screen according to the saved settings.
    """
    if call_settings()[2]:
        # set_screen opens the selected screen
        set_screen("pageCheck")
    elif call_settings()[3]:
        # set_screen opens the selected screen
        set_screen("pageRepeat")
    else:
        # set_screen opens the selected screen
        set_screen("menu")


def random_or_successively() -> list:
    """
    random_or_successively:
        displays a shuffled or successively list according to the settings.
    """
    randomly = call_settings()[6]
    successively = call_settings()[7]
    if randomly:
        return show_random_notes()
    elif successively:
        return show_successively_notes()


def show_random_notes() -> list:
    """
    show_random_notes:
        displays a shuffled list according to the saved setting.
    """
    word = call_settings()[4]
    translate = call_settings()[5]
    if word and translate:
        return separation_notes_randomly()
    elif word and not translate:
        return shuffle_list(separation_word())
    elif translate and not word:
        return shuffle_list(separation_translate())


def show_successively_notes() -> list:
    """
    show_successively_notes:
        displays a successively list according to the saved setting.
    """
    word = call_settings()[4]
    translate = call_settings()[5]
    if word and translate:
        return separation_notes_successively()
    elif word and not translate:
        return separation_word()
    elif translate and not word:
        return separation_translate()


def separation_word() -> list:
    """
    separation_word:
        output a successively list of words.
    """
    word_list = [word for word in output_settings_notes()[::2]]
    return word_list


def separation_translate() -> list:
    """
    separation_translate:
        utput a successively list of translations.
    """
    translate_list = [word for word in output_settings_notes()[1::2]]
    return translate_list


def separation_notes_successively() -> list:
    """
    separation_notes_successively:
        output a successively, unmixed list, the content of which is sequentially followed by the word translation.
    """
    sorted_list_a = [
        list(word_translate(word, output_settings_notes()))[0]
        if index % 2 == 0
        else list(word_translate(word, output_settings_notes()))[1]
        for index, word in enumerate(output_settings_notes()[::2])
    ]
    sorted_list_b = [
        list(word_translate(word, output_settings_notes()))[0]
        if index % 2 != 0
        else list(word_translate(word, output_settings_notes()))[1]
        for index, word in enumerate(output_settings_notes()[::2])
    ]
    separation_list = sorted_list_a + sorted_list_b
    return separation_list


def separation_notes_randomly() -> list:
    """
    separation_notes_randomly:
        sorts the shuffled list so that the list looks like the word translation.
    """
    sorted_list_random = [
        list(word_translate(word, output_settings_notes()))[0]
        if index % 2 == 0
        else list(word_translate(word, output_settings_notes()))[1]
        for index, word in enumerate(shuffle_list(output_settings_notes()))
    ]
    return sorted_list_random


def shuffle_list(lst: list) -> list:
    """
    shuffle_list:
        shuffles the elements of the resulting list.
    """
    random_lst = lst.copy()
    random.shuffle(random_lst)
    return random_lst


# error


def field_empty(word: str) -> bool:
    """
    field_empty:
        checks if the field is not empty.
    """
    test_theme = word.strip()
    if test_theme:
        return True
    else:
        return False


def fields_empty(word: str, translate: str, function):
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


def same_theme(word: str) -> bool:
    """
    same_theme:
        checks whether the selected word is not a list item.
        themes_from_db retrieves themes from the database.
    """
    if not word in themes_from_db():
        return True
    else:
        return False


def check_themes(word: str, function):
    """
    check_themes:
        field_empty checks if the field is not empty.
        same_theme checks whether the selected word is not a list item.
        performs the function if the field is not empty and the searched word is not in the list.
    """
    if not field_empty(word):
        popup_empty()
    elif not same_theme(word):
        popup_same_theme()
    else:
        function(word)


def word_translate(word: str, lst: list) -> tuple:
    """
    word_translate:
        checks whether the highlighted word is a 'word' or a 'translation' and outputs the word and its pair.
    """
    index = lst.index(word)
    if index % 2 == 0:
        return word, lst[index + 1]
    else:
        return lst[index - 1], word


def translation_pair(word: str, lst: list) -> str:
    """
    translation_pair:
        checks whether the highlighted word is "word" or "translation" and outputs its pair.
    """
    index = lst.index(word)
    if index % 2 == 0:
        return lst[index + 1]
    else:
        return lst[index - 1]


def set_screen(name_screen: str):
    """
    set_screen:
        adds all pages and names them.
    """
    sm.current = name_screen


sm = ScreenManager(transition=NoTransition())
