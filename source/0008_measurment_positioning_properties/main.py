#!usr/bin/env python3
# coding UTF-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class RootWidget(FloatLayout):
    pass


class MeasurementApp(App):

    def build(self):
        return RootWidget()


MeasurementApp().run()
