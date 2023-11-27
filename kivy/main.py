from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder

LabelBase.register(name='Bras Mono', fn_regular='fonts/BrassMono-Bold.ttf')

BASE_URL = f'http://127.0.0.1:8000/'
headers = {'user-agent': 'trackmood-app/0.0.1'}


class TrackmoodApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('login.kv'))
        screen_manager.add_widget(Builder.load_file('signup.kv'))
        return screen_manager


if __name__ == '__main__':
    TrackmoodApp().run()
