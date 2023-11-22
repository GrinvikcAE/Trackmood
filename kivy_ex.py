from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

from helpers import username_helper


class TrackmoodApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = '400'
        self.theme_cls.theme_style = 'Dark'

        screen = MDScreen()
        self.username = Builder.load_string(username_helper)
        # username = MDTextField(text='Enter your username:', pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                       size_hint_x=None, width=300)


        btn_flat = MDRectangleFlatButton(text="Show", pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                         on_release=self.show_data)


        #RGB = 255.0
        #label = MDLabel(text="Hello!", halign="center", theme_text_color="Custom", font_style="Caption",
        #                text_color=(10/RGB, 100/RGB, 83/RGB, 1), font_name="Arial",
        #                pos_hint={'center_x': 0.5, 'center_y': 0.9})
        #screen.add_widget(label)

        #icon_label = MDIcon(icon="account", pos_hint={'center_x': 0.1, 'center_y': 0.9})
        #screen.add_widget(icon_label)

        screen.add_widget(self.username)
        screen.add_widget(btn_flat)
        return screen

    def show_data(self, obj):
        print(self.username.text)


TrackmoodApp().run()
