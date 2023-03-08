from kivy.app import App

from kivy.uix.button import Button

class ExemploApp(App):
    def Build(self):
        return Button(text = "Olá mundo")
        