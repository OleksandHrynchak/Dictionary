from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import sp

from Frontend.background import KV
from Frontend.moduls import RoundedButton
from Backend.switching import page_selection, set_screen, sm


class Menu(Screen):
    """
    Menu:
        Class inherited from `Screen`,\n
        which represents the main menu screen of the application.
    """

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        # Main layout.
        floatlayout = FloatLayout()
        # Background.
        self.root = Builder.load_string(KV)
        # page_selection displays the screen that was selected in the settings.
        self.button_start = RoundedButton(
            text="Start",
            font_size=sp(20),
            size_hint=(0.7, 0.08),
            pos_hint={"x": 0.15, "y": 0.34},
            on_press=page_selection,
        )
        floatlayout.add_widget(self.button_start)

        # set_screen opens the selected screen
        self.button_setings = RoundedButton(
            text="Settings",
            on_press=lambda x: set_screen("pageSettings"),
            font_size=sp(20),
            size_hint=(0.7, 0.08),
            pos_hint={"x": 0.15, "y": 0.22},
        )
        floatlayout.add_widget(self.button_setings)
        # set_screen opens the selected screen
        self.button_theme = RoundedButton(
            text="Thems",
            on_press=lambda x: set_screen("pageThemes"),
            font_size=sp(20),
            size_hint=(0.7, 0.08),
            pos_hint={"x": 0.15, "y": 0.1},
        )
        floatlayout.add_widget(self.button_theme)

        self.add_widget(self.root)
        self.add_widget(floatlayout)


sm.add_widget(Menu(name="menu"))
