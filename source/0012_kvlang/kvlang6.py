import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


code = '''
BoxLayout:
    Button:
        text: "1"
    Button:
        text: "2"

'''

from kivy.lang import Builder


class Study6App(App):

    def build(self):
        return Builder.load_string(code)


window = Study6App()
window.run()