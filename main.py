from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


Window.size = (360, 580)
Window.clearcolor = (0.98, 0.52, 0, 1)


class WindowLayout(BoxLayout):
    pass


class ConversorApp(App):
    def build(self):
        return WindowLayout()


if __name__ == "__main__":
    ConversorApp().run()