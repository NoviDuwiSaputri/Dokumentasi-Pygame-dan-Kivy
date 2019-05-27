from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Line


class Menggambar(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        print("line created", touch)


class GambarkuApp(App):
    def build(self):
        parent = Widget()
        self.painter = Menggambar()
        clearbtn = Button(text='Clear')
        warnabtn = Button(text='Random Color')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)

        # button layout
        # buttonLayout = BoxLayout(orientation='horizontal')
        buttonLayout = GridLayout(rows=2)
        buttonLayout.add_widget(clearbtn)
        buttonLayout.add_widget(warnabtn)
        # 2 layout becomes one
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(parent)
        layout.add_widget(buttonLayout)
        return layout

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def add_blue(self, obj):
        self.painter


if __name__ == '__main__':
    GambarkuApp().run()