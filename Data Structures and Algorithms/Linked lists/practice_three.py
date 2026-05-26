
"""
We are Building a Train Carriage Management System
Each Carriage is Connected to the next carriage.

The Task:
Each node must represent a train carriage
Each carriage stores the carriage ID or name and number of passengers
"""

class Carriage:
    def __init__(self, carriage_info):
        self.carriage_info = carriage_info
        self.next = None 

# This is the linked list that will store the carriages
class Train:
    def __init__(self):
        self.head = None

    def append(self, carriage_info):
        new_carriage = Carriage(carriage_info)

        if not self.head:
            new_carriage = Carriage(carriage_info)

            self.head = new_carriage
            return
        
        current_carriage = self.head
        while current_carriage.next:
            current_carriage = current_carriage.next
        current_carriage.next = new_carriage

    def display (self):
        current_carriage = self.head
        carriages = []
        while current_carriage:
            carriages.append(str(current_carriage.carriage_info))
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
                number_of_passengers = int(input("This carriage has: "))
                train.append(number_of_passengers)
                print(f"'{number_of_passengers}' was successfully added to current Train Carriage info")

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