from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import sp

from Frontend.moduls import RoundedButton


class AddThemePopup(Popup):
    """
    AddThemePopup:
        class inherited from `Popup`.\n
        which contains a textinput label and a button.\n
        used to add a theme to the database.
    """

    def __init__(self, **kwargs):
        super(AddThemePopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_name_theme = Label(
            text="Enter a theme name:",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.85},
        )
        self.floatlayout.add_widget(self.label_name_theme)

        self.text_input_theme = TextInput(
            hint_text="Theme name",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(18),
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
            font_size=sp(20),
            size_hint=(0.75, 0.2),
            pos_hint={"x": 0.125, "y": 0.1},
        )
        self.floatlayout.add_widget(self.button_add)


class DeletePopup(Popup):
    """
    DeletePopup:
        class inherited from `Popup`.\n
        which contains a label with a warning about deletion
        and a label that indicates the theme that will be deleted and a button.\n
        additionally accepts the name of the theme `name_theme`,
        used to notify when the selected theme is deleted.
    """

    def __init__(self, name_theme, **kwargs):
        super(DeletePopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_delete = Label(
            text="Delete theme:",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_delete)

        self.label_theme = Label(
            text=f"{name_theme}",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.60},
        )
        self.floatlayout.add_widget(self.label_theme)

        self.button_delete = RoundedButton(
            text="Delete",
            font_size=sp(20),
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_delete)

        self.button_delete.bind(on_press=self.dismiss)


class RenamePopup(Popup):
    """
    RenamePopup:
        class inherited from `Popup`.\n
        which contains a label with a warning about renaming and a label indicating the theme to be renamed,
        a text input containing the name of the theme that can be changed, and a button to change the theme name.\n
        additionally takes the theme name `name_theme`,
        used to notify about the renaming of the selected theme.
    """

    def __init__(self, name_theme, **kwargs):
        super(RenamePopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_rename = Label(
            text="Edit theme:",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.80},
        )
        self.floatlayout.add_widget(self.label_rename)

        self.label_theme = Label(
            text=f"{name_theme}",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_theme)

        self.text_input_rename_theme = TextInput(
            text=f"{name_theme}",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(18),
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
            font_size=sp(20),
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_update)


class DeleteNotePopup(Popup):
    """
    DeleteNotePopup:
        class inherited from `Popup`,\n
        which contains a delete warning label and a label with the word and translation
        to delete and a button to delete the note.\n
        additionally accepts the name of the word `word` and the translation `translate`,
        used to notify when the selected note is deleted.
    """

    def __init__(self, word, translate, **kwargs):
        super(DeleteNotePopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_delete = Label(
            text="Delete note:",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_delete)

        self.label_theme = Label(
            text=f"{word} - {translate}",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.60},
        )
        self.floatlayout.add_widget(self.label_theme)

        self.button_delete = RoundedButton(
            text="Delete",
            font_size=sp(20),
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_delete)

        self.button_delete.bind(on_press=self.dismiss)


class RenameNotesPopup(Popup):
    """
    RenameNotesPopup:
        class inherited from `Popup`,\n
        which contains a renaming warning label and a label with a word and translation for renaming
        a textinput with a typed word that can be changed a textinput with a translation
        that can be changed and a button to rename a note.\n
        additionally accepts the name of the word `word` and the translation `translate`,
        used to notify when the selected note has been renamed.
    """

    def __init__(self, word, translate, **kwargs):
        super(RenameNotesPopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_footnote = Label(
            text="Edit note:",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.80},
        )
        self.floatlayout.add_widget(self.label_footnote)

        self.label_notes = Label(
            text=f"{word} - {translate}",
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
        )
        self.floatlayout.add_widget(self.label_notes)

        self.text_input_word = TextInput(
            text=word,
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(18),
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
            font_size=sp(18),
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
            font_size=sp(20),
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_update)


class ErrorPopup(Popup):
    """
    ErrorPopup:
        class inherited from `Popup`,\n
        which contains an error warning label and an OK button.\n
        used to notify when a field is not filled.
    """

    def __init__(self, **kwargs):
        super(ErrorPopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_warning = Label(
            text=("One of the fields is not filled"),
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.65},
        )
        self.floatlayout.add_widget(self.label_warning)

        self.button_agree = RoundedButton(
            text="OK",
            font_size=sp(20),
            size_hint=(0.75, 0.18),
            pos_hint={"x": 0.125, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_agree)

        self.button_agree.bind(on_press=self.dismiss)


class BackPopup(Popup):
    """
    BackPopup:
        class inherited from `Popup`,\n
        which contains a warning about saving settings and an OK button.\n
        used to notify when the user wants to leave the page without saving the settings.
    """

    def __init__(self, **kwargs):
        super(BackPopup, self).__init__(**kwargs)

        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_warning = Label(
            text=("Save settings changes?"),
            font_size=sp(18),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.65},
        )
        self.floatlayout.add_widget(self.label_warning)

        self.button_agree = RoundedButton(
            text="OK",
            font_size=sp(20),
            size_hint=(0.38, 0.15),
            pos_hint={"x": 0.1, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_agree)

        self.button_cancel = RoundedButton(
            text="Cancel",
            font_size=sp(20),
            size_hint=(0.38, 0.15),
            pos_hint={"x": 0.5, "y": 0.08},
        )
        self.floatlayout.add_widget(self.button_cancel)


class DictBubble(ModalView):
    """
    DictBubble:
        class inherited from `ModalView`,\n
        which contains a rename button and a delete button.\n
        used to call the rename or delete windows when the user wants to rename or delete a note or theme.
    """

    def __init__(self, **kwargs):
        super(DictBubble, self).__init__(**kwargs)

        self.bubble = Bubble(orientation="horizontal")
        self.box_layout = BoxLayout(orientation="horizontal")

        self.button_rename = BubbleButton(
            text="Rename",
            font_size=sp(18),
            halign="center",
        )
        self.button_rename.bind(on_press=self.dismiss)

        self.button_delete = BubbleButton(
            text="Delete",
            font_size=sp(18),
            halign="center",
        )
        self.button_delete.bind(on_press=self.dismiss)

        self.box_layout.add_widget(self.button_rename)
        self.box_layout.add_widget(self.button_delete)

        self.bubble.add_widget(self.box_layout)
        self.add_widget(self.bubble)


class RightAnswerPopup(Popup):
    """
    RightAnswerPopup:
        class inherited from `Popup`,\n
        which contains a button.\n
        used to alert the user to the correct answer.
    """

    def __init__(self, **kwargs):
        super(RightAnswerPopup, self).__init__(**kwargs)

        self.auto_dismiss = False
        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.button = RoundedButton(
            text="Next",
            font_size=sp(20),
            size_hint=(0.62, 0.2),
            pos_hint={"x": 0.196, "y": 0.13},
        )
        self.floatlayout.add_widget(self.button)

        self.button.bind(on_press=self.dismiss)


class WrongAnswerPopup(Popup):
    """
    WrongAnswerPopup:
        class inherited from `Popup`,\n
        which contains a button.\n
        used to notify the user of an wrong answer.
    """

    def __init__(self, correct_word, **kwargs):
        super(WrongAnswerPopup, self).__init__(**kwargs)

        self.auto_dismiss = False
        self.floatlayout = FloatLayout()
        self.content = self.floatlayout

        self.label_incorrect_word = Label(
            text=f"{correct_word}",
            font_size=sp(20),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.70},
            color=(1, 0.51, 0.58, 1),
        )
        self.floatlayout.add_widget(self.label_incorrect_word)

        self.button = RoundedButton(
            text="Next",
            font_size=sp(20),
            size_hint=(0.62, 0.2),
            pos_hint={"x": 0.196, "y": 0.13},
        )
        self.floatlayout.add_widget(self.button)

        self.button.bind(on_press=self.dismiss)


def popup_empty():
    """
    popup_empty:
        title="The field is not filled"
    """
    popup = ErrorPopup(
        title="The field is not filled",
        title_size=sp(18),
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()


def popup_same_theme():
    """
    popup_same_theme:
        title="Repetition error"\n
        text="This theme already exists"
    """
    popup = ErrorPopup(
        title="Repetition error",
        title_size=sp(18),
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "This theme already exists"


def popup_settings_error():
    """
    popup_same_theme:
        title="Settings error"\n
        text="Checkbox is not selected"
    """
    popup = ErrorPopup(
        title="Settings error",
        title_size=sp(18),
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "Checkbox is not selected"


def popup_create_theme():
    """
    popup_create_theme:
        title="Theme is not created"\n
        text="Please create a theme."
    """
    popup = ErrorPopup(
        title="Theme is not created",
        title_size=sp(18),
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "Please create a theme."


def popup_selecte_theme():
    """
    popup_create_theme:
        title="Theme is not selected"\n
        text="Please selecte a theme."
    """
    popup = ErrorPopup(
        title="Theme is not selected",
        title_size=sp(18),
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "Please selecte a theme."


def popup_selecte_theme():
    """
    popup_create_theme:
        title="Settings error"\n
        text="Please add an record to the theme"
    """
    popup = ErrorPopup(
        title="Subject does not contain any records",
        title_size=sp(18),
        size_hint=(0.8, 0.6),
        pos_hint={"x": 0.1, "y": 0.2},
        separator_height=3,
        separator_color=[0.0, 0.84, 0.64],
    )
    popup.open()
    popup.label_warning.text = "Please add an record to the theme."
