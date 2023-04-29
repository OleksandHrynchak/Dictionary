from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar

from Frontend.background import *
from Frontend.moduls import RoundedButton, DarkenedGridLayout

from Backend.switching import *


class PageStartTwo (Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        floatlayout.add_widget(RoundedButton(
            text="<--",
            on_press=lambda x: set_screen('menu'),
            font_size=20,
            size_hint=(.15, .08),
            pos_hint={'x': .04, 'y': .89},
        ))
        floatlayout.add_widget(ProgressBar(
            size_hint=(.8, .2),
            pos_hint={'x': .1, 'y': .70}
        ))
        floatlayout.add_widget(Label(
            text="Слова",  # Word
            font_size='20',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .65}
        ))
        floatlayout.add_widget(TextInput(
            hint_text='Введіть переклад',  # Enter the translation
            hint_text_color=[.55, .55, .55, 1],
            font_size='20',
            size_hint=(.8, .2),
            pos_hint={'x': .1, 'y': .30},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1]
        ))
        floatlayout.add_widget(RoundedButton(
            text="Далі",  # Next
            font_size=20,
            size_hint=(.6, .10),
            pos_hint={'x': .2, 'y': .07},
        ))

        self.add_widget(self.root)
        self.add_widget(floatlayout)


sm.add_widget(PageStartTwo(name='pageStartTwo'))
