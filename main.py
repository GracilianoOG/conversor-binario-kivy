from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


Window.size = (340, 580)
Window.clearcolor = (0.98, 0.52, 0, 1)


class WindowLayout(FloatLayout):
    def on_convert_click(self):
        decimal = self.ids.input.text
        binary = ""

        if(decimal is not ""):
            decimal = int(decimal)
        else:
            return

        while decimal >= 1:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2

        self.ids.output.text = f"%08d" % int(binary)


class ConversorApp(App):
    def build(self):
        return WindowLayout()


if __name__ == "__main__":
    ConversorApp().run()