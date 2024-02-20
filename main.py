from kivymd.app import MDApp
from kivy.core.window import Window

from Frontend.menu import sm
from Frontend.repeat import sm
from Frontend.check import sm
from Frontend.settings import sm
from Frontend.themes import sm
from Database.SQLite3.database import create_database


class Dictionary(MDApp):
    """
    Dictionary:
        The main application class that inherits from `MDApp`.
    """

    def __init__(self, **kvargs):
        super(Dictionary, self).__init__(**kvargs)

    def build(self):
        """
        build:
            Method that returns the root widget of the application.
        """
        return sm

    def on_start(self):
        Window.softinput_mode = "below_target"


if __name__ == "__main__":
    Dictionary().run()
