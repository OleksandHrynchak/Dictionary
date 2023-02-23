
from kivy.uix.screenmanager import ScreenManager, NoTransition


def set_screen(name_screen):
    sm.current = name_screen


# log (how pages one or two)
def page_one(Check, activeone):
    if activeone == True:
        global pagecheck
        pagecheck = True
    elif activeone == False:
        pagecheck = False


def page_two(Repetition, activetwo):
    if activetwo == True:
        global pagerepetition
        pagerepetition = True
    elif activetwo == False:
        pagerepetition = False


def one_or_two(any):
    if pagecheck:
        set_screen('pageStartTwo')
    elif pagerepetition:
        set_screen('pageStartOne')
    else:
        set_screen('menu')
# /log


sm = ScreenManager(transition=NoTransition())
