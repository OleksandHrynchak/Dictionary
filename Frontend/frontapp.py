from kivymd.app import MDApp

from menu import *
from start_one import *
from start_two import *
from setings import *
from themes import *

from Backend.switching import *


class Dictionary(MDApp):
    def __init__(self, **kvargs):
        super(Dictionary, self).__init__(**kvargs)

    def build(self):
        return sm


if __name__ == '__main__':
    Dictionary().run()
