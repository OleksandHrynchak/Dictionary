from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.metrics import sp


from Frontend.background import KV
from Frontend.moduls import RoundedButton
from Frontend.popups import RightAnswerPopup, WrongAnswerPopup
from Backend.switching import (
    set_screen,
    call_settings,
    translation_pair,
    output_settings_notes,
    random_or_successively,
    sm,
)


class PageCheck(Screen):
    """
    PageCheck:
        Class inherited from `Screen`,
        which presents a screen to test the knowledge of the selected theme.
    """

    def __init__(self, **kwargs):
        super(PageCheck, self).__init__(**kwargs)
        # Main layout.
        floatlayout = FloatLayout()
        # Background.
        self.root = Builder.load_string(KV)
        # set_screen opens the selected screen
        floatlayout.add_widget(
            RoundedButton(
                text="<--",
                on_press=lambda x: set_screen("menu"),
                font_size=sp(20),
                size_hint=(0.15, 0.08),
                pos_hint={"x": 0.04, "y": 0.89},
            )
        )

        self.progres_bar = ProgressBar(
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.75},
            max=1,
        )
        floatlayout.add_widget(self.progres_bar)

        self.index_notes = 0
        self.label_question = Label(
            text="Word",
            font_size=sp(20),
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.7},
        )
        floatlayout.add_widget(self.label_question)

        self.text_input_answer = TextInput(
            hint_text="Enter the answer",
            hint_text_color=[0.55, 0.55, 0.55, 1],
            font_size=sp(20),
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.35},
            foreground_color=[1, 1, 1, 1],
            background_color=[0.29, 0.29, 0.29],
            cursor_color=[1, 1, 1, 1],
        )
        floatlayout.add_widget(self.text_input_answer)

        self.button_verify = RoundedButton(
            text="Verify",
            font_size=sp(20),
            size_hint=(0.6, 0.08),
            pos_hint={"x": 0.2, "y": 0.07},
        )
        floatlayout.add_widget(self.button_verify)
        self.button_verify.bind(on_press=self.check_answer)

        self.add_widget(self.root)
        self.add_widget(floatlayout)

    def activete_notes(self):
        """
        activete_notes:
            Outputs the word and stores the answer to the given word.
        """
        self.label_question.text = self.notes[self.index_notes]
        # translation_pair outputs a pair to the given word.
        self.answer = translation_pair(
            self.label_question.text, output_settings_notes()
        )

    def change_notes(self, button):
        """
        change_notes:
            Clears the input field,sets the next word,
            if the list ends, then returns to the first word of the list and goes through again.
        """
        self.text_input_answer.text = ""
        self.index_notes += 1
        if self.index_notes >= len(self.notes):
            self.index_notes = 0

        self.label_question.text = self.notes[self.index_notes]
        self.answer = translation_pair(
            self.label_question.text, output_settings_notes()
        )

    def check_answer(self, button):
        """
        check_answer:
            Checks the answer with the saved one, if the answer matches,
            it displays a message about the correct answer, if it does not match,
            it displays a message that the answer is incorrect and displays the correct answer.
        """
        right_answer = self.answer.lower().replace(" ", "")
        answer_entered = self.text_input_answer.text.lower().replace(" ", "")
        if right_answer == answer_entered:
            self.popup_correct()
        else:
            self.popup_incorrect()

    def popup_correct(self):
        """
        popup_correct:
            Displays the text `Perfectly`.
        """
        popup_right = RightAnswerPopup(
            title="Perfectly",
            title_size=sp(20),
            title_color=(0, 0.84, 0.64, 1),
            size_hint=(1, 0.5),
            pos_hint={"x": 0, "y": 0},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            background_color=(1, 1, 1, 1),
        )
        popup_right.open()
        button = popup_right.button
        # change_notes clears the field and moves to the next word.
        button.bind(on_press=self.change_notes)

    def popup_incorrect(self):
        """
        popup_correct:
            Displays the text `Right answer` and the correct word.
        """
        popup_wrong = WrongAnswerPopup(
            title="Right answer:",
            title_size=sp(20),
            title_color=(1, 0.51, 0.58, 1),
            size_hint=(1, 0.5),
            pos_hint={"x": 0, "y": 0},
            separator_height=3,
            separator_color=[0.0, 0.84, 0.64],
            background_color=(1, 1, 1, 1),
            correct_word=self.answer,
        )
        popup_wrong.open()
        button = popup_wrong.button
        # change_notes clears the field and moves to the next word.
        button.bind(on_press=self.change_notes)

    def on_enter(self):
        """
        on_enter:
            Executed when the user enters the check screen.
        """
        # call_settings executes the saved settings.
        call_settings()
        # random_or_successively outputs the list according to saves.
        self.notes = random_or_successively()
        # update_stopwatch updates the timer value.
        self.stopwatch_event = Clock.schedule_interval(self.update_stopwatch, 1)
        self.activete_notes()

    def on_leave(self):
        """
        on_leave:
            Executed when the user exits the check screen.
        """
        Clock.unschedule(self.stopwatch_event)
        self.progres_bar.value = 0
        self.index_notes = 0

    def update_stopwatch(self, dt):
        """
        update_stopwatch:
            Updates the timer value, when the timer ends,
            returns the user to the menu screen.
        """
        need_second = call_settings()[8] * 60
        current_second = int(self.progres_bar.value * need_second)
        current_second += 1.001

        if current_second <= need_second:
            self.progres_bar.value = current_second / need_second
        else:
            self.progres_bar.value = 0
            self.stopwatch_event.cancel()
            # set_screen opens the selected screen
            set_screen("menu")


sm.add_widget(PageCheck(name="pageCheck"))
