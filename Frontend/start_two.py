from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

from Frontend.background import *
from Frontend.moduls import RoundedButton
from Frontend.popups import RightAnswerPopup, WrongAnswerPopup
from Backend.switching import *


class PageStartTwo(Screen):
    def __init__(self, **kwargs):
        super(PageStartTwo, self).__init__(**kwargs)
        floatlayout = FloatLayout()
        self.root = Builder.load_string(KV)

        floatlayout.add_widget(
            RoundedButton(
                text="<--",
                on_press=lambda x: set_screen("menu"),
                font_size=20,
                size_hint=(0.15, 0.08),
                pos_hint={"x": 0.04, "y": 0.89},
            )
        )

        time_max = int(call_settings()[8])
        self.progres_bar = ProgressBar(
            max=time_max,
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.75},
        )
        floatlayout.add_widget(self.progres_bar)

        self.index_notes = 0
        self.label_question = Label(
            text="Word",  # Word
            font_size="20",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.7},
        )
        floatlayout.add_widget(self.label_question)

        self.text_input_answer = TextInput(
            hint_text="Enter the answer",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size="20",
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.35},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        floatlayout.add_widget(self.text_input_answer)

        self.button_verify = RoundedButton(
            text="Verify",
            font_size=20,
            size_hint=(0.6, 0.08),
            pos_hint={"x": 0.2, "y": 0.07},
        )
        floatlayout.add_widget(self.button_verify)
        self.button_verify.bind(on_press=self.check_answer)

        self.add_widget(self.root)
        self.add_widget(floatlayout)

    def activete_notes(self):
        self.label_question.text = self.notes[self.index_notes]
        self.test = translation_pair(self.label_question.text, output_settings_notes())

    def change_notes(self, button):
        self.text_input_answer.text = ""
        self.index_notes += 1
        if self.index_notes >= len(self.notes):
            self.index_notes = 0

        self.label_question.text = self.notes[self.index_notes]
        self.test = translation_pair(self.label_question.text, output_settings_notes())

    def check_answer(self, button):
        if self.test == self.text_input_answer.text:
            self.popup_correct()
        else:
            self.popup_incorrect()

    def popup_correct(self):
        popup_right = RightAnswerPopup(
            title="Perfectly",
            title_size=20,
            title_color=(0, 0.84, 0.64, 1),
            size_hint=(1, 0.5),
            pos_hint={"x": 0, "y": 0},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            background_color=(1, 1, 1, 1),
        )
        popup_right.open()
        button = popup_right.button
        button.bind(on_press=self.change_notes)

    def popup_incorrect(self):
        popup_wrong = WrongAnswerPopup(
            title="Right answer:",
            title_size=20,
            title_color=(1, 0.51, 0.58, 1),
            size_hint=(1, 0.5),
            pos_hint={"x": 0, "y": 0},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            background_color=(1, 1, 1, 1),
            correct_word=self.test,
        )
        popup_wrong.open()
        button = popup_wrong.button
        button.bind(on_press=self.change_notes)

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


sm.add_widget(PageStartTwo(name="pageStartTwo"))
