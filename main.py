from kivymd.app import MDApp

from Frontend.menu import sm
from Frontend.start_one import sm
from Frontend.start_two import sm
from Frontend.setings import sm
from Frontend.themes import sm


class Dictionary(MDApp):
    def __init__(self, **kvargs):
        super(Dictionary, self).__init__(**kvargs)

    def build(self):
        return sm


if __name__ == "__main__":
    Dictionary().run()
