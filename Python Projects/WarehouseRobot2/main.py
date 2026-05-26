from mission import add_mission
from operations import execute
from data import missions, completed_missions

def view_missions():
    if not missions:
        print("No missions")
        return

    for p, m in missions:
        print(m)

def view_completed():
    if not completed_missions:
        print("No completed missions")
        return

    for m in completed_missions:
        print(m)

def main():
    option = 0

    while option != 5:
        print("\n=== Warehouse Robot Mission Control ===")
        print("1. Add Mission")
        print("2. Execute Mission")
        print("3. View Missions")
        print("4. View Completed")
        print("5. Exit")

        try:
            option = int(input("Choose: "))

            if option == 1:
                add_mission()
            elif option == 2:
                execute()
            elif option == 3:
                view_missions()
            elif option == 4:
                view_completed()

        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()