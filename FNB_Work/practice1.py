"""
Requirements
Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float)
Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’
Display the name in UPPERCASE using .upper() and in Title Case using .title()
Calculate and display the age in months (age × 12)
Round the favourite number to 2 decimal places using round()
Print the data type of each collected value using type()
"""

class User():
    def __init__(self, name: str, surname: str, age: int, fav_number: float):
        self.name = name
        self.surname = surname
        self.age = age
        self.fav_number = fav_number

        user = (name, surname, age, fav_number)

    def calculate_age(self, age):
        age_in_months = age*12
        return age_in_months

if __name__ == "__main__":
    #user = User()

    while True:
        print("\n== My First FNB practice Q==\n")
        print("1. Enter your information")
        print("2. View name in upper case and title case")
        print("3. Display your age in months")
        print("4. Display your favourite numbe rounded to 2 Decimals")
        print("5. Display all Data Types")
        print("6. Exit")

        option = int(input("\nChoose an Option: "))

        if option == 1:
            name = input("\nEnter your name: ")
            surname = input("Enter your surname: ")
            age = input("Enter your age: ")
            fav_number = input("Enter your favourite number: ")

            user = User(name, surname, age, fav_number)
        
        elif option == 2:
            print(user.name.upper())
        
        elif option == 3:
            print(f"Your age in months: {user.age*12}")
        
        elif option == 4:
            print(f"Your fav number is: {user.fav_number.round(2)}")
        
        elif option == 5:
            print(f"Name: {user.name} => {user.name.type()}")
            print(f"Surname: {user.surname} => {user.surname.type()}")
            print(f"Age: {user.age} => {user.age.type()}")
            print(f"fav_number: {user.fav_number} => {user.fav_number.type()}")
        
        elif option == 6:
            print("\nExit..")
            break

        else:
            print("Invalid input..Choose a valid input")