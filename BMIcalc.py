from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = "vertical")
        weight_input = TextInput(readonly = True, halign = "left", font_size = 50, hint_text = "Enter weight in kg")
        height_input = TextInput(readonly = False, halign = "left", font_size = 50, hint_text = "Enter height in cm")
        button = Button(text="Calculate BMI")
        display_label = Label(text="BMI: ", font_size = 24, color=(1,1,1,1), size_hint=(1, 0.2))
        
        layout.add_widget(weight_input)
        layout.add_widget(height_input)
        layout.add_widget(button)
        layout.add_widget(display_label)


        return layout


if __name__ == "__main__":
    MyApp().run()
 