from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set("graphics", "width", "340")
Config.set("graphics", "height", "580")

# Importing it before setting graphics don't change the screen size
from kivy.core.window import Window

Window.clearcolor = (0.98, 0.52, 0, 1)


class WindowLayout(FloatLayout):
    def clear_output(self):
        self.ids.input.text = ""

    def on_convert_click(self):
        self.to_binary(self.ids.input.text)
    
    def to_binary(self, decimal):
        decimalCalc = decimal
        binary = ""

        try:
            decimalCalc = int(decimalCalc)
            decimal = int(decimal)
        except ValueError:
            self.ids.output.text = "Digite um valor válido!"
            self.clear_output()
            return

        if(decimalCalc == 0):
            binary = "0"
        elif(decimalCalc < 0):
            self.ids.output.text = "Apenas números positivos!"
            self.clear_output()
            return

        while decimalCalc >= 1:
            binary = str(decimalCalc % 2) + binary
            decimalCalc = decimalCalc // 2

        self.ids.output.text = f"Valor {decimal} em binário:\n{binary.zfill(8)}"
        self.clear_output()


class ConversorApp(App):
    def build(self):
        return WindowLayout()


if __name__ == "__main__":
    ConversorApp().run()