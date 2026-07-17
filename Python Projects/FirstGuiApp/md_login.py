from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

class MaterialLoginApp(MDApp):
    def build(self):
        # 1. Configure the global app theme styling
        self.theme_cls.theme_style = "Dark"      # Choices: "Light" or "Dark"
        self.theme_cls.primary_palette = "Teal" # Accent color for inputs/buttons

        # 2. Setup layout container with centered alignment
        layout = MDBoxLayout(
            orientation='vertical', 
            padding=40, 
            spacing=25,
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(0.8, 0.6)
        )

        # 3. Modern Material Title Label
        self.title_label = MDLabel(
            text="Welcome Back", 
            halign="center",
            font_style="H4" # Uses built-in typography sizing
        )
        layout.add_widget(self.title_label)

        # 4. Modern Input Field with built-in animations and icons
        self.username_input = MDTextField(
            hint_text="Username",
            helper_text="Enter your unique system ID",
            helper_text_mode="on_focus",
            icon_left="account" # Loads built-in Material design icon
        )
        layout.add_widget(self.username_input)

        # 5. Clean, elevated Material design action button
        submit_btn = MDRaisedButton(
            text="SIGN IN",
            pos_hint={'center_x': 0.5}, # Centers the button horizontally
            size_hint_x=0.5
        )
        submit_btn.bind(on_release=self.authenticate)
        layout.add_widget(submit_btn)

        return layout

    def authenticate(self, instance):
        input_text = self.username_input.text
        if input_text.strip():
            self.title_label.text = f"Logged in as: {input_text}"
            self.username_input.text = ""
        else:
            self.title_label.text = "Username Required!"

if __name__ == '__main__':
    MaterialLoginApp().run()
