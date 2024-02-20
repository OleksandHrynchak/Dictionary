from kivy.lang import Builder
from kivy.clock import Clock

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.uix.button import Button
from kivy.metrics import sp


from Frontend.background import KV
from Frontend.moduls import RoundedButton
from Backend.switching import set_screen, translation_pair, random_or_successively, sm
from Database.SQLite3.database_operations import call_settings, output_settings_notes
from Voice.TTS import text_speach

# To work with Mysql, uncomment the import from the mysql folder and comment from SQLite 3.
# from Database.MySQL.database_operations import call_settings, output_settings_notes


class PageRepeat(Screen):
    """
    PageRepeat:
        Class inherited from `Screen`,
        which presents a screen to repeat the selected theme.
    """

    def __init__(self, **kwargs):
        super(PageRepeat, self).__init__(**kwargs)
        # Main layout.
        floatlayout = FloatLayout()
        # Background.
        self.root = Builder.load_string(KV)
        # set_screen opens the selected screen
        self.button_back = RoundedButton(
            text="<--",
            on_press=lambda page: set_screen("menu"),
            font_size=sp(20),
            size_hint=(0.15, 0.08),
            pos_hint={"x": 0.04, "y": 0.89},
        )
        floatlayout.add_widget(self.button_back)

        self.progres_bar = ProgressBar(
            size_hint=(0.8, 0.2),
            pos_hint={"x": 0.1, "y": 0.75},
            max=1,
        )
        floatlayout.add_widget(self.progres_bar)

        self.index_notes = 0
        self.label_question = Label(
            font_size=sp(20),
            halign="center",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.65},
        )
        floatlayout.add_widget(self.label_question)

        self.label_answer = Label(
            font_size=sp(20),
            halign="center",
            size_hint=(1, 0),
            pos_hint={"x": 0, "y": 0.45},
        )
        floatlayout.add_widget(self.label_answer)

        self.button_read = RoundedButton(
            text="Read",
            font_size=sp(20),
            size_hint=(0.6, 0.10),
            pos_hint={"x": 0.2, "y": 0.07},
        )
        floatlayout.add_widget(self.button_read)
        self.button_read.bind(on_press=self.voice_text)

        self.button_forward = Button(
            text="\\\n/",
            font_size=sp(30),
            size_hint=(0.2, 0.6),
            pos_hint={"x": 0.8, "y": 0.25},
            background_color=(0, 0, 0, 0),
        )
        floatlayout.add_widget(self.button_forward)
        self.button_forward.bind(on_press=self.change_notes)

        self.button_previous = Button(
            text="/\n\\",
            font_size=sp(30),
            size_hint=(0.2, 0.6),
            pos_hint={"x": 0, "y": 0.25},
            background_color=(0, 0, 0, 0),
        )
        floatlayout.add_widget(self.button_previous)
        self.button_previous.bind(on_press=self.previous_notes)

        self.add_widget(self.root)
        self.add_widget(floatlayout)

    def voice_text(self, button):
        """
        voice_text:
            Reads the word and the translation.
        """
        text_speach(self.label_question.text)
        text_speach(self.label_answer.text)

    def previous_notes(self, button):
        """
        previous_notes:
            When the button is pressed, changes the text of the question and answer labels one less index.
        """
        self.index_notes -= 2
        self.change_notes(button)

    def change_notes(self, button):
        """
        change_notes:
            When the button is pressed, changes the text of the question and answer labels by one more index.
        """
        self.index_notes += 1
        if abs(self.index_notes) >= len(self.notes):
            self.index_notes = 0

        self.label_question.text = self.notes[self.index_notes]

        self.label_answer.text = translation_pair(
            self.label_question.text, output_settings_notes()
        )

    def activete_notes(self):
        """
        activete_notes:
            Is called when the window is launched, sets the text to two labels question and answer.
        """
        self.label_question.text = self.notes[self.index_notes]

        self.label_answer.text = translation_pair(
            self.label_question.text, output_settings_notes()
        )

    def on_enter(self):
        """
        on_enter:
            Executed when the user enters the repeat screen.
        """
        # call_settings executes the saved settings.
        call_settings()
        # self.progres_bar.max = int(call_settings()[8])
        # random_or_successively outputs the list according to saves.
        self.notes = random_or_successively()
        # update_stopwatch updates the timer value.
        self.stopwatch_event = Clock.schedule_interval(self.update_stopwatch, 1)
        self.activete_notes()

    def on_leave(self):
        """
        on_leave:
            Executed when the user exits the repeat screen.
        """
        # Clock.unschedule stops the timer.
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


sm.add_widget(PageRepeat(name="pageRepeat"))
