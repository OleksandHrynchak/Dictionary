from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from Frontend.moduls import RoundedButton

from Database.database_operations import *


class AddThemePopup(Popup):
    def __init__(self, **kwargs):
        super(AddThemePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.lable_name_theme = Label(
            text="Введіть назву теми:",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .85}
        )
        self.floatlayout.add_widget(self.lable_name_theme)

        self.text_input_theme = TextInput(
            hint_text='Назва теми',
            hint_text_color=[.55, .55, .55, 1],
            font_size=18,
            halign="center",
            size_hint=(.8, .15),
            pos_hint={'x': .1, 'y': .5},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1],
            multiline=False
        )
        self.floatlayout.add_widget(self.text_input_theme)

        self.add_button = RoundedButton(
            text="Додати тему",  # Add a word
            font_size=20,
            size_hint=(.75, .2),
            pos_hint={'x': .125, 'y': .1}
        )
        self.floatlayout.add_widget(self.add_button)


class DeletePopup(Popup):
    def __init__(self, name_theme, **kwargs):
        super(DeletePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.lable_delete = Label(
            text="Видалити тему:",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .70}
        )
        self.floatlayout.add_widget(self.lable_delete)

        self.lable_theme = Label(
            text=f"{name_theme}",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .60}
        )
        self.floatlayout.add_widget(self.lable_theme)

        self.button_delete = RoundedButton(
            text="Видалити",
            font_size=20,
            size_hint=(.75, .18),
            pos_hint={'x': .125, 'y': .08}
        )
        self.floatlayout.add_widget(self.button_delete)

        self.button_delete.bind(on_press=self.dismiss)


class RenamePopup(Popup):
    def __init__(self, name_theme, **kwargs):
        super(RenamePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.lable_rename = Label(
            text="Редагувати тему:",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .80}
        )
        self.floatlayout.add_widget(self.lable_rename)

        self.lable_theme = Label(
            text=f"{name_theme}",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .70}
        )
        self.floatlayout.add_widget(self.lable_theme)

        self.text_input = TextInput(
            text=name_theme,
            hint_text_color=[.55, .55, .55, 1],
            font_size=18,
            halign="center",
            size_hint=(.8, .15),
            pos_hint={'x': .1, 'y': .4},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1],
            multiline=False
        )
        self.floatlayout.add_widget(self.text_input)

        self.button_update = RoundedButton(
            text="Зберегти",
            font_size=20,
            size_hint=(.75, .18),
            pos_hint={'x': .125, 'y': .08}
        )
        self.floatlayout.add_widget(self.button_update)

        # self.button_update.bind(on_press=self.dismiss)


class DeleteNotePopup(Popup):
    def __init__(self, word, translate, **kwargs):
        super(DeleteNotePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.lable_delete = Label(
            text="Видалити запис:",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .70}
        )
        self.floatlayout.add_widget(self.lable_delete)

        self.lable_theme = Label(
            text=f"{word} - {translate}",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .60}
        )
        self.floatlayout.add_widget(self.lable_theme)

        self.button_delete = RoundedButton(
            text="Видалити",
            font_size=20,
            size_hint=(.75, .18),
            pos_hint={'x': .125, 'y': .08}
        )
        self.floatlayout.add_widget(self.button_delete)

        self.button_delete.bind(on_press=self.dismiss)


class RenameNotesPopup(Popup):
    def __init__(self, word, translate, ** kwargs):
        super(RenameNotesPopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.lable_footnote = Label(
            text="Редагувати запис:",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .80}
        )
        self.floatlayout.add_widget(self.lable_footnote)

        self.lable_notes = Label(
            text=f"{word} - {translate}",
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .70}
        )
        self.floatlayout.add_widget(self.lable_notes)

        self.text_input_word = TextInput(
            text=word,
            hint_text_color=[.55, .55, .55, 1],
            font_size=18,
            halign="center",
            size_hint=(.38, .15),
            pos_hint={'x': .1, 'y': .4},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1],
            multiline=False
        )
        self.floatlayout.add_widget(self.text_input_word)

        self.text_input_translate = TextInput(
            text=translate,
            hint_text_color=[.55, .55, .55, 1],
            font_size=18,
            halign="center",
            size_hint=(.38, .15),
            pos_hint={'x': .5, 'y': .4},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1],
            multiline=False
        )
        self.floatlayout.add_widget(self.text_input_translate)

        self.button_update = RoundedButton(
            text="Зберегти",
            font_size=20,
            size_hint=(.75, .18),
            pos_hint={'x': .125, 'y': .08}
        )
        self.floatlayout.add_widget(self.button_update)

        # self.button_update.bind(on_press=self.dismiss)


class ErrorPopup(Popup):
    def __init__(self, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.lable_warning = Label(
            text=("Одне з полів не заповнено"),
            font_size='18',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .65}
        )
        self.floatlayout.add_widget(self.lable_warning)

        self.button_agree = RoundedButton(
            text="Гаразд",
            font_size=20,
            size_hint=(.75, .18),
            pos_hint={'x': .125, 'y': .08}
        )
        self.floatlayout.add_widget(self.button_agree)

        self.button_agree.bind(on_press=self.dismiss)


class DictBubble(ModalView):
    def __init__(self, **kwargs):
        super(DictBubble, self).__init__(**kwargs)
        self.bubble = Bubble(orientation="horizontal")

        self.button_rename = BubbleButton(text="Rename")
        self.button_rename.bind(on_press=self.dismiss)

        self.button_delete = BubbleButton(text="Delete")
        self.button_delete.bind(on_press=self.dismiss)

        self.bubble.add_widget(self.button_rename)
        self.bubble.add_widget(self.button_delete)
        self.add_widget(self.bubble)
