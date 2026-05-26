import heapq
from view_missions import view_mission 
from add_mission import add_mission 
from execute import execute
from view_completed import view_completed

mission_id = 0
missions = []
completed_missions = []

# Main menu
option = 0
while option != 5:
    print("\n=== Warehouse Robot Mission Control ===\n")
    print("1. Add new Mission")
    print("2. Execute the next mission")
    print("3. View all pending missions")
    print("4. View the mission history stack")
    print("5. Exit")

    try:
        option = int(input("\nChoose an option: "))

        if option == 1:
            add_mission()
        
        elif option == 2:
            execute()
        
        elif option == 3:
            view_mission()

        elif option == 4:
            view_completed()
        
        elif option == 5:
            print("Thank You! Bye")

        else:
            print("Invalid option. Choose a valid option [1-5]")

    except ValueError:
        print("Invalid input. Choose a valid option [1-5]")