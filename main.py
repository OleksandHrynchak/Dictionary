from kivymd.app import MDApp

from Frontend.menu import *
from Frontend.start_one import *
from Frontend.start_two import *
from Frontend.setings import *
from Frontend.themes import *
from Frontend.background import *

from Backend.switching import *


class Dictionary(MDApp):
    def __init__(self, **kvargs):
        super(Dictionary, self).__init__(**kvargs)

    def build(self):
        return sm


if __name__ == "__main__":
    Dictionary().run()
