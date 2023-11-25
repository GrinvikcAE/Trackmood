from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

from helpers import username_helper


Window.size = (400, 700)

LabelBase.register(name='Bras Mono', fn_regular='fonts/BrassMono-Bold.ttf')

class TrackmoodApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('signup.kv'))
        return screen_manager

    # def show_data(self, obj):
    #     pass


if __name__ == '__main__':
    TrackmoodApp().run()
