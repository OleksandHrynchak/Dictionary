import random

from kivy.uix.screenmanager import ScreenManager, NoTransition

from Frontend.popups import (
    popup_empty,
    popup_same_theme,
    popup_create_theme,
    popup_selecte_theme,
)
from Database.SQLite3.database_operations import (
    themes_from_db,
    call_settings,
    output_settings_notes,
)


def is_theme_present():
    """
    is_theme_present:
        Checks if there are theme to choose from.
    """
    return not themes_from_db()


def is_theme_select():
    """
    is_theme_select:
        Checks whether the theme for data output is selected.
    """
    selected_theme = call_settings()[1]
    return selected_theme == "Select theme"


def is_note_present():
    """
    is_note_present:
        Checks if there are note.
    """
    return not output_settings_notes()


def is_theme_ready():
    """
    is_theme_ready:
        Checks if the theme is ready for use.
    """
    if is_theme_present():
        set_screen("pageThemes")
        popup_create_theme()
        return False

    elif is_theme_select():
        set_screen("pageSettings")
        popup_selecte_theme()
        return False

    elif is_note_present():
        set_screen("pageThemes")
        popup_selecte_theme()
        return False

    return True


# How pages opened Repetition or Check
def page_selection(button):
    """
    page_selection:
        Opens the screen according to the saved settings.
    """

    if is_theme_ready():
        check = call_settings()[2]
        repeat = call_settings()[3]
        if check:
            # set_screen opens the selected screen
            set_screen("pageCheck")
        elif repeat:
            # set_screen opens the selected screen
            set_screen("pageRepeat")
        else:
            # set_screen opens the selected screen
            set_screen("menu")


def random_or_successively() -> list:
    """
    random_or_successively:
        Displays a shuffled or successively list according to the settings.
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
        Displays a shuffled list according to the saved setting.
    """
    word = call_settings()[4]
    translate = call_settings()[5]
    if word and translate:
        return separation_notes_randomly()
    elif word and not translate:
        return shuffle_list(separation_words())
    elif translate and not word:
        return shuffle_list(separation_translates())


def show_successively_notes() -> list:
    """
    show_successively_notes:
        Displays a successively list according to the saved setting.
    """
    word = call_settings()[4]
    translate = call_settings()[5]
    if word and translate:
        return separation_notes_successively()
    elif word and not translate:
        return separation_words()
    elif translate and not word:
        return separation_translates()


def separation_words() -> list:
    """
    separation_words:
        Output a successively list of words.
    """
    word_list = [word for word in output_settings_notes()[::2]]
    return word_list


def separation_translates() -> list:
    """
    separation_translates:
        Output a successively list of translations.
    """
    translate_list = [word for word in output_settings_notes()[1::2]]
    return translate_list


def separation_notes_successively() -> list:
    """
    separation_notes_successively:
        Output a successively, unmixed list, the content of which is sequentially followed by the word translation.
    """
    words = output_settings_notes()
    sorted_list_a = []
    sorted_list_b = []

    for index, word in enumerate(words[::2]):
        note = list(word_translate(word, words))
        if index % 2 == 0:
            sorted_list_a.append(note[0])
        else:
            sorted_list_a.append(note[1])

    for index, word in enumerate(words[::2]):
        note = list(word_translate(word, words))
        if index % 2 != 0:
            sorted_list_b.append(note[0])
        else:
            sorted_list_b.append(note[1])

    separation_list = sorted_list_a + sorted_list_b
    return separation_list


def separation_notes_randomly() -> list:
    """
    separation_notes_randomly:
        Sorts the shuffled list so that the list looks like the word translation.
    """
    words = output_settings_notes()
    sorted_list_random = []

    for index, word in enumerate(shuffle_list(words)):
        note = list(word_translate(word, words))
        if index % 2 == 0:
            sorted_list_random.append(note[0])
        else:
            sorted_list_random.append(note[1])
    return sorted_list_random


def shuffle_list(lst: list) -> list:
    """
    shuffle_list:
        Shuffles the elements of the resulting list.
    """
    random_lst = lst.copy()
    random.shuffle(random_lst)
    return random_lst


def field_empty(word: str) -> bool:
    """
    field_empty:
        Checks if the field is not empty.
    """
    test_theme = word.strip()
    if test_theme:
        return True
    else:
        return False


def fields_empty(word: str, translate: str, function):
    """
    fields_empty:
        Checks if the fields are not empty.
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
        Checks whether the selected word is not a list item.
    """
    if themes_from_db():
        # themes_from_db retrieves themes from the database.
        if not word in themes_from_db():
            return True
        else:
            return False
    else:
        return True


def check_themes(word: str, function):
    """
    check_themes:
        Performs the function if the field is not empty and if the searched word is not in the list.
    """
    # field_empty checks if the field is not empty.
    if not field_empty(word):
        popup_empty()

    # same_theme checks whether the selected word is not a list item.
    elif not same_theme(word):
        popup_same_theme()
    else:
        function(word)


def word_translate(word: str, lst: list) -> tuple:
    """
    word_translate:
        Checks whether the highlighted word is a 'word' or a 'translation' and outputs the word and its pair.
    """
    index = lst.index(word)
    if index % 2 == 0:
        return word, lst[index + 1]
    else:
        return lst[index - 1], word


def translation_pair(word: str, lst: list) -> str:
    """
    translation_pair:
        Checks whether the highlighted word is "word" or "translation" and outputs its pair.
    """
    index = lst.index(word)
    if index % 2 == 0:
        return lst[index + 1]
    else:
        return lst[index - 1]


def set_screen(name_screen: str):
    """
    set_screen:
        Adds all pages and names them.
    """
    sm.current = name_screen


sm = ScreenManager(transition=NoTransition())
