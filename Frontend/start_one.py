from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

from Frontend.background import *
from Frontend.moduls import RoundedButton
from Backend.switching import *
from Database.database_operations import call_settings, output_settings_notes


class PageStartOne(Screen):
    def __init__(self, **kwargs):
        super(PageStartOne, self).__init__(**kwargs)
        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        self.button_back = RoundedButton(
            text="<--",
            on_press=lambda page: set_screen("menu"),
            font_size=20,
            size_hint=(0.15, 0.08),
            pos_hint={"x": 0.04, "y": 0.89},
        )
        floatlayout.add_widget(self.button_back)

        time_max = int(call_settings()[8])
        self.progres_bar = ProgressBar(
            max=time_max,
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.75},
        )
        floatlayout.add_widget(self.progres_bar)

        self.index_notes = 0
        self.label_question = Label(
            font_size="20",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.65},
        )
        floatlayout.add_widget(self.label_question)

        self.label_answer = Label(
            font_size="20",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.45},
        )
        floatlayout.add_widget(self.label_answer)

        self.button_next = RoundedButton(
            text="Next",
            font_size=20,
            size_hint=(0.6, 0.10),
            pos_hint={"x": 0.2, "y": 0.07},
        )
        floatlayout.add_widget(self.button_next)
        self.button_next.bind(on_press=self.change_notes)

        self.add_widget(self.root)
        self.add_widget(floatlayout)

    def change_notes(self, button):
        self.index_notes += 1
        if self.index_notes >= len(self.notes):
            self.index_notes = 0

        self.label_question.text = self.notes[self.index_notes]
        self.label_answer.text = translation_pair(
            self.label_question.text, output_settings_notes()
        )

    def activete_notes(self):
        self.label_question.text = self.notes[self.index_notes]
        self.label_answer.text = translation_pair(
            self.label_question.text, output_settings_notes()
        )

    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++stopwatch
    def on_enter(self):
        call_settings()
        self.notes = random_or_successively()
        self.stopwatch_event = Clock.schedule_interval(self.update_stopwatch, 1)
        self.activete_notes()

    def on_leave(self):
        Clock.unschedule(self.stopwatch_event)
        self.progres_bar.value = 0
        self.index_notes = 0

    def update_stopwatch(self, dt):
        need_second = call_settings()[8] * 60
        current_second = int(self.progres_bar.value * need_second)
        current_second += 1

        if current_second <= need_second:
            self.progres_bar.value = current_second / need_second
        else:
            self.progres_bar.value = 0
            self.stopwatch_event.cancel()
            set_screen("menu")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++stopwatch

sm.add_widget(PageStartOne(name="pageStartOne"))
