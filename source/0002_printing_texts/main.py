#!usr/bin/env python3
# coding UTF-8

from kivy.app import App
from kivy.uix.label import Label


def build():
    # Example 1:
    # return Label(text='Exercise with Python and Kivy',
    #              italic=True,
    #              font_size=50)  # 50 pixels

    # Example 2:
    lb = Label()
    lb.text = 'Exercise with Python and Kivy'
    lb.italic = True
    lb.font_size = 50
    return lb



hello_world = App()
hello_world.build = build
hello_world.run()
