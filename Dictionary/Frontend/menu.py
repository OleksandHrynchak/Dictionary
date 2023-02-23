from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from backfon import *

from Backend.switching import *


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        self.buttonstart = Button(
            text="Cтарт",  # Start
            on_press=one_or_two,  # перша чи друга сторінка
            font_size=20,
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .34},
            background_color=[.0, .84, .64],
            background_normal=''
        )
        floatlayout.add_widget(self.buttonstart)

        floatlayout.add_widget(Button(
            text="Налаштування",  # Settings
            on_press=lambda x: set_screen('pageSetings'),
            font_size=20,
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .22},
            background_color=[.0, .84, .64],
            background_normal=''
        ))
        floatlayout.add_widget(Button(
            text="Теми",  # Thems
            on_press=lambda x: set_screen('pageTemes'),
            font_size=20,
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .1},
            background_color=[.0, .84, .64],
            background_normal=''
        ))

        self.add_widget(self.root)
        self.add_widget(floatlayout)


sm.add_widget(Menu(name='menu'))
