from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


Window.size = (340, 580)
Window.clearcolor = (0.98, 0.52, 0, 1)


class WindowLayout(FloatLayout):
    def clear_output(self):
        self.ids.input.text = ""
    
    def on_convert_click(self):
        decimalStr = self.ids.input.text
        decimal = decimalStr
        binary = ""

        if(decimal != ""):
            decimal = int(decimal)
        else:
            self.ids.output.text = "Digite um valor para conversão!"
            return

        if(decimal == 0):
            binary = "0"
        elif(decimal < 0):
            self.ids.output.text = "Apenas números positivos!"
            self.clear_output()
            return

        while decimal >= 1:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2

        self.ids.output.text = f"Valor {decimalStr} em binário:\n{binary.zfill(8)}"
        self.clear_output()


class ConversorApp(App):
    def build(self):
        return WindowLayout()


if __name__ == "__main__":
    ConversorApp().run()