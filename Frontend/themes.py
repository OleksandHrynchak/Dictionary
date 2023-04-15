from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.window import Window


from Frontend.backfon import *
from Frontend.moduls import RoundedButton, DarkenedGridLayout
from Frontend.popups import *

from Database.database_operations import (
    add_theme,
    themes_from_db,
    id_theme,
    save_word_and_translate,
    output_notes,
    update_theme,
    delete_theme,
    delete_words)

from Backend.switching import *


class PageThemes(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        relativelayout = RelativeLayout()
        self.floatlayout = FloatLayout(size_hint_y=1.4)
        self.gridlayout = DarkenedGridLayout(
            cols=2,
            size_hint_y=None,
            height=0
        )
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation='horizontal',
            size_hint=[.7, .19],
            pos_hint={'x': .15, 'y': .70}
        )
        # загальний скролвю
        scrollview = ScrollView(
            size_hint=(1, .8),
            pos_hint={'x': 0, 'y': .05}
        )
        # скролвю для виведеня слів в грідлояуті
        self.scrollview_for_notes = ScrollView(
            size_hint=(.7, .6),
            pos_hint={'x': .15, 'y': .22}
        )
        self.root = Builder.load_string(KV)

# --------------------------------------------------------------------------------------
        self.spinner = Spinner(
            text="Виберіть тему",  # Select a themes
            font_size=18,
            size_hint=(.7, .30),
            pos_hint={'x': .15, 'y': .7},
            values=themes_from_db(),
        )
        self.spinner.bind(text=id_theme)
        self.spinner.bind(text=self.range_notes)
        self.spinner.bind(on_press=self.start_timer_for_thems)
        self.spinner.bind(on_release=self.stop_timer_for_thems)
        self.close_spiner = None
        self.spinner.dropdown_cls.max_height = self.spinner.height * 2 + 5
# -------------------------------------------------------------------------------------
        relativelayout.add_widget(RoundedButton(
            text="<--",
            on_press=lambda x: set_screen('menu'),
            font_size=20,
            size_hint=(.16, .08),
            pos_hint={'x': .04, 'y': .89},
        ))

        self.floatlayout.add_widget(RoundedButton(
            text="Додати тему",  # Add a theme
            on_press=self.popup_add_themes,
            font_size=20,
            size_hint=(.7, .07),
            pos_hint={'x': .15, 'y': .92},
        ))

        self.text_input_word = TextInput(
            hint_text='Слово',  # Word
            hint_text_color=[.55, .55, .55, 1],
            font_size='18',
            halign="center",
            size_hint=(.38, .08),
            pos_hint={'x': .1, 'y': .10},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1]
        )
        self.floatlayout.add_widget(self.text_input_word)

        self.text_input_translate = TextInput(
            hint_text='Переклад',  # Translate
            hint_text_color=[.55, .55, .55, 1],
            font_size='18',
            halign="center",
            size_hint=(.38, .08),
            pos_hint={'x': .5, 'y': .10},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1]
        )
        self.floatlayout.add_widget(self.text_input_translate)

        self.button_add_note = RoundedButton(
            text="Додати слово",  # Add a word
            font_size=20,
            size_hint=(.6, .07),
            pos_hint={'x': .2, 'y': 0},
        )
        self.floatlayout.add_widget(self.button_add_note)
        self.button_add_note.bind(on_press=lambda a: fields_empty(self.text_input_word.text,
                                                                  self.text_input_translate.text,
                                                                  self.click_button_add_note))

        self.scrollview_for_notes.add_widget(self.gridlayout)
        boxlayout.add_widget(self.spinner)
        self.floatlayout.add_widget(self.scrollview_for_notes)
        self.floatlayout.add_widget(boxlayout)
        scrollview.add_widget(self.floatlayout)
        relativelayout.add_widget(scrollview)
        self.add_widget(self.root)
        self.add_widget(relativelayout)

    def popup_add_themes(self, button):
        self.popup_new_theme = AddThemePoput(
            title='Додайте тему',
            title_size=18,
            size_hint=(.9, .7),
            pos_hint={'x': .05, 'y': .15},
            separator_height=3,
            separator_color=[.0, .84, .64],
        )
        self.popup_new_theme.open()
        self.button = self.popup_new_theme.add_button
        self.button.bind(on_press=lambda pres:
                         field_empty(self.popup_new_theme.text_input_theme.text, self.add_new_theme))

    def add_new_theme(self, text_value):
        add_theme(text_value)
        self.spinner.values = themes_from_db()
        self.spinner.text = themes_from_db()[-1]
        self.popup_new_theme.dismiss()

    def click_button_add_note(self, button):
        word = self.text_input_word.text
        translate = self.text_input_translate.text

        save_word_and_translate(word, translate)

        self.text_input_word.text = ''
        self.text_input_translate.text = ''

        self.range_notes(spinner=None, name_theme=None)

        self.scrollview_for_notes.scroll_y = 0

    def range_notes(self, spinner, name_theme):
        self.gridlayout.clear_widgets()
        self.notes = output_notes()
        for word in self.notes:
            self.button_notes = Button(
                font_size=18,
                text=word,
                height=50,
                size_hint_y=None,
                text_size=(None, None),
                background_color=[0, 0, 0, 0],
                background_normal=''
            )
            self.gridlayout.add_widget(self.button_notes)
            self.button_notes.bind(on_press=self.start_timer_for_notes)
            self.button_notes.bind(on_release=self.stop_timer_for_notes)
        self.gridlayout.bind(
            minimum_height=self.gridlayout.setter('height'))
        self.scrollview_for_notes.scroll_y = 1

# start----------------function for notes
    def start_timer_for_notes(self, button):
        Clock.schedule_once(self.show_bubble_for_notes, 1)

    def stop_timer_for_notes(self, button):
        Clock.unschedule(self.show_bubble_for_notes)

    def show_bubble_for_notes(self, second):
        modalview_notes = DictBubble(
            size_hint=(None, None),
            pos_hint={'y': .7},
            size=[140, 50],
            overlay_color=[0, 0, 0, 0]
        )
        # modalview.pos = self.button_add_note.pos
        # print(self)
        # print(self.button_notes)
        # print(button)
        #modalview_notes.pos = self.gridlayout.to_window(*self.gridlayout.pos)
        modalview_notes.open()
        button1_rename = modalview_notes.button_rename
        button_delete = modalview_notes.button_delete
        # button1_rename.bind(on_press=self.rename)
        # button_delete.bind(on_press=self.remove)

# end----------------function for notes

# start ----------------function for thems

    def start_timer_for_thems(self, spinner):
        Clock.schedule_once(self.show_bubble_for_themes, 1)

    def stop_timer_for_thems(self, spinner):
        Clock.unschedule(self.show_bubble_for_themes)
        if self.close_spiner is not None:
            self.spinner.is_open = True

    def show_bubble_for_themes(self, spinner):
        modalview_theme = DictBubble(
            size_hint=(None, None),
            pos_hint={'y': .7},
            size=[140, 50],
            overlay_color=[0, 0, 0, 0]
        )
        modalview_theme.center_x = self.floatlayout.width / 2
        modalview_theme.open()
        button1_rename = modalview_theme.button_rename
        button_delete = modalview_theme.button_delete

        button1_rename.bind(on_press=self.rename_for_theme)
        button_delete.bind(on_press=self.remove_for_theme)

        self.close_spiner = True

        modalview_theme.on_dismiss = self.modal_dismiss

    def modal_dismiss(self):
        self.close_spiner = None

    def rename_for_theme(self, bubble):
        popup = RenamePopup(
            title="Перейменування теми",
            title_size=18,
            size_hint=(.9, .7),
            pos_hint={'x': .05, 'y': .15},
            separator_height=3,
            separator_color=[.0, .84, .64],
            name_theme=self.spinner.text
        )
        popup.open()
        button = popup.button_update
        button.bind(on_press=lambda pres:
                    self.rename_theme(popup.text_input.text))

    def rename_theme(self, update):
        index_theme = themes_from_db().index(f"{self.spinner.text}")
        update_theme(update)
        self.spinner.values = themes_from_db()
        self.spinner.text = themes_from_db()[index_theme]

    def remove_for_theme(self, bubble):
        popup = DeletePopup(
            title="Видаленя тему",
            title_size=18,
            size_hint=(.9, .7),
            pos_hint={'x': .05, 'y': .15},
            separator_height=3,
            separator_color=[.0, .84, .64],
            name_theme=self.spinner.text
        )
        popup.open()
        button = popup.button_delete
        button.bind(on_press=self.remove_theme)

    def remove_theme(self, delete):
        delete_words()
        delete_theme()
        self.spinner.values = themes_from_db()
        self.spinner.text_autoupdate = True

# end ----------------function for thems


sm.add_widget(PageThemes(name='pageTemes'))
