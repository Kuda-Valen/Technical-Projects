import heapq
from addtask import tasks
from addtask import done_tasks
from addtask import deleted_tasks

def view_tasks():

    print("\n === All Tasks ===\n")
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            #print(task)
            print(f"Name: {task[1][1]} || Description: {task[1][2]} || Priority: {task[1][0]} || Due Date: {task[1][4]} || Status: {task[1][5]}")
            
    
        print("\nChoose a task")
        task_name = input("Enter the name of the task you want to select: ").lower()
        a = 0
        for i, task in enumerate(tasks):
            if task[1][1] == task_name:
                print(f"Task '{tasks[i][1][1]}' has been selected.")
                a += 1
            else:
                print("Task Name 'task_name' not found...")
                print("Try again\n")
                return
                
        while True:
            print("\na. Mark as done")
            print("b. Edit task status")
            print("c. Delete task")
            print("d. Back to main menu")

            sub_option = input("\nChoose an option [a-d]: ").lower()

            if sub_option == 'a': 
                new_name = tasks[i][1][1]
                new_priority = tasks[i][1][0]
                new_desc = tasks[i][1][2]
                new_date = tasks[i][1][3]
                new_due_date = tasks[i][1][4]
                new_status = "Done"

                done_task_info = (new_name, new_desc, new_date, new_due_date, new_status)
                done_tasks.append(done_task_info)
                print(f"\nTask '{tasks[i][1][1]}'has been marked as done.")

                deleted_tasks.append(tasks[i])
                del tasks[i]
                return
                
            
            elif sub_option == 'b':
                edit_option = 0
                while True:
                    print("\n== Edit Task Status ==\n")
                    print("1. Edit task name")
                    print("2. Edit task description")
                    print("3. Edit task due date")
                    print("4. Edit task priority")
                    print("5. Edit task status")
                    print("6. Back to task options")

                    edit_option = int(input("\nChoose an option [1-6]:"))

                    if edit_option == 1:
                        print("\nEdit Task Name")
                        print(f"Current Task Name: {tasks[i][1][1]} with Description: {tasks[i][1][2]}")
                        new_name = input("Enter new task name: ")
                        new_priority = tasks[i][1][0]
                        new_desc = tasks[i][1][2]
                        new_date = tasks[i][1][3]
                        new_due_date = tasks[i][1][4]
                        new_status = tasks[i][1][5]

                        deleted_tasks.append(tasks[i])
                        del tasks[i]
                    
                        edited_task = (new_priority,new_name,  new_desc, new_date, new_due_date, new_status)
                        heapq.heappush(tasks, (new_priority, edited_task))
                        print(f"Your Task name has been changed to '{new_name}' successfully...")
                        break


                        """This is where we left off"""

                        
                    elif edit_option == 2:
                        print("\nEdit Task Description")
                    
                    elif edit_option == 3:
                        print("\nEdit Task Due Date")

                    elif edit_option == 4: 
                        print("\nEdit Task Priority")

                    elif edit_option == 5:
                        print("\nEdit Task Status")
                        
                    elif edit_option == 6:
                        break


            elif sub_option == 'c':
                print("\n== Delete Tasks == ")
                del tasks[i]
            
            elif sub_option == 'd':
                break
