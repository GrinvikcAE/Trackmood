username_helper = """
MDTextField:
    hint_text: "Enter your username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "account"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""

# screen = MDScreen()
#         self.username = Builder.load_string(username_helper)
#         # username = MDTextField(text='Enter your username:', pos_hint={'center_x': 0.5, 'center_y': 0.5},
#         #                       size_hint_x=None, width=300)
#
#
#         btn_flat = MDRectangleFlatButton(text="Show", pos_hint={'center_x': 0.5, 'center_y': 0.4},
#                                          on_release=self.show_data)
#
#
#         #RGB = 255.0
#         #label = MDLabel(text="Hello!", halign="center", theme_text_color="Custom", font_style="Caption",
#         #                text_color=(10/RGB, 100/RGB, 83/RGB, 1), font_name="Arial",
#         #                pos_hint={'center_x': 0.5, 'center_y': 0.9})
#         #screen.add_widget(label)
#
#         #icon_label = MDIcon(icon="account", pos_hint={'center_x': 0.1, 'center_y': 0.9})
#         #screen.add_widget(icon_label)
#
#         screen.add_widget(self.username)
#         screen.add_widget(btn_flat)
# <Main>:
#     ScrollView:
#         MDList:
#             OneLineIconListItem:
#                 text: "Screen 1"
#                 on_release:
#                     root.nav_drawer.set_state("close")
#                     root.screen_manager.current = "screen1"
#                 IconLeftWidget:
#                     icon: "account-circle"
#                     on_release:
#                         root.nav_drawer.set_state("close")
#                         root.screen_manager.current = "screen1"
#             OneLineIconListItem:
#                 text: "Screen 2"
#                 on_release:
#                     root.nav_drawer.set_state("close")
#                     root.screen_manager.current = "screen2"
#                 IconLeftWidget:
#                     icon: "exit-to-app"
#                     on_release:
#                         root.nav_drawer.set_state("close")
#                         root.screen_manager.current = "screen2"
#
# <LoginScreen>:
#     Screen:
#         MDTopAppBar:
#             pos_hint: {"top": 1}
#             title: "Navigation Drawer"
#             elevation: 2.5
#             left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
#
#         MDNavigationDrawer:
#             id: nav_drawer
#             Main:
#                 screen_manager: screen_manager
#                 nav_drawer: nav_drawer
#
#         MDNavigationLayout:
#             ScreenManager:
#                 id: screen_manager
#                 Screen:
#                     name: "screen1"
#                     MDLabel:
#                         text: "Screen 1"
#                         halign: "center"
#                 Screen:
#                     name: "screen2"
#                     MDLabel:
#                         text: "Screen 2"
#                         halign: "center"