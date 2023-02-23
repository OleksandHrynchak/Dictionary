from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

from backfon import *

from Backend.switching import set_screen, sm


class PageStartOne (Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        floatlayout.add_widget(Button(
            text="<--",
            on_press=lambda x: set_screen('menu'),
            font_size=20,
            size_hint=(.15, .08),
            pos_hint={'x': .04, 'y': .89},
            background_color=[.0, .84, .64],
            background_normal=''
        ))
        floatlayout.add_widget(ProgressBar(
            size_hint=(.8, .2),
            pos_hint={'x': .1, 'y': .70}))
        floatlayout.add_widget(Label(
            text="Слова",  # Words
            font_size='20',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .65}
        ))
        floatlayout.add_widget(Label(
            text="Переклад",  # Examples
            font_size='20',
            size_hint=(1, 0),
            pos_hint={'x': 0, 'y': .45}
        ))
        floatlayout.add_widget(Button(
            text="Далі",
            font_size=20,
            size_hint=(.6, .10),
            pos_hint={'x': .2, 'y': .07},
            background_color=[.0, .84, .64],
            background_normal=''
        ))

        self.add_widget(self.root)
        self.add_widget(floatlayout)


sm.add_widget(PageStartOne(name='pageStartOne'))
