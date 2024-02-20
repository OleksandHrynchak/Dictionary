from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.metrics import sp


from Frontend.background import KV
from Frontend.moduls import RoundedButton, DarkenedGridLayout
from Frontend.popups import (
    AddThemePopup,
    RenameNotesPopup,
    DeleteNotePopup,
    RenamePopup,
    DeletePopup,
    DictBubble,
)
from Backend.switching import (
    set_screen,
    fields_empty,
    check_themes,
    word_translate,
    sm,
)
from Database.SQLite3.database_operations import (
    add_theme,
    themes_from_db,
    id_theme,
    save_word_and_translate,
    output_notes,
    update_theme,
    delete_theme,
    delete_notes,
    update_note,
    delete_note,
)


class PageThemes(Screen):
    """
    PageThemes:
        Class inherited from `Screen`,\n
        which represents a screen for viewing topics in the program and their content.
    """

    def __init__(self, **kwargs):
        super(PageThemes, self).__init__(**kwargs)
        # Main layout.
        self.relativelayout = RelativeLayout()
        # Layout for records used in scroll view.
        self.floatlayout = FloatLayout(size_hint_y=1.4)
        # Gridlayout in which the background is darkened.
        self.gridlayout = DarkenedGridLayout(cols=2, size_hint_y=None, height=0)
        # Layout for a spinner.
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation="horizontal",
            size_hint=[0.7, 0.19],
            pos_hint={"x": 0.15, "y": 0.70},
        )
        # Main scroll view.
        self.scrollview = ScrollView(
            size_hint=(1, 0.8),
            pos_hint={"x": 0, "y": 0.05},
        )
        # Scroll view to display words in gridlayout.
        self.scrollview_for_notes = ScrollView(
            size_hint=(0.7, 0.6), pos_hint={"x": 0.15, "y": 0.22}
        )
        # Background.
        self.root = Builder.load_string(KV)
        # --------------------------------------------------------------------------------------
        self.spinner = Spinner(
            text="Select a themes",
            font_size=sp(18),
            size_hint=(0.7, 0.30),
            pos_hint={"x": 0.15, "y": 0.7},
        )
        # id_theme defines id theme.
        self.spinner.bind(text=id_theme)
        # range_notes displays the notes of the given theme.
        self.spinner.bind(text=self.range_notes)
        # start_timer_for_themes calls a bubble if the button is held down for more than 1 second.
        self.spinner.bind(on_press=self.start_timer_for_themes)
        # stop_timer_for_theme cancels the start_timer_for_notes event if
        # the button has not been pressed for more than one second.
        self.spinner.bind(on_release=self.stop_timer_for_theme)
        self.close_spiner = None
        self.spinner.dropdown_cls.max_height = self.spinner.height * 2 + 5
        # -------------------------------------------------------------------------------------
        # set_screen opens the selected screen
        self.relativelayout.add_widget(
            RoundedButton(
                text="<--",
                on_press=lambda page: set_screen("menu"),
                on_release=self.update_scroll_views,
                font_size=sp(20),
                size_hint=(0.16, 0.08),
                pos_hint={"x": 0.04, "y": 0.89},
            )
        )

        self.floatlayout.add_widget(
            RoundedButton(
                text="Add a theme",
                on_press=self.popup_add_themes,
                font_size=sp(20),
                size_hint=(0.7, 0.07),
                pos_hint={"x": 0.15, "y": 0.92},
            )
        )

        self.text_input_word = TextInput(
            hint_text="Word",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(18),
            halign="center",
            size_hint=(0.38, 0.08),
            pos_hint={"x": 0.1, "y": 0.12},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        self.floatlayout.add_widget(self.text_input_word)

        self.text_input_translate = TextInput(
            hint_text="Translate",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(18),
            halign="center",
            size_hint=(0.38, 0.08),
            pos_hint={"x": 0.5, "y": 0.12},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        self.floatlayout.add_widget(self.text_input_translate)

        self.button_add_note = RoundedButton(
            text="Add a word",
            font_size=sp(20),
            size_hint=(0.6, 0.07),
            pos_hint={"x": 0.2, "y": 0.02},
        )
        self.floatlayout.add_widget(self.button_add_note)
        # fields_empty checks if the fields are not empty.
        self.button_add_note.bind(
            on_press=lambda a: fields_empty(
                self.text_input_word.text,
                self.text_input_translate.text,
                self.click_button_add_note,
            )
        )

        self.scrollview_for_notes.add_widget(self.gridlayout)
        boxlayout.add_widget(self.spinner)
        self.floatlayout.add_widget(self.scrollview_for_notes)
        self.floatlayout.add_widget(boxlayout)
        self.scrollview.add_widget(self.floatlayout)
        self.relativelayout.add_widget(self.scrollview)
        self.add_widget(self.root)
        self.add_widget(self.relativelayout)

    def popup_add_themes(self, button):
        """
        popup_add_themes
            Causes a popup to add a new theme.
        """
        self.popup_new_theme = AddThemePopup(
            title="Add a theme",
            title_size=sp(18),
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
        )
        self.popup_new_theme.open()
        button_add = self.popup_new_theme.button_add
        # check_themes checks whether the field is empty and whether there are no similar themes.
        button_add.bind(
            on_press=lambda pres: check_themes(
                self.popup_new_theme.text_input_theme.text, self.add_new_theme
            )
        )

    def add_new_theme(self, new_theme: str):
        """
        add_new_theme:
            Adds a new theme to the database.
        """
        # add_theme transfers the word to the database
        add_theme(new_theme)
        # themes_from_db retrieves themes from the database.
        self.spinner.values = themes_from_db()
        self.spinner.text = themes_from_db()[-1]

        self.popup_new_theme.dismiss()

    def click_button_add_note(self, word: str, translate: str):
        """
        click_button_add_note:
            Adds a new note to the database.
        """
        # save_word_and_translate transfers the word and translations to the database.
        save_word_and_translate(word, translate)
        self.text_input_word.text = ""
        self.text_input_translate.text = ""
        # range_notes displays the word and translation in the grid layout.
        self.range_notes(spinner=None, name_theme=None)
        self.scrollview_for_notes.scroll_y = 0

    def range_notes(self, spinner, name_theme: str):
        """
        range_notes:
            Displays notes for the user in a table.
        """
        self.gridlayout.clear_widgets()
        # Output_notes if the theme is not empty outputs a list of words and translations
        # from the selected theme, if the empty function is not executed.
        self.notes = output_notes()
        if self.notes != None:
            for word in self.notes:
                self.buttons_notes = Button(
                    font_size=sp(18),
                    text=word,
                    halign="center",
                    size_hint_y=None,
                    background_color=[0, 0, 0, 0],
                    background_normal="",
                )
                self.buttons_notes.height = self.scrollview_for_notes.height / 8
                self.buttons_notes.text_size = (self.button_text(), None)
                self.gridlayout.add_widget(self.buttons_notes)
                # start_timer_for_notes calls a bubble if the button is held down for more than 1 second.
                self.buttons_notes.bind(on_press=self.start_timer_for_notes)
                # stop_timer_for_notes cancels the start_timer_for_notes event if
                # the button has not been pressed for more than one second.
                self.buttons_notes.bind(on_release=self.stop_timer_for_notes)
        else:
            return
        self.gridlayout.bind(minimum_height=self.gridlayout.setter("height"))
        self.scrollview_for_notes.scroll_y = 1

    def button_text(self):
        """
        button_text:
            Defines the width of the gridlayout column for the button text.
        """
        text_size_x = int((self.gridlayout.size[0] / 2) - 4)
        return text_size_x

    # <functions for notes>

    def start_timer_for_notes(self, button):
        """
        start_timer_for_notes:
            Starts a timer for one second if the button is pressed and performs the entered function.
        """
        # Clock.schedule_once causes a bubble if the button has been pressed for more than 1 second.
        Clock.schedule_once(self.show_bubble_for_notes, 1)
        self.button_note = button

    def stop_timer_for_notes(self, button):
        """
        stop_timer_for_notes:
            Stops the timer if the button has not been pressed for one second
            and cancels the execution of the entered function.
        """
        # Clock.unschedule cancels the bubble call if the button has been pressed for less than 1 second.
        Clock.unschedule(self.show_bubble_for_notes)

    def show_bubble_for_notes(self, second):
        """
        show_bubble_for_notes:
            Calls a bubble to rename or delete notes.
        """
        modalview_notes = DictBubble(
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.4, "y": 0.88},
            size_hint_min_x=200,
            overlay_color=[0, 0, 0, 0],
        )
        modalview_notes.bubble.show_arrow = False
        modalview_notes.open()
        # word_translate selects which word from the list was selected and adds its pair to it.
        self.word, self.translate = word_translate(self.button_note.text, self.notes)
        button1_rename = modalview_notes.button_rename
        # rename_for_note opens a window where you can change the selected word and translation.
        button1_rename.bind(on_press=self.rename_for_note)
        button_delete = modalview_notes.button_delete
        # remove_for_note brings up a window in which you can remove the entered word and translation.
        button_delete.bind(on_press=self.remove_for_note)

    def rename_for_note(self, bubble):
        """
        rename_for_note:
            Causes a popup to rename the note.
        """
        self.popup_rename_note = RenameNotesPopup(
            title="Renaming a note",
            title_size=sp(18),
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            word=self.word,
            translate=self.translate,
        )
        self.popup_rename_note.open()
        button = self.popup_rename_note.button_update
        # fields_empty checks that fields are not left empty.
        button.bind(
            on_press=lambda pres: fields_empty(
                self.popup_rename_note.text_input_word.text,
                self.popup_rename_note.text_input_translate.text,
                self.rename_note,
            )
        )

    def rename_note(self, up_word: str, up_translate: str):
        """
        `up_word` -> `update_word`\n
        `up_translate` -> `update_translate`\n
        rename_note:
            Rename the selected note.

        """
        # update_note updates the word and translation that were selected and changed in the text fields.
        update_note(up_word, up_translate, self.word, self.translate)
        # range_notes displays the word and translation in the grid layout.
        position_note = self.scrollview_for_notes.scroll_y
        self.range_notes(spinner=None, name_theme=None)
        self.scrollview_for_notes.scroll_y = position_note
        self.popup_rename_note.dismiss()

    def remove_for_note(self, bubble):
        """
        remove_for_note:
            Causes a popup to remove the note.
        """
        popup = DeleteNotePopup(
            title="Deleting a note",
            title_size=sp(18),
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            word=self.word,
            translate=self.translate,
        )
        popup.open()
        button = popup.button_delete
        # remove_note removes the selected word and translation.
        button.bind(on_press=self.remove_note)

    def remove_note(self, button):
        """
        remove_note:
            Deletes the selected note.
        """
        # Delete_note deletes the selected word and translation from the database.
        delete_note(self.word, self.translate)
        # range_notes displays the word and translation in the grid layout.
        position_note = self.scrollview_for_notes.scroll_y
        self.range_notes(spinner=None, name_theme=None)
        self.scrollview_for_notes.scroll_y = position_note

    # </functions for notes>

    # <function for thems>

    def start_timer_for_themes(self, spinner):
        """
        start_timer_for_themes:
            Starts a timer for one second if the button is pressed and performs the entered function.
        """
        # Clock.schedule_once causes a bubble if the button has been pressed for more than 1 second.
        Clock.schedule_once(self.show_bubble_for_theme, 1)

    def stop_timer_for_theme(self, spinner):
        """
        stop_timer_for_theme:
            Stops the timer if the button has not been pressed for one second
            and cancels the execution of the entered function.
        """
        Clock.unschedule(self.show_bubble_for_theme)
        # if self.close_spiner is not None cancels the opening of the spinner.
        if self.close_spiner is not None:
            self.spinner.is_open = True

    def show_bubble_for_theme(self, spinner):
        """
        show_bubble_for_theme:
            Calls a bubble to rename or delete theme.
        """
        modalview_theme = DictBubble(
            size_hint=(0.2, 0.08),
            pos_hint={"y": 0.7},
            size_hint_min_x=200,
            overlay_color=[0, 0, 0, 0],
        )
        modalview_theme.center_x = self.floatlayout.width / 2
        modalview_theme.open()

        button_rename = modalview_theme.button_rename
        button_delete = modalview_theme.button_delete
        # rename_for_theme opens a window where you can change the selected theme.
        button_rename.bind(on_press=self.rename_for_theme)
        # remove_for_theme opens a window where you can remove the selected theme.
        button_delete.bind(on_press=self.remove_for_theme)
        self.close_spiner = True
        modalview_theme.on_dismiss = self.modal_dismiss

    def modal_dismiss(self):
        """
        modal_dismiss:
            Executed when the bubble closes and allows the spinner to open.
        """
        self.close_spiner = None

    def rename_for_theme(self, bubble):
        """
        rename_for_theme:
            Causes a popup to rename the theme.
        """
        self.popup_rename_theme = RenamePopup(
            title="Renaming a theme",
            title_size=sp(18),
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            name_theme=self.spinner.text,
        )
        self.popup_rename_theme.open()
        button = self.popup_rename_theme.button_update
        # check_themes checks whether the field is empty and whether there are no similar themes.
        button.bind(
            on_press=lambda pres: check_themes(
                self.popup_rename_theme.text_input_rename_theme.text, self.rename_theme
            )
        )

    def rename_theme(self, up_theme: str):
        """
        `up_theme` -> `update_theme`\n
        rename_theme:
            Rename the selected theme.
        """
        # index_theme assigns an index to the selected topic.
        index_theme = themes_from_db().index(f"{self.spinner.text}")
        # update_theme updates the selected theme.
        update_theme(up_theme)
        # themes_from_db retrieves themes from the database.
        self.spinner.values = themes_from_db()
        self.spinner.text = themes_from_db()[index_theme]

        self.popup_rename_theme.dismiss()

    def remove_for_theme(self, bubble):
        """
        remove_for_theme:
            Causes a popup to remove the theme.
        """
        popup = DeletePopup(
            title="Deleting a theme",
            title_size=sp(18),
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            name_theme=self.spinner.text,
        )
        popup.open()
        button = popup.button_delete
        # remove_theme removes the selected topic.
        button.bind(on_press=self.remove_theme)

    def remove_theme(self, button):
        """
        remove_theme:
            Deletes the selected theme.
        """
        # delete_notes deletes all words from the theme.
        delete_notes()
        # delete_theme deletes the selected theme.
        delete_theme()
        # themes_from_db retrieves themes from the database.
        self.spinner.values = themes_from_db()
        self.spinner.text_autoupdate = True
        if not self.spinner.text:
            self.spinner.text = "Create a theme"

    # </function for thems>

    def update_scroll_views(self, button):
        """
        update_scroll_views:
            Executed when you go to the theme page and open all scroll views in their initial positions.
        """
        self.scrollview.scroll_y = 1
        self.scrollview_for_notes.scroll_y = 1

    def on_enter(self):
        """
        on_enter:
            Executed when the user enters the check screen.
        """
        if themes_from_db():
            self.spinner.values = themes_from_db()


sm.add_widget(PageThemes(name="pageThemes"))
