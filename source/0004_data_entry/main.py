#!usr/bin/env python3
# coding UTF-8

from kivy.app import App
from kivy.uix.textinput import TextInput


def build():
    ti = TextInput()
    ti.text = "Text Input Component"
    return ti


window = App()
window.build = build
window.run()