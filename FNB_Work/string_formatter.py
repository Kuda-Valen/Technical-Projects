"""
    This script need sto take user's first name, last name and a short bio message as input
    Then it appllies multiple string tranformations to produce a formatted user profile output
    This simulates how a real app backend processes user-submitted text

    == Requirements ==

    - Take user input first_name, last_name, bio message 
    - Create a username by combining first initial and last name in lowercase
    - display the full name in Title case using .title()
    - strip leading/trailing whitespace from teh bio before displaying it using  .strip()
    - Count and display the number of characters in the bio using len()
    - replace any occurrence of "I am" in the bio with "I'm" using .replace()
    - Display all output using  f-strings 
"""

def username_setter(name, surname):
    name = name.lower()
    surname = surname.lower()
    username = name[0] + surname
    return username

if __name__ == "__main__":

    while True:
        print("\n==== User Info Formatter ====\n")
        print("1. Input user information")
        print("2. Display Formatted info")
        print("3. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                first_name = input("Enter your first name: ").strip()
                last_name = input("Enter your last name: ").strip()
                bio = input("Enter a small Bio paragraph: ").strip()
            
            elif option == 2:
                print("\n== Formatted User Info ==\n")
                username = username_setter(first_name, last_name)
                print(first_name.title(), last_name.title())
                print(f"Your username: {username}")
                print(f"Your Bio: \n{bio.strip()}")
                print(f"Number of characters in your bio: {len(bio)}")
                print(f"New bio without 'I am': \n{bio.replace("I am", "I'm")}")
                
            
            elif option == 3:
                print("\nExiting...")
                break
            
            else:
                print("Invalid input. Choose a valid option:...")
        
        except ValueError as e:
            print(f"\nEncountered an input error: {e}")