from kivy.lang import Builder

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.popup import Popup


from backfon import *

from Database.datebase import *

from Backend.switching import set_screen, sm


class PageThemes(Screen):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        relativelayout = RelativeLayout()
        floatlayout = FloatLayout(size_hint_y=1.4)
        gridlayout = GridLayout(
            cols=2,
            size_hint_y=None,
            height=0
        )
        boxlayout = BoxLayout(
            size_hint_y=1,
            orientation='horizontal',
            size_hint=[.7, .19],
            pos_hint={'x': .15, 'y': .70}
        )
        scrollview = ScrollView(
            size_hint=(1, .8),
            pos_hint={'x': 0, 'y': .05}
        )
        svforgl = ScrollView(  # svforgl --> scrollview for gridlayout


            size_hint=(.7, .6),
            pos_hint={'x': .15, 'y': .22}
        )

        self.root = Builder.load_string(KV)
# --------------------------------------------------------------------------------------
        self.spinner = Spinner(
            text='Виберіть тему',  # Select a themes
            font_size=18,
            # values=self.thems_from_db,
            size_hint=(.7, .30),
            pos_hint={'x': .15, 'y': .7},
        )
        max = 2
        self.spinner.bind(on_press=self.thems_from_db)
        self.spinner.dropdown_cls.max_height = self.spinner.height * max + max * 2
# -------------------------------------------------------------------------------------
# //////////////////////////////////////////////////////////////////////////////////////
        """
        for i in range(30):
            gridlayoutnew = GridLayout(
                cols=2,
                height=(25))
            label = Label(
                text='Слово %a' % i,
                font_size=18)
            gridlayout.height += gridlayoutnew.height
            gridlayoutnew.add_widget(label)
            gridlayout.add_widget(gridlayoutnew)"""

# //////////////////////////////////////////////////////////////////////////////////////
        relativelayout.add_widget(Button(
            text="<--",
            on_press=lambda x: set_screen('menu'),
            font_size=20,
            size_hint=(.16, .08),
            pos_hint={'x': .04, 'y': .89},
            background_color=[.0, .84, .64],
            background_normal=''
        ))

        floatlayout.add_widget(Button(
            text="Додати тему",  # Add a theme
            font_size=20,
            size_hint=(.7, .07),
            pos_hint={'x': .15, 'y': .92},
            on_press=self.add_them,
            background_color=[.0, .84, .64],
            background_normal=''
        ))
        floatlayout.add_widget(TextInput(
            hint_text='Слово',  # Word
            hint_text_color=[.55, .55, .55, 1],
            font_size='18',
            halign="center",
            size_hint=(.38, .08),
            pos_hint={'x': .1, 'y': .10},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1]
        ))
        floatlayout.add_widget(TextInput(
            hint_text='Переклад',  # Translate
            hint_text_color=[.55, .55, .55, 1],
            font_size='18',
            halign="center",
            size_hint=(.38, .08),
            pos_hint={'x': .5, 'y': .10},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1]
        ))
        floatlayout.add_widget(Button(
            text="Додати слово",  # Add a word
            font_size=20,
            size_hint=(.6, .07),
            pos_hint={'x': .2, 'y': 0},
            background_color=[.0, .84, .64],
            background_normal=''
        ))

        svforgl.add_widget(gridlayout)  # svforgl --> scrollview for gridlayout
        boxlayout.add_widget(self.spinner)
        floatlayout.add_widget(svforgl)
        floatlayout.add_widget(boxlayout)
        scrollview.add_widget(floatlayout)
        relativelayout.add_widget(scrollview)
        self.add_widget(self.root)
        self.add_widget(relativelayout)

    def add_them(self, button):
        floatlayoutforpopup = FloatLayout()

        self.textinputthem = TextInput(
            hint_text='Назва теми',
            hint_text_color=[.55, .55, .55, 1],
            font_size=20,
            halign="center",
            size_hint=(.8, .35),
            pos_hint={'x': .1, 'y': .5},
            foreground_color=[1, 1, 1, 1],
            background_color=[.29, .29, .29],
            cursor_color=[1, 1, 1, 1]
        )
        self.addbutton = Button(
            text="Додати тему",  # Add a word
            font_size=20,
            size_hint=(.75, .2),
            pos_hint={'x': .125, 'y': .1}
        )

        floatlayoutforpopup.add_widget(self.textinputthem)
        floatlayoutforpopup.add_widget(self.addbutton)

        popup = Popup(
            title='Додайте тему',
            title_size=18,
            size_hint=(.9, .7),
            pos_hint={'x': .05, 'y': .15},
            separator_height=3,
            separator_color=[.0, .84, .64],
            content=floatlayoutforpopup,
        )
        popup.open()

        self.addbutton.bind(on_press=self.add_button_log)
        self.addbutton.bind(on_press=popup.dismiss)

    def add_button_log(self, pres):

        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            port=3306,
            database='dictionary_db',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                create_them = "INSERT INTO Thems (them) VALUES (%s)"
                values = (self.textinputthem.text,)
                cursor.execute(create_them, values)
                connection.commit()
        finally:
            connection.close()

    def thems_from_db(self, value):
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            port=3306,
            database='dictionary_db',
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Thems")
                records = cursor.fetchall()
                print(records)
                word = [record['them'] for record in records]
                print(word)
                self.spinner.values = word

                connection.commit()
        finally:
            connection.close()


sm.add_widget(PageThemes(name='pageTemes'))
