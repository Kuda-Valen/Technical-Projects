
"""
We are Building a Train Carriage Management System
Each Carriage is Connected to the next carriage.

The Task:
Each node must represent a train carriage
Each carriage stores the carriage ID or name and number of passengers
"""

class Carriage:
    def __init__(self, carriage_name, carriage_passengers):
        self.carriage_name = carriage_name
        self.carriage_passengers = carriage_passengers
        self.next = None 

# This is the linked list that will store the carriages
class Train:
    def __init__(self):
        self.head = None

    def append(self, carriage_name, carriage_passengers):
        new_carriage = Carriage(carriage_name, carriage_passengers)

        if not self.head:
            new_carriage = Carriage(carriage_name, carriage_passengers)

            self.head = new_carriage
            return
        
        current_carriage = self.head
        while current_carriage.next:
            current_carriage = current_carriage.next
        current_carriage.next = new_carriage

    def display (self):
        current_carriage = self.head
        carriage = (current_carriage.carriage_name, current_carriage.carriage_passengers)
        carriages = []
        while current_carriage:
            carriages.append(str(carriage))
            current_carriage = current_carriage.next
        print(f" --> ".join(carriages) +" --> None")

def main_menu():
    """Main Menu to Manage this train system"""
    train = Train()

    while True:
        option = 0
        print("\n1. Add a new Carriage")
        print("2. View Train Carriages")
        print("5. Exit...")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                print("\n- Adding a new carriage details -")
                carriage_name = input("Enter Carriage Name: ")
                number_of_passengers = input("This carriage has: ")
                train.append(carriage_name, number_of_passengers)
                print(f"Carriage: '{carriage_name}' with '{number_of_passengers}' passengers was successfully added to current Train Carriage ")

            elif option == 2:
                print("\n - View Train Carriages -")
                train.display()
            
            elif option == 5:
                print("\nExiting....")
                break

            else: 
                print("\nInvalid option. Choose valid option..")

        except Exception as e:
            print(f"\n!! --Invalid input Error: {e} --!!")

main_menu()