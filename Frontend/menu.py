from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


from Backend.switching import *
from Frontend.backfon import *
from Frontend.moduls import RoundedButton, DarkenedGridLayout


class Menu(Screen):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        self.buttonstart = RoundedButton(
            text="Cтарт",  # Start
            on_press=one_or_two,  # перша чи друга сторінка
            font_size=20,
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .34},
        )
        floatlayout.add_widget(self.buttonstart)

        floatlayout.add_widget(RoundedButton(
            text="Налаштування",  # Settings
            on_press=lambda x: set_screen('pageSetings'),
            font_size=20,
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .22},
        ))
        floatlayout.add_widget(RoundedButton(
            text="Теми",  # Thems
            on_press=lambda x: set_screen('pageTemes'),
            font_size=20,
            size_hint=(.7, .08),
            pos_hint={'x': .15, 'y': .1},
        ))

        self.add_widget(self.root)
        self.add_widget(floatlayout)


sm.add_widget(Menu(name='menu'))
