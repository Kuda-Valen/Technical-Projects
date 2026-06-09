"""Student Course Registration System
You are building a university registration system using a custom singly linked list.

MAIN GOAL
Create a linked list where each node represents a student.

"""

class StudentNode:
    def __init__(self, student_info):
        self.student_info = student_info
        self.next = None

        

class Student:
    def __init__(self, name: str, student_num: str, year: int, course: str):
        self.name = name
        self.student_num = student_num
        self.year = year
        self.course = course

class Manager:
    def __init__(self):
        self.head = None

    def add_student(self):
        #name = input("\nEnter Student name: ")
        #student_num = input("Enter Student number: ")
        #course = input("Enter Course Name: ")
        #year = int(input("Which Year level: "))

        #student_info = Student(name, student_num, year, course)
        student_info = Student("Kuda", "eduv4807080", 3, "Information Technology Robotics")

        student_node = StudentNode(student_info)

        if self.head is None:
            self.head = student_node
            return
        
        current = self.head

        while current.next:
            current = current.next
        
        current.next = student_node

    def view_students(self):
        if self.head is None: 
            print("\nThere are not students")
            return
        
        current = self.head

        while current:
            student = current.student_info

            print(f"Student Name: {student.name} ")
            print(f"Student Number: {student.student_num}")
        
            current = current.next 

if __name__ == "__main__":
    manager = Manager()

    while True:
        print("\nStudent Course Registration System")
        print("1. Add a Student")
        print("2. View all Students")
        print("9. Exit")

        try: 
            option = int(input("Choose an option: "))

            if option == 1:
                manager.add_student()

            if option == 2:
                manager.view_students()        
        except ValueError as e:
            print(f"Invalid input. Error: {e}")
