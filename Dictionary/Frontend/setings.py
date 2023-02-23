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

from backfon import *

from Backend.switching import *


class PageSetings(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        relativelayout = RelativeLayout()
        floatlayout = FloatLayout(size_hint_y=1.2)
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation='horizontal',
            size_hint=[.7, .23],
            pos_hint={'x': .15, 'y': .77}
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
            # values=('Тема0', 'Тема1', 'Тема2', 'Тема3', 'Тема4',
            #        'Тема5', 'Тема6', 'Тема7', 'Тема8', 'Тема9'),
            sync_height=True,
            size_hint=(.7, .3),
            pos_hint={'x': .15, 'y': .7}
        )
        max = 2
        spinner.dropdown_cls.max_height = spinner.height * max + max * 2
# -------------------------------------------------------------------------------------
        relativelayout.add_widget(Button(
            text="<--",
            on_press=lambda x: set_screen('menu'),
            font_size=20,
            size_hint=(.15, .08),
            pos_hint={'x': .04, 'y': .89},
            background_color=[.0, .84, .64],
            background_normal=''
        ))
        relativelayout.add_widget(Button(
            text="Зберегти",  # Save
            # on_press=set_screen('menu'),
            font_size=20,
            size_hint=(.6, .08),
            pos_hint={'x': .2, 'y': .04},
            background_color=[.0, .84, .64],
            background_normal=''
        ))
# ___________________________________________________________________________________________________________
        self.checkboxpageone = CheckBox(
            group="page_start",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .2, 'y': .80})
        floatlayout.add_widget(self.checkboxpageone)
        self.checkboxpageone.bind(active=page_one)

        floatlayout.add_widget(Label(
            text="Перевірка",  # Check
            font_size='18',
            size_hint=[0.05, 0.06],
            pos_hint={'x': .45, 'y': .80}
        ))
# ___________________________________________________________________________________________________________
        self.checkboxpagetwo = CheckBox(
            group="page_start",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .2, 'y': .70},
        )
        floatlayout.add_widget(self.checkboxpagetwo)
        self.checkboxpagetwo.bind(active=page_two)

        floatlayout.add_widget(Label(
            text="Повторення",  # Repetition
            font_size='18',
            size_hint=[0.05, 0.06],
            pos_hint={'x': .45, 'y': .70}
        ))
# ___________________________________________________________________________________________________________
        checkboxeng = CheckBox(
            size_hint=[0.05, 0.06],
            pos_hint={'x': .2, 'y': .60},
        )
        floatlayout.add_widget(checkboxeng)

        floatlayout.add_widget(Label(
            text="Eng ---> Ua",
            font_size='18',
            size_hint=[0.05, 0.06],
            pos_hint={'x': .45, 'y': .60}
        ))
# ___________________________________________________________________________________________________________
        checkboxua = CheckBox(
            size_hint=[0.05, 0.06],
            pos_hint={'x': .2, 'y': .50}
        )
        floatlayout.add_widget(checkboxua)

        floatlayout.add_widget(Label(
            text="Ua ---> Eng",
            font_size='18',
            size_hint=[0.05, 0.06],
            pos_hint={'x': .45, 'y': .50}
        ))
# ___________________________________________________________________________________________________________
        checkboxrand = CheckBox(
            group="choice",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .2, 'y': .40}
        )
        floatlayout.add_widget(checkboxrand)

        floatlayout.add_widget(Label(
            text="Рандомно",  # Randomly
            font_size='18',
            size_hint=[0.05, 0.06],
            pos_hint={'x': .45, 'y': .40}
        ))
# ___________________________________________________________________________________________________________
        checkboxnumb = CheckBox(
            group="choice",
            size_hint=[0.05, 0.06],
            pos_hint={'x': .2, 'y': .30}
        )
        floatlayout.add_widget(checkboxnumb)

        floatlayout.add_widget(Label(
            text="По порядку",  # Successively
            font_size='18',
            size_hint=[0.05, 0.06],
            pos_hint={'x': .45, 'y': .30}
        ))
# ___________________________________________________________________________________________________________

        self.slidertime = Slider(
            min=1,
            max=60,
            step=1,
            orientation='horizontal',
            size_hint=[.7, .05],
            pos_hint={'x': .15, 'y': .20},
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
            font_size='25',
            halign="center",
            size_hint=(.3, .08),
            pos_hint={'x': .35, 'y': .10},
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

    def text_number(self, instance, text):  # комент
        self.slidertime.value = int('0' + text)

    def textinput_bugs(self, instance, text):  # комент
        range_max = 60
        if int('0' + text) > range_max:
            self.textinputtime.text = str(range_max)


sm.add_widget(PageSetings(name='pageSetings'))
