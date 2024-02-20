from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.metrics import sp


from Frontend.background import KV
from Frontend.moduls import RoundedButton, CustomLabel
from Frontend.popups import BackPopup, popup_settings_error
from Backend.switching import call_settings, set_screen, sm
from Database.SQLite3.database_operations import (
    themes_from_db,
    id_settings_theme,
    change_save,
)

# To work with Mysql, uncomment the import from the mysql folder and comment from SQLite 3.
# from Database.MySQL.database_operations import themes_from_db


class PageSettings(Screen):
    """
    PageSettings:
        Class inherited from `Screen`,\n
        which represents the screen for application settings.
    """

    def __init__(self, **kwargs):
        super(PageSettings, self).__init__(**kwargs)
        # Main layout.
        relativelayout = RelativeLayout()
        # layout for settings.
        floatlayout = FloatLayout()
        # Layout for a spinner.
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation="horizontal",
            size_hint=[0.7, 0.30],
            pos_hint={"x": 0.15, "y": 0.7},
        )
        # layout for checkboxes and their labels, is part of the settings.
        self.gridlayout = GridLayout(
            cols=2,
            spacing=[20, 0],
            row_force_default=True,
            row_default_height=50,
            size_hint=[0.6, 0.5],
            pos_hint={"x": 0.2, "y": 0.37},
        )
        # Main scroll view.
        self.scrollview = ScrollView(
            size_hint=(1, 0.7),
            pos_hint={"x": 0, "y": 0.16},
        )
        # Background.
        self.root = Builder.load_string(KV)
        # --------------------------------------------------------------------------------------
        self.spinner = Spinner(
            text="Select theme",
            font_size=sp(18),
            size_hint=(0.7, 0.3),
            pos_hint={"x": 0.15, "y": 0.7},
        )
        # id_settings_theme defines id theme.
        self.spinner.bind(text=id_settings_theme)
        self.spinner.dropdown_cls.max_height = self.spinner.height * 2 + 4
        # -------------------------------------------------------------------------------------
        relativelayout.add_widget(
            RoundedButton(
                text="<--",
                on_press=self.save_check,
                font_size=sp(20),
                size_hint=(0.15, 0.08),
                pos_hint={"x": 0.04, "y": 0.89},
            )
        )
        relativelayout.add_widget(
            RoundedButton(
                text="Save",
                on_press=self.save_settings,
                font_size=sp(20),
                size_hint=(0.6, 0.08),
                pos_hint={"x": 0.2, "y": 0.04},
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_check = CheckBox(
            group="page_start",
            size=(20, 5),
            size_hint_x=None,
            active=True,
        )
        self.gridlayout.add_widget(self.checkbox_check)
        # force_checkbox_check is responsible for ensuring that checkboxes do not remain unactivated.
        self.checkbox_check.bind(on_press=self.force_checkbox_check)

        self.gridlayout.add_widget(
            CustomLabel(
                text="Check",
                font_size=sp(20),
                height=40,
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_repeat = CheckBox(
            group="page_start",
            size=(20, 5),
            size_hint_x=None,
        )
        self.gridlayout.add_widget(self.checkbox_repeat)
        # force_checkbox_check is responsible for ensuring that checkboxes do not remain unactivated.
        self.checkbox_repeat.bind(on_press=self.force_checkbox_check)

        self.gridlayout.add_widget(
            CustomLabel(
                text="Repeat",
                font_size=sp(20),
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_word = CheckBox(
            size=(20, 5),
            size_hint_x=None,
        )
        self.gridlayout.add_widget(self.checkbox_word)

        self.gridlayout.add_widget(
            CustomLabel(
                text="Word",
                font_size=sp(20),
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_translate = CheckBox(
            size=(20, 5),
            size_hint_x=None,
        )
        self.gridlayout.add_widget(self.checkbox_translate)

        self.gridlayout.add_widget(
            CustomLabel(
                text="Translate",
                font_size=sp(20),
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_randomly = CheckBox(
            group="choice",
            size=(20, 5),
            size_hint_x=None,
        )
        self.gridlayout.add_widget(self.checkbox_randomly)
        # force_checkbox_check is responsible for ensuring that checkboxes do not remain unactivated.
        self.checkbox_randomly.bind(on_press=self.force_checkbox_check)

        self.gridlayout.add_widget(
            CustomLabel(
                text="Randomly",
                font_size=sp(20),
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_successively = CheckBox(
            group="choice",
            size=(20, 5),
            size_hint_x=None,
            active=True,
        )
        self.gridlayout.add_widget(self.checkbox_successively)
        # force_checkbox_check is responsible for ensuring that checkboxes do not remain unactivated.
        self.checkbox_successively.bind(on_press=self.force_checkbox_check)

        self.gridlayout.add_widget(
            CustomLabel(
                text="Successively",
                font_size=sp(18),
            )
        )
        # ___________________________________________________________________________________________________________

        self.slider_time = Slider(
            min=1,
            max=60,
            step=1,
            orientation="horizontal",
            size_hint=[0.7, 0.05],
            pos_hint={"x": 0.15, "y": 0.13},
            value_track=True,
            value_track_color=[0.41, 1, 0.96, 1],
        )
        floatlayout.add_widget(self.slider_time)
        self.slider_time.bind(value=self.slider_value)

        self.text_input_time = TextInput(
            input_filter="int",
            multiline=False,
            hint_text="min",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(25),
            halign="center",
            size_hint=(0.3, 0.09),
            pos_hint={"x": 0.35, "y": 0.01},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        floatlayout.add_widget(self.text_input_time)
        # txt_input_number passes the textinput value to the slider.
        self.text_input_time.bind(text=self.text_input_number)
        # text_input_max_number sets the maximum value of the input text.
        self.text_input_time.bind(text=self.text_input_max_number)
        # text_input_min_number sets the minimum value of the input text.
        self.text_input_time.bind(text=self.text_input_min_number)

        boxlayout.add_widget(self.spinner)
        floatlayout.add_widget(self.gridlayout)
        floatlayout.add_widget(boxlayout)
        self.scrollview.add_widget(floatlayout)
        relativelayout.add_widget(self.scrollview)
        self.add_widget(self.root)
        self.add_widget(relativelayout)

        if themes_from_db():
            self.spinner.values = themes_from_db()
            self.update_settings()

    def slider_value(self, spinner, value):
        """
        slider_value:
            Passes the value of the text input to the slider.
        """
        self.text_input_time.text = str(value)

    def text_input_number(self, text_input, sec: str):
        """
        text_input_number:
            Passes slider value to textinput.
        """
        self.slider_time.value = int("0" + sec)

    def text_input_max_number(self, textinput, sec: str):
        """
        text_input_max_number:
            Creates a limit of the maximum number for entering into the textinput.
        """
        max_sec = 60
        if int("0" + sec) > max_sec:
            self.text_input_time.text = str(max_sec)

    def text_input_min_number(self, textinput, sec: str):
        """
        text_input_min_number:
            Creates a limit on the minimum number to enter in textinput.
        """
        min_sec = 1
        if int("0" + sec) < min_sec:
            self.text_input_time.text = str(min_sec)

    def force_checkbox_check(self, checkbox):
        """
        force_checkbox_check:
            Is responsible for ensuring that the checkboxes do not remain unactivated,
            one of the checkboxes of the group must always be activated.
        """
        if checkbox == self.checkbox_check:
            self.checkbox_repeat.active = not checkbox.active
        elif checkbox == self.checkbox_repeat:
            self.checkbox_check.active = not checkbox.active

        if checkbox == self.checkbox_randomly:
            self.checkbox_successively.active = not checkbox.active
        elif checkbox == self.checkbox_successively:
            self.checkbox_randomly.active = not checkbox.active

    def update_settings(self):
        """
        update_settings:
            Updates all settings values.
        """
        self.spinner.text = call_settings()[1]
        self.checkbox_check.active = bool(call_settings()[2])
        self.checkbox_repeat.active = bool(call_settings()[3])
        self.checkbox_word.active = bool(call_settings()[4])
        self.checkbox_translate.active = bool(call_settings()[5])
        self.checkbox_randomly.active = bool(call_settings()[6])
        self.checkbox_successively.active = bool(call_settings()[7])
        self.text_input_time.text = str(call_settings()[8])

    def check_settings(self) -> dict:
        """
        check_settings:
            Reates a dictionary with the current setting values.
        """
        settings = {
            "theme": str(self.spinner.text),
            "verify": self.checkbox_check.active,
            "repetition": self.checkbox_repeat.active,
            "word": self.checkbox_word.active,
            "translate": self.checkbox_translate.active,
            "randomly": self.checkbox_randomly.active,
            "successively": self.checkbox_successively.active,
            "timer": int(self.text_input_time.text),
        }
        return settings

    def save_settings(self, button):
        """
        save_settings:
            Updates the settings in the database, checks whether one of
            the world or translate checkboxes is activated,
            if they are not activated, then displays a warning.
        """
        if not self.checkbox_word.active and not self.checkbox_translate.active:
            popup_settings_error()
        else:
            change_save(self.check_settings())

    def save_check(self, button):
        """
        save_check:
            Checks whether the settings are saved in the database.
        """
        if tuple(self.check_settings().values()) == call_settings()[1:]:
            # set_screen opens the selected screen
            set_screen("menu")
        else:
            self.popup_back()

    def popup_back(self):
        """
        popup_back:
            Causes a popup to exit the settings screen.
        """
        self.popup_choise = BackPopup(
            title="Warning",
            title_size=sp(18),
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
        )
        self.popup_choise.open()
        button_agree = self.popup_choise.button_agree
        # save_close saves the settings in the database and takes the user to the menu screen
        button_agree.bind(on_press=self.save_close)
        button_cancel = self.popup_choise.button_cancel
        # back_close takes the user to the menu screen without saving the settings to the database.
        button_cancel.bind(on_press=self.back_close)

    def save_close(self, button):
        """
        save_close:
            Saves the settings in the database, takes the user to the menu screen
            and turns off the message window.
        """
        self.save_settings(button)
        set_screen("menu")
        self.update_settings()
        self.popup_choise.dismiss()

    def back_close(self, button):
        """
        back_close:
            Does not save the settings in the database, takes the user to the menu screen
            and turns off the message window.
        """
        set_screen("menu")
        self.update_settings()
        self.popup_choise.dismiss()

    def on_enter(self):
        """
        on_enter:
            Executed when the user enters the settings screen.
        """

        call_settings()
        self.update_settings()
        if themes_from_db():
            self.spinner.values = themes_from_db()
        self.gridlayout.row_default_height = (self.scrollview.height * 0.64) / 6


sm.add_widget(PageSettings(name="pageSettings"))
