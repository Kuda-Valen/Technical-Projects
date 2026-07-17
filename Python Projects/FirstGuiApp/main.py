from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(App):
    def build(self):
        # 1. Create a vertical layout container
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)

        # 2. Add a welcome message heading
        self.heading = Label(text="Welcome Back!", font_size="28sp", color=(1, 1, 1, 1))
        layout.add_widget(self.heading)

        # 3. Add an input field for the user's name
        self.name_input = TextInput(hint_text="Enter your name...", multiline=False, size_hint_y=None, height=50)
        layout.add_widget(self.name_input)

        # 4. Add an action button
        submit_btn = Button(text="Submit", font_size="20sp", background_color=(0.2, 0.8, 0.2, 1), size_hint_y=None, height=60)
        
        # 5. Bind the button to a Python function (Event Handling)
        submit_btn.bind(on_press=self.greet_user)
        layout.add_widget(submit_btn)

        return layout

    def greet_user(self, instance):
        # This function runs when the button is clicked
        user_name = self.name_input.text
        if user_name.strip():
            self.heading.text = f"Hello, {user_name}!"
            self.name_input.text = ""  # Clear the input field
        else:
            self.heading.text = "Please enter a name first!"

if __name__ == '__main__':
    LoginScreen().run()
