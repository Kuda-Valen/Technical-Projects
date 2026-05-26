import heapq
from addtask import add_task
from view_tasks import view_tasks





if __name__ == "__main__":
    option = 0

    while True:
        print("\n === Task Manager ===\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. View Tasks by Category")
        print("5. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                add_task()
            
            elif option == 2:
                view_tasks()

            elif option == 3:
                print("\n === Tasks by Category ===\n")
            
            else:
                print("Invalid Option. Choose a valid option...")

        except ValueError: 
            print("Invalid input. Please enter valid option [1-5]")



