#!usr/bin/env python3
# coding UTF-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

i = 0


def click():
    global i
    i += 1
    print(f"The button was pressed {i} times")


def build():
    # Instances
    layout = FloatLayout()
    ed = TextInput(text='Exercise')
    bt = Button(text='Click here')

    # Configurations
    ed.size_hint = None, None
    ed.height = 300  # dimensions (pixels)
    ed.width = 400  # dimensions (pixels)
    ed.y = 250  # position (pixels)
    ed.x = 100  # position (pixels)

    bt.size_hint = None, None
    bt.width = 200
    bt.height = 50
    bt.y = 100
    bt.x = 200

    bt.on_press = click

    # Adding to layout
    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout


window = App()

# Window settings
Window.size = 600, 600
window.title = 'Kivy exercise'

window.build = build
window.run()
