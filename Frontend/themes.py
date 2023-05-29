from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.clock import Clock


from Frontend.background import *
from Frontend.moduls import RoundedButton, DarkenedGridLayout
from Frontend.popups import *
from Backend.switching import *
from Database.database_operations import (
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
            # scroll_y=1
        )
        # Scroll view to display words in gridlayout.
        self.scrollview_for_notes = ScrollView(
            size_hint=(0.7, 0.6), pos_hint={"x": 0.15, "y": 0.22}
        )
        # background.
        self.root = Builder.load_string(KV)
        # --------------------------------------------------------------------------------------
        self.spinner = Spinner(
            text="Select a themes",
            font_size=18,
            size_hint=(0.7, 0.30),
            pos_hint={"x": 0.15, "y": 0.7},
            values=themes_from_db(),
        )
        # id_theme defines id theme.
        self.spinner.bind(text=id_theme)
        # range_notes displays the notes of the given theme.
        self.spinner.bind(text=self.range_notes)
        # start_timer_for_themes calls a bubble if the button is held down for more than 1 second.
        self.spinner.bind(on_press=self.start_timer_for_themes)
        # stop_timer_for_themes cancels the start_timer_for_notes event if
        # the button has not been pressed for more than one second.
        self.spinner.bind(on_release=self.stop_timer_for_themes)
        self.close_spiner = None
        self.spinner.dropdown_cls.max_height = self.spinner.height * 2 + 5
        # -------------------------------------------------------------------------------------
        self.relativelayout.add_widget(
            RoundedButton(
                text="<--",
                on_press=lambda page: set_screen("menu"),
                on_release=self.update_scroll_views,
                font_size=20,
                size_hint=(0.16, 0.08),
                pos_hint={"x": 0.04, "y": 0.89},
            )
        )

        self.floatlayout.add_widget(
            RoundedButton(
                text="Add a theme",
                on_press=self.popup_add_themes,
                font_size=20,
                size_hint=(0.7, 0.07),
                pos_hint={"x": 0.15, "y": 0.92},
            )
        )

        self.text_input_word = TextInput(
            hint_text="Word",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size="18",
            halign="center",
            size_hint=(0.38, 0.08),
            pos_hint={"x": 0.1, "y": 0.10},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        self.floatlayout.add_widget(self.text_input_word)

        self.text_input_translate = TextInput(
            hint_text="Translate",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size="18",
            halign="center",
            size_hint=(0.38, 0.08),
            pos_hint={"x": 0.5, "y": 0.10},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        self.floatlayout.add_widget(self.text_input_translate)

        self.button_add_note = RoundedButton(
            text="Add a word",
            font_size=20,
            size_hint=(0.6, 0.07),
            pos_hint={"x": 0.2, "y": 0},
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
        self.popup_new_theme = AddThemePopup(
            title="Add a theme",
            title_size=18,
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
        )
        self.popup_new_theme.open()
        button_add = self.popup_new_theme.add_button
        # check_themes checks whether the field is empty and whether there are no similar themes.
        button_add.bind(
            on_press=lambda pres: check_themes(
                self.popup_new_theme.text_input_theme.text, self.add_new_theme
            )
        )

    def add_new_theme(self, new_theme):
        """
        add_new_theme:
            add_theme transfers the word to the database
            themes_from_db retrieves themes from the database
        """
        add_theme(new_theme)
        self.spinner.values = themes_from_db()
        self.spinner.text = themes_from_db()[-1]
        self.popup_new_theme.dismiss()

    def click_button_add_note(self, word, translate):
        """
        click_button_add_note:
            save_word_and_translate transfers the word and translations to the database.
            range_notes displays the word and translation in the grid layout.
        """
        save_word_and_translate(word, translate)
        self.text_input_word.text = ""
        self.text_input_translate.text = ""
        self.range_notes(spinner=None, name_theme=None)
        self.scrollview_for_notes.scroll_y = 0

    def range_notes(self, spinner, name_theme):
        """
        range_notes:
            output_notes outputs a list of words and translations from the selected theme.
        """
        self.gridlayout.clear_widgets()
        self.notes = output_notes()
        for word in self.notes:
            self.buttons_notes = Button(
                font_size=18,
                text=word,
                height=50,
                size_hint_y=None,
                text_size=(None, None),
                background_color=[0, 0, 0, 0],
                background_normal="",
            )
            self.gridlayout.add_widget(self.buttons_notes)
            # start_timer_for_notes calls a bubble if the button is held down for more than 1 second.
            self.buttons_notes.bind(on_press=self.start_timer_for_notes)
            # stop_timer_for_notes cancels the start_timer_for_notes event if
            # the button has not been pressed for more than one second.
            self.buttons_notes.bind(on_release=self.stop_timer_for_notes)
        self.gridlayout.bind(minimum_height=self.gridlayout.setter("height"))
        self.scrollview_for_notes.scroll_y = 1

    # start----------------function for notes
    def start_timer_for_notes(self, button):
        """
        start_timer_for_notes:
            Clock.schedule_once causes a bubble if the button has been pressed for more than 1 second.
        """
        Clock.schedule_once(self.show_bubble_for_notes, 1)
        self.button_note = button

    def stop_timer_for_notes(self, button):
        """
        stop_timer_for_notes:
            Clock.unschedule cancels the bubble call if the button has been pressed for less than 1 second.
        """
        Clock.unschedule(self.show_bubble_for_notes)

    def show_bubble_for_notes(self, second):
        modalview_notes = DictBubble(
            size_hint=(None, None),
            pos_hint={"x": 0.4, "y": 0.88},
            size=[140, 50],
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
        self.popup_rename_note = RenameNotesPopup(
            title="Renaming a note",
            title_size=18,
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

    def rename_note(self, up_word, up_translate):
        """
        rename_note:
            update_note updates the word and translation that
                were selected and changed in the text fields.
            range_notes displays the word and translation in the grid layout.

        """
        update_note(up_word, up_translate, self.word, self.translate)
        self.range_notes(spinner=None, name_theme=None)
        self.popup_rename_note.dismiss()

    def remove_for_note(self, bubble):
        popup = DeleteNotePopup(
            title="Deleting a note",
            title_size=18,
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

    def remove_note(self, delete):
        """
        remove_note:
            delete_note deletes the selected word and translation from the database.
            range_notes displays the word and translation in the grid layout.
        """
        delete_note(self.word, self.translate)
        self.range_notes(spinner=None, name_theme=None)

    # end----------------function for notes

    # start ----------------function for thems

    def start_timer_for_themes(self, spinner):
        """
        start_timer_for_themes:
            Clock.schedule_once causes a bubble if the button has been pressed for more than 1 second.
        """
        Clock.schedule_once(self.show_bubble_for_themes, 1)

    def stop_timer_for_themes(self, spinner):
        """
        stop_timer_for_themes:
            Clock.unschedule cancels the bubble call if the button has been pressed for less than 1 second.
            (if self.close_spiner is not None) cancels the opening of the spinner.
        """
        Clock.unschedule(self.show_bubble_for_themes)
        if self.close_spiner is not None:
            self.spinner.is_open = True

    def show_bubble_for_themes(self, spinner):
        modalview_theme = DictBubble(
            size_hint=(None, None),
            pos_hint={"y": 0.7},
            size=[140, 50],
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
            executed when the bubble closes and allows the spinner to open.
        """
        self.close_spiner = None

    def rename_for_theme(self, bubble):
        self.popup_rename_theme = RenamePopup(
            title="Renaming a theme",
            title_size=18,
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
                self.popup_rename_theme.text_input.text, self.rename_theme
            )
        )

    def rename_theme(self, update):
        """
        rename_theme:
            index_theme assigns an index to the selected topic.
            update_theme update_theme updates the selected theme.
            themes_from_db retrieves themes from the database.
        """
        index_theme = themes_from_db().index(f"{self.spinner.text}")
        update_theme(update)
        self.spinner.values = themes_from_db()
        self.spinner.text = themes_from_db()[index_theme]
        self.popup_rename_theme.dismiss()

    def remove_for_theme(self, bubble):
        popup = DeletePopup(
            title="Deleting a theme",
            title_size=18,
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

    def remove_theme(self, delete):
        """
        remove_theme:
            delete_notes deletes all words from the theme.
            delete_theme deletes the selected theme.
            themes_from_db retrieves themes from the database.

        """
        delete_notes()
        delete_theme()
        self.spinner.values = themes_from_db()
        self.spinner.text_autoupdate = True

    # end ----------------function for thems

    def update_scroll_views(self, button):
        """
        update_scroll_views:
            executed when you go to the theme page and open all scroll views in their initial positions.
        """
        self.scrollview.scroll_y = 1
        self.scrollview_for_notes.scroll_y = 1


sm.add_widget(PageThemes(name="pageTemes"))
