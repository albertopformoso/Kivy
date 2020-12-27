import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Screen1(BoxLayout):

    def on_press_bt(self):
        window.root_window.remove_widget(window.root)
        window.root_window.add_widget(Screen2())


class Screen2(BoxLayout):

    def on_press_bt(self):
        window.root_window.remove_widget(window.root)
        window.root_window.add_widget(Screen1())


class KVvsPY2(App):

    def build(self):
        return Screen1()


window = KVvsPY2()
window.run()