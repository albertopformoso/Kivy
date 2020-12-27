import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


def funcSelf(x):
    print('funcSelf')
Button.funcSelf = funcSelf


class MyScreen(BoxLayout):

    def funcRoot(self):
        print('funcRoot')


class Study5App(App):

    def funcApp(self):
        print('funcApp')

window = Study5App()
window.run()