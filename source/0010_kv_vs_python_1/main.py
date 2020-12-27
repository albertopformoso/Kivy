import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Screen1(BoxLayout):

    def on_press_bt(self):
        window.root_window.remove_widget(window.root)
        window.root_window.add_widget(Screen2())

    def __init__(self, **kwargs):
        super(Screen1, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt1 = Button(text='Click')
        bt1.on_press = self.on_press_bt
        self.add_widget(bt1)
        self.add_widget(Button(text='bt2'))
        self.add_widget(Button(text='bt3'))


class Screen2(BoxLayout):

    def on_press_bt(self):
        window.root_window.remove_widget(window.root)
        window.root_window.add_widget(Screen1())

    def __init__(self, **kwargs):
        super(Screen2, self).__init__(**kwargs)
        self.orientation = 'vertical'
        bt = Button(text='Click')
        bt.on_press = self.on_press_bt
        self.add_widget(bt)


class KVvsPY(App):

    def build(self):
        return Screen1()


window = KVvsPY()
window.run()