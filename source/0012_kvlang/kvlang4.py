import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MyScreen(BoxLayout):

    def click(self):
        print('Clicked')
        self.ids.lb1.text = "°_°"
        self.ids.lb2.text = ":v"


class Study4App(App):
    pass


window = Study4App()
window.run()