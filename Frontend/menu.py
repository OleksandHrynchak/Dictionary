from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout


from Frontend.background import *
from Frontend.moduls import RoundedButton
from Backend.switching import *


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)

        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        self.button_start = RoundedButton(
            text="Start",
            font_size=20,
            size_hint=(0.7, 0.08),
            pos_hint={"x": 0.15, "y": 0.34},
        )
        floatlayout.add_widget(self.button_start)
        self.button_start.bind(on_press=page_selection)

        self.button_setings = RoundedButton(
            text="Settings",
            font_size=20,
            size_hint=(0.7, 0.08),
            pos_hint={"x": 0.15, "y": 0.22},
        )
        floatlayout.add_widget(self.button_setings)
        self.button_setings.bind(on_press=lambda x: set_screen("pageSettings"))

        self.button_theme = RoundedButton(
            text="Thems",
            font_size=20,
            size_hint=(0.7, 0.08),
            pos_hint={"x": 0.15, "y": 0.1},
        )
        floatlayout.add_widget(self.button_theme)
        self.button_theme.bind(on_press=lambda x: set_screen("pageTemes"))

        self.add_widget(self.root)
        self.add_widget(floatlayout)


sm.add_widget(Menu(name="menu"))
