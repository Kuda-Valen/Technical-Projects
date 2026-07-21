from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.label import MDLabel

# --- 1. THE DATA MODEL ---
class UserData:
    """Holds the processed data exactly like your original class."""
    def __init__(self, name: str, surname: str, age: int, fav_number: float):
        self.full_name = f"{name} {surname}"
        self.upper_name = self.full_name.upper()
        self.title_name = self.full_name.title()
        self.age_months = age * 12
        self.rounded_fav = round(fav_number, 2)
        
        # Save types as strings to display them easily
        self.types_info = (
            f"Name Type: {type(name).__name__}\n"
            f"Surname Type: {type(surname).__name__}\n"
            f"Age Type: {type(age).__name__}\n"
            f"Fav Num Type: {type(fav_number).__name__}"
        )

# --- 2. THE INPUT SCREEN ---
class InputScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=15)
        
        # Title
        layout.add_widget(MDLabel(text="FNB Practice Form", font_style="H5", halign="center"))
        
        # Form Inputs
        self.name_input = MDTextField(hint_text="First Name", icon_left="account")
        self.surname_input = MDTextField(hint_text="Surname", icon_left="account-box")
        self.age_input = MDTextField(hint_text="Age", icon_left="calendar", input_filter="int")
        self.fav_num_input = MDTextField(hint_text="Favourite Number", icon_left="star", input_filter="float")
        
        layout.add_widget(self.name_input)
        layout.add_widget(self.surname_input)
        layout.add_widget(self.age_input)
        layout.add_widget(self.fav_num_input)
        
        # Submit Button
        submit_btn = MDRaisedButton(text="SUBMIT & PROCESS", pos_hint={'center_x': 0.5}, size_hint_x=1)
        submit_btn.bind(on_release=self.process_data)
        layout.add_widget(submit_btn)
        
        self.add_widget(layout)

    def process_data(self, instance):
        # Validation check
        if not (self.name_input.text and self.surname_input.text and self.age_input.text and self.fav_num_input.text):
            return # Don't advance if fields are empty
            
        # Convert types safely just like your terminal requirements
        user_object = UserData(
            name=self.name_input.text,
            surname=self.surname_input.text,
            age=int(self.age_input.text),
            fav_number=float(self.fav_num_input.text)
        )
        
        # Pass the data to the Output Screen and switch screens
        output_screen = self.manager.get_screen('output')
        output_screen.display_results(user_object)
        self.manager.current = 'output'

# --- 3. THE OUTPUT SCREEN ---
class OutputScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation='vertical', padding=30, spacing=15)
        
        self.results_label = MDLabel(text="", font_style="Body1", halign="left")
        layout.add_widget(self.results_label)
        
        # Back Button
        back_btn = MDFlatButton(text="BACK TO FORM", pos_hint={'center_x': 0.5})
        back_btn.bind(on_release=self.go_back)
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
        
    def display_results(self, user):
        # Update the UI text dynamically using an f-string
        self.results_label.text = (
            f"✨ Welcome, {user.title_name}!\n\n"
            f"🔤 UPPERCASE: {user.upper_name}\n"
            f"🔤 Title Case: {user.title_name}\n\n"
            f"📅 Age in Months: {user.age_months} months\n\n"
            f"🔢 Rounded Fav Number: {user.rounded_fav}\n\n"
            f"💻 System Data Types:\n{user.types_info}"
        )
        
    def go_back(self, instance):
        self.manager.current = 'input'

# --- 4. THE MAIN APPLICATION ---
class FnbPracticeApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        
        # Initialize ScreenManager
        sm = MDScreenManager()
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(OutputScreen(name='output'))
        
        return sm

if __name__ == '__main__':
    FnbPracticeApp().run()
