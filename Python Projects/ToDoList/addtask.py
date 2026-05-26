
import heapq

tasks = []
done_tasks = []
deleted_tasks = []

def add_task():
    
    name = input("\nEnter task name: ").lower()
    priority = int(input("Enter task priority (1-5): "))
    desc = input("Enter task description: ")
    date = input("Enter task start date (DD/MM/YYYY): ")
    due_date = input("Enter task due date (DD/MM/YYYY): ")
    status = "Not Started"

    task_info = (priority, name, desc, date, due_date, status)

    heapq.heappush(tasks, (priority, task_info))
    print(f"\nTask '{name}' added successfully with priority {priority}.")