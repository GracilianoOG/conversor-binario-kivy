from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class WindowLayout(BoxLayout):
    pass


class ConversorApp(App):
    def build(self):
        return WindowLayout()


if __name__ == "__main__":
    ConversorApp().run()