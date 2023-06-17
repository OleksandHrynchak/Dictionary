from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from Frontend.moduls import RoundedButton
from Database.database_operations import *


class AddThemePopup(Popup):
    def __init__(self, **kwargs):
        super(AddThemePopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_name_theme = Label(
            text="Enter a theme name:",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.85},
        )
        self.floatlayout.add_widget(self.label_name_theme)

        self.text_input_theme = TextInput(
            hint_text="Theme name",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=18,
            halign="center",
            size_hint=(0.8, 0.15),
            pos_hint={"x": 0.1, "y": 0.5},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
            multiline=False,
        )
        self.floatlayout.add_widget(self.text_input_theme)

        self.button_add = RoundedButton(
            text="Add theme",  # Add a word
            font_size=20,
            size_hint=(0.75, 0.2),
            pos_hint={"x": 0.125, "y": 0.1},
        )
        self.floatlayout.add_widget(self.button_add)


class DeletePopup(Popup):
    def __init__(self, name_theme, **kwargs):
        super(DeletePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_delete = Label(
            text="Delete theme:",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_delete)

        self.label_theme = Label(
            text=f"{name_theme}",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.60},
        )
        self.floatlayout.add_widget(self.label_theme)

        self.button_delete = RoundedButton(
            text="Delete",
            font_size=20,
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_delete)

        self.button_delete.bind(on_press=self.dismiss)


class RenamePopup(Popup):
    def __init__(self, name_theme, **kwargs):
        super(RenamePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_rename = Label(
            text="Edit theme:",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.80},
        )
        self.floatlayout.add_widget(self.label_rename)

        self.label_theme = Label(
            text=f"{name_theme}",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_theme)

        self.text_input_rename_theme = TextInput(
            text=f"{name_theme}",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=18,
            halign="center",
            size_hint=(0.8, 0.15),
            pos_hint={"x": 0.1, "y": 0.4},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
            multiline=False,
        )
        self.floatlayout.add_widget(self.text_input_rename_theme)

        self.button_update = RoundedButton(
            text="Save",
            font_size=20,
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_update)


class DeleteNotePopup(Popup):
    def __init__(self, word, translate, **kwargs):
        super(DeleteNotePopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_delete = Label(
            text="Delete note:",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_delete)

        self.label_theme = Label(
            text=f"{word} - {translate}",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.60},
        )
        self.floatlayout.add_widget(self.label_theme)

        self.button_delete = RoundedButton(
            text="Delete",
            font_size=20,
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_delete)

        self.button_delete.bind(on_press=self.dismiss)


class RenameNotesPopup(Popup):
    def __init__(self, word, translate, **kwargs):
        super(RenameNotesPopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_footnote = Label(
            text="Edit note:",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.80},
        )
        self.floatlayout.add_widget(self.label_footnote)

        self.label_notes = Label(
            text=f"{word} - {translate}",
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_notes)

        self.text_input_word = TextInput(
            text=word,
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=18,
            halign="center",
            size_hint=(0.38, 0.15),
            pos_hint={"x": 0.1, "y": 0.4},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
            multiline=False,
        )
        self.floatlayout.add_widget(self.text_input_word)

        self.text_input_translate = TextInput(
            text=translate,
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=18,
            halign="center",
            size_hint=(0.38, 0.15),
            pos_hint={"x": 0.5, "y": 0.4},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
            multiline=False,
        )
        self.floatlayout.add_widget(self.text_input_translate)

        self.button_update = RoundedButton(
            text="Save",
            font_size=20,
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_update)


class ErrorPopup(Popup):
    def __init__(self, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_warning = Label(
            text=("One of the fields is not filled"),
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.65},
        )
        self.floatlayout.add_widget(self.label_warning)

        self.button_agree = RoundedButton(
            text="OK",
            font_size=20,
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_agree)

        self.button_agree.bind(on_press=self.dismiss)


class BackPopup(Popup):
    def __init__(self, **kwargs):
        super(BackPopup, self).__init__(**kwargs)
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_warning = Label(
            text=("Save settings changes?"),
            font_size="18",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.65},
        )
        self.floatlayout.add_widget(self.label_warning)

        self.button_agree = RoundedButton(
            text="OK",
            font_size=20,
            size_hint=(0.38, 0.15),
            pos_hint={"x": 0.1, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_agree)

        self.button_cancel = RoundedButton(
            text="Cancel",
            font_size=20,
            size_hint=(0.38, 0.15),
            pos_hint={"x": 0.5, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_cancel)


class DictBubble(ModalView):
    def __init__(self, **kwargs):
        super(DictBubble, self).__init__(**kwargs)
        self.bubble = Bubble(orientation="horizontal")

        layout = BoxLayout(orientation="horizontal")

        self.button_rename = BubbleButton(text="Rename")
        self.button_rename.bind(on_press=self.dismiss)

        self.button_delete = BubbleButton(text="Delete")
        self.button_delete.bind(on_press=self.dismiss)

        layout.add_widget(self.button_rename)
        layout.add_widget(self.button_delete)

        self.bubble.add_widget(layout)
        self.add_widget(self.bubble)


class RightAnswerPopup(Popup):
    def __init__(self, **kwargs):
        super(RightAnswerPopup, self).__init__(**kwargs)
        self.auto_dismiss = False
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.button = RoundedButton(
            text="Next",
            font_size=20,
            size_hint=(0.62, 0.2),
            pos_hint={"x": 0.196, "y": 0.13},
        )
        self.floatlayout.add_widget(self.button)

        self.button.bind(on_press=self.dismiss)


class WrongAnswerPopup(Popup):
    def __init__(self, correct_word, **kwargs):
        super(WrongAnswerPopup, self).__init__(**kwargs)
        self.auto_dismiss = False
        self.floatlayout = FloatLayout()

        self.content = self.floatlayout

        self.label_incorrect_word = Label(
            text=f"{correct_word}",
            font_size=20,
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
            color=(1, 0.51, 0.58, 1),
        )
        self.floatlayout.add_widget(self.label_incorrect_word)

        self.button = RoundedButton(
            text="Next",
            font_size=20,
            size_hint=(0.62, 0.2),
            pos_hint={"x": 0.196, "y": 0.13},
        )
        self.floatlayout.add_widget(self.button)

        self.button.bind(on_press=self.dismiss)


def popup_empty():
    popup = ErrorPopup(
        title="The field is not filled",
        title_size=18,
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()


def popup_same_theme():
    popup = ErrorPopup(
        title="Repetition error",
        title_size=18,
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "This theme already exists"


def popup_settings_error():
    popup = ErrorPopup(
        title="Settings error",
        title_size=18,
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "Сheckbox is not selected"
