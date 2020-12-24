#!usr/bin/env python3
# coding UTF-8

from kivy.app import App
from kivy.uix.button import Button


def click():
    global i
    i += 1
    print(f"The button was pressed {i} times")


def build():
    bt = Button()
    bt.text = "Click here"
    bt.on_press = click
    return bt


i = 0
window = App()
window.build = build
window.run()