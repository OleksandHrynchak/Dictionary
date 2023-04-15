from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle


class RoundedButton(Button):
    def __init__(self, **kwargs):
        super(RoundedButton, self).__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.background_normal = ''
        with self.canvas.before:
            Color(.0, .84, .64, 1)
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
                radius=[8]
            )
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class DarkenedGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(DarkenedGridLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 0, .5)
            self.rect = RoundedRectangle(
                size=self.size,
                pos=self.pos,
            )
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
