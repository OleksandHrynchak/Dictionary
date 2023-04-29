from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView

from Frontend.background import *
from Frontend.moduls import RoundedButton, DarkenedGridLayout

from Backend.switching import *
from Database.database_operations import themes_from_db


class PageSetings(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        relativelayout = RelativeLayout()
        floatlayout = FloatLayout(size_hint_y=1)
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation='horizontal',
            size_hint=[.7, .30],
            pos_hint={'x': .15, 'y': .7}
        )
        scrollview = ScrollView(
            size_hint=(1, .7),
            pos_hint={'x': 0, 'y': .16}
        )
        self.root = Builder.load_string(KV)
# --------------------------------------------------------------------------------------
        spinner = Spinner(
            text='Список тем',  # List of themes
            font_size=20,
            size_hint=(.7, .3),
            pos_hint={'x': .15, 'y': .7},
            values=themes_from_db(),
        )
        spinner.dropdown_cls.max_height = spinner.height * 2+2*2
# -------------------------------------------------------------------------------------
        relativelayout.add_widget(RoundedButton(
            text="<--",
            on_press=lambda x: set_screen('menu'),
            font_size=20,
            size_hint=(.15, .08),
            pos_hint={'x': .04, 'y': .89},
        ))
        relativelayout.add_widget(RoundedButton(
            text="Зберегти",  # Save
            font_size=20,
            size_hint=(.6, .08),
            pos_hint={'x': .2, 'y': .04},
        ))
# ___________________________________________________________________________________________________________
        self.checkbox_page_one = CheckBox(
            group="page_start",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .21, 'y': .75},
            active=True
        )
        floatlayout.add_widget(self.checkbox_page_one)
        self.checkbox_page_one.bind(active=self.on_checkbox_active)

        floatlayout.add_widget(Label(
            text="Перевірка",  # Check
            font_size=20,
            size_hint=[0.05, 0.06],
            pos_hint={'x': .50, 'y': .75}
        ))
# ___________________________________________________________________________________________________________
        self.checkbox_page_two = CheckBox(
            group="page_start",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .21, 'y': .65},
            active=False
        )
        floatlayout.add_widget(self.checkbox_page_two)
        self.checkbox_page_two.bind(active=self.on_checkbox_active)

        floatlayout.add_widget(Label(
            text="Повторення",  # Repetition
            font_size=20,
            size_hint=[0.05, 0.06],
            pos_hint={'x': .51, 'y': .65}
        ))
# ___________________________________________________________________________________________________________
        self.checkbox_word = CheckBox(
            size_hint=[0.05, 0.06],
            pos_hint={'x': .21, 'y': .55},
        )
        floatlayout.add_widget(self.checkbox_word)

        floatlayout.add_widget(Label(
            text="Eng ---> Ua",
            font_size=20,
            size_hint=[0.05, 0.06],
            pos_hint={'x': .499, 'y': .55}
        ))
# ___________________________________________________________________________________________________________
        self.checkbox_translate = CheckBox(
            size_hint=[0.05, 0.06],
            pos_hint={'x': .21, 'y': .45}
        )
        floatlayout.add_widget(self.checkbox_translate)

        floatlayout.add_widget(Label(
            text="Ua ---> Eng",
            font_size=20,
            size_hint=[0.05, 0.06],
            pos_hint={'x': .499, 'y': .45}
        ))
# ___________________________________________________________________________________________________________
        self.checkbox_random = CheckBox(
            group="choice",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .21, 'y': .35}
        )
        floatlayout.add_widget(self.checkbox_random)

        floatlayout.add_widget(Label(
            text="Рандомно",  # Randomly
            font_size=20,
            size_hint=[0.05, 0.06],
            pos_hint={'x': .498, 'y': .35}
        ))
# ___________________________________________________________________________________________________________
        self.checkbox_numb = CheckBox(
            group="choice",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .21, 'y': .25}
        )
        floatlayout.add_widget(self.checkbox_numb)

        floatlayout.add_widget(Label(
            text="По порядку",  # Successively
            font_size=20,
            size_hint=[0.05, 0.06],
            pos_hint={'x': .505, 'y': .25}
        ))
# ___________________________________________________________________________________________________________

        self.slidertime = Slider(
            min=1,
            max=60,
            step=1,
            orientation='horizontal',
            size_hint=[.7, .05],
            pos_hint={'x': .15, 'y': .13},
            value_track=True,
            value_track_color=[.41, 1, .96, 1]
        )
        floatlayout.add_widget(self.slidertime)
        self.slidertime.bind(value=self.slider_value)

        self.textinputtime = TextInput(
            input_filter='int',
            multiline=False,
            hint_text='min',
            hint_text_color=[.55, .55, .55, 1],
            font_size=25,
            halign="center",
            size_hint=(.3, .09),
            pos_hint={'x': .35, 'y': .01},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1],
        )
        floatlayout.add_widget(self.textinputtime)

        self.textinputtime.bind(text=self.text_number)  # комент
        self.textinputtime.bind(text=self.textinput_bugs)  # комент

        boxlayout.add_widget(spinner)
        floatlayout.add_widget(boxlayout)
        scrollview.add_widget(floatlayout)
        relativelayout.add_widget(scrollview)
        self.add_widget(self.root)
        self.add_widget(relativelayout)

    def slider_value(self, instance, value):  # комент
        self.textinputtime.text = str(value)

    def text_number(self, instance, sec):  # комент
        self.slidertime.value = int('0' + sec)

    def textinput_bugs(self, instance, sec):  # комент
        max_sec = 60
        if int('0' + sec) > max_sec:
            self.textinputtime.text = str(max_sec)

    def on_checkbox_active(self, checkbox, value):
        # print(self)
        # print(checkbox)
        print(value)
        if value:
            if self.checkbox_page_one.active:
                self.checkbox_page_two.active = False
            elif self.checkbox_page_two.active:
                self.checkbox_page_one.active = False
        # print(self.checkbox_page_one.active)
        # print(self.checkbox_page_two.active)


sm.add_widget(PageSetings(name='pageSetings'))
