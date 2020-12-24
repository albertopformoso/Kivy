#!usr/bin/env python3
# coding UTF-8

from kivy.app import App
from kivy.uix.label import Label


class HelloApp(App):

    def build(self):
        return Label(text='Hello World')


HelloApp.run()