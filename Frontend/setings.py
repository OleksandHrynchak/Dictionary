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


from Frontend.background import *
from Frontend.moduls import RoundedButton, CustomLabel
from Frontend.popups import *
from Backend.switching import *
from Database.database_operations import themes_from_db


class PageSettings(Screen):
    def __init__(self, **kwargs):
        super(PageSettings, self).__init__(**kwargs)
        relativelayout = RelativeLayout()
        floatlayout = FloatLayout()
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation="horizontal",
            size_hint=[0.7, 0.30],
            pos_hint={"x": 0.15, "y": 0.7},
        )
        gridlayout = GridLayout(
            cols=2,
            spacing=[20, 0],
            row_force_default=True,
            row_default_height=45,
            size_hint=[0.6, 0.5],
            pos_hint={"x": 0.2, "y": 0.37},
        )
        scrollview = ScrollView(
            size_hint=(1, 0.7),
            pos_hint={"x": 0, "y": 0.16},
        )
        self.root = Builder.load_string(KV)
        # --------------------------------------------------------------------------------------
        self.spinner = Spinner(
            text="List of themes",
            font_size=18,
            size_hint=(0.7, 0.3),
            pos_hint={"x": 0.15, "y": 0.7},
            values=themes_from_db(),
        )
        self.spinner.bind(text=id_settings_theme)
        self.spinner.dropdown_cls.max_height = self.spinner.height * 2 + 4
        # -------------------------------------------------------------------------------------
        relativelayout.add_widget(
            RoundedButton(
                text="<--",
                on_press=self.save_check,
                font_size=20,
                size_hint=(0.15, 0.08),
                pos_hint={"x": 0.04, "y": 0.89},
            )
        )
        relativelayout.add_widget(
            RoundedButton(
                text="Save",
                on_press=self.save_settings,
                font_size=20,
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
        gridlayout.add_widget(self.checkbox_check)
        self.checkbox_check.bind(on_press=self.force_checkbox_check)

        gridlayout.add_widget(
            CustomLabel(
                text="Check",
                font_size=20,
                height=40,
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_repeat = CheckBox(
            group="page_start",
            size=(20, 5),
            size_hint_x=None,
        )
        gridlayout.add_widget(self.checkbox_repeat)
        self.checkbox_repeat.bind(on_press=self.force_checkbox_check)

        gridlayout.add_widget(
            CustomLabel(
                text="Repeat",
                font_size=20,
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_word = CheckBox(
            size=(20, 5),
            size_hint_x=None,
        )
        gridlayout.add_widget(self.checkbox_word)

        gridlayout.add_widget(
            CustomLabel(
                text="Word",
                font_size=20,
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_translate = CheckBox(
            size=(20, 5),
            size_hint_x=None,
        )
        gridlayout.add_widget(self.checkbox_translate)

        gridlayout.add_widget(
            CustomLabel(
                text="Translate",
                font_size=20,
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_randomly = CheckBox(
            group="choice",
            size=(20, 5),
            size_hint_x=None,
        )
        gridlayout.add_widget(self.checkbox_randomly)
        self.checkbox_randomly.bind(on_press=self.force_checkbox_check)

        gridlayout.add_widget(
            CustomLabel(
                text="Randomly",
                font_size=20,
            )
        )
        # ___________________________________________________________________________________________________________
        self.checkbox_successively = CheckBox(
            group="choice",
            size=(20, 5),
            size_hint_x=None,
            active=True,
        )
        gridlayout.add_widget(self.checkbox_successively)
        self.checkbox_successively.bind(on_press=self.force_checkbox_check)

        gridlayout.add_widget(
            CustomLabel(
                text="Successively",
                font_size=20,
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
            font_size=25,
            halign="center",
            size_hint=(0.3, 0.09),
            pos_hint={"x": 0.35, "y": 0.01},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        floatlayout.add_widget(self.text_input_time)

        self.text_input_time.bind(text=self.text_input_number)  # комент
        self.text_input_time.bind(text=self.text_input_max_number)
        self.text_input_time.bind(text=self.text_input_min_number)  # комент

        boxlayout.add_widget(self.spinner)
        floatlayout.add_widget(gridlayout)
        floatlayout.add_widget(boxlayout)
        scrollview.add_widget(floatlayout)
        relativelayout.add_widget(scrollview)
        self.add_widget(self.root)
        self.add_widget(relativelayout)
        self.update_settings()

    def slider_value(self, spinner, value):
        self.text_input_time.text = str(value)

    def text_input_number(self, textinput, sec):
        self.slider_time.value = int("0" + sec)

    def text_input_max_number(self, textinput, sec):
        max_sec = 60
        if int("0" + sec) > max_sec:
            self.text_input_time.text = str(max_sec)

    def text_input_min_number(self, textinput, sec):
        min_sec = 1
        if int("0" + sec) < min_sec:
            self.text_input_time.text = str(min_sec)

    def force_checkbox_check(self, checkbox):
        if checkbox == self.checkbox_check:
            self.checkbox_repeat.active = not checkbox.active
        elif checkbox == self.checkbox_repeat:
            self.checkbox_check.active = not checkbox.active

        if checkbox == self.checkbox_randomly:
            self.checkbox_successively.active = not checkbox.active
        elif checkbox == self.checkbox_successively:
            self.checkbox_randomly.active = not checkbox.active

    def update_settings(self):
        self.spinner.text = call_settings()[1]
        self.checkbox_check.active = bool(call_settings()[2])
        self.checkbox_repeat.active = bool(call_settings()[3])
        self.checkbox_word.active = bool(call_settings()[4])
        self.checkbox_translate.active = bool(call_settings()[5])
        self.checkbox_randomly.active = bool(call_settings()[6])
        self.checkbox_successively.active = bool(call_settings()[7])
        self.text_input_time.text = str(call_settings()[8])

    def check_settings(self):
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
        if not self.checkbox_word.active and not self.checkbox_translate.active:
            popup_settings_error()
        else:
            change_save(self.check_settings())

    def save_check(self, button):
        if tuple(self.check_settings().values()) == call_settings()[1:]:
            set_screen("menu")
        else:
            self.popup_back()

    def popup_back(self):
        self.popup_choise = BackPopup(
            title="Warning",
            title_size=18,
            size_hint=(0.9, 0.7),
            pos_hint={"x": 0.05, "y": 0.15},
        )
        self.popup_choise.open()
        button_agree = self.popup_choise.button_agree
        button_agree.bind(on_press=self.save_close)
        button_cancel = self.popup_choise.button_cancel
        button_cancel.bind(on_press=self.back_close)

    def save_close(self, button):
        self.save_settings(button)
        set_screen("menu")
        self.update_settings()
        self.popup_choise.dismiss()

    def back_close(self, button):
        set_screen("menu")
        self.update_settings()
        self.popup_choise.dismiss()


sm.add_widget(PageSettings(name="pageSettings"))
