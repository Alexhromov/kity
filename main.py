from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class CounterApp(App):
    counter = 0
    goal = 2

    def refresh(self, instance):
        self.counter = 0
        self.but1.text = "0"
        self.but1.background_color = [.4, .1, 0, 1]

    def update_but1(self, instance):
        self.counter += 1
        if self.counter == self.goal and self.goal != 0:
            self.but1.background_color = [0, 1, 0, 1]
        self.but1.text = str(self.counter)

    def on_focus(self, instance, value):
        if not value:
            self.goal = int(self.textinput.text)

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=20)

        blh = BoxLayout(orientation='horizontal', size_hint=(1, .2))
        blh.add_widget(Button(text="Refresh", on_press=self.refresh))
        blh.add_widget(Widget())

        blh.add_widget(Label(text="Goal"))
        self.textinput = TextInput()
        self.textinput.bind(focus=self.on_focus)
        blh.add_widget(self.textinput)

        bl.add_widget(blh)
        self.but1 = Button(text=str(self.counter), on_press=self.update_but1, size_hint=(1, .8))
        bl.add_widget(self.but1)
        return bl


if __name__ == "__main__":
    CounterApp().run()