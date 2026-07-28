"""
    Build a student grade classifier that takes a learner's name and marks
    for three subjects, calculate an average, assigns a grade and a status 
    (Pass/Fail), and displays a full report card. The program must correclty
    use conditionals for all grade and status logic.

    REQUIREMENTS
    - Collect learner name and marks for three subjects (as floats) using input()
    - Calculate the average mark across three subjects
    - Assign a letter grade: A(80+), B(70-79), C(60-69), D(50-59), F(below 50) using 
      if/else/elif
    - Assign Pass status if the average is 50 or above, Fail otherwise
    - Flag any individual subject mark below 40 as 'needs intervention'
    - Display a formatted report card showing all inputs, the average, the grade, 
    the status, and any intervention flags
"""

class Student():
    def __init__(self, name, subjects, average_grade, status):
        self.name = name
        self.subjects = []
        self.average_grade = average_grade
        self.status = status

        name = input("Enter your name: ")
        print("Enter your subjects:..")

        i=3
        while i < 3:
            subject = input("Enter subject: ")
            grade = float(input("Enter subject grade: "))
            subject_grade = {
                "subject" : subject,
                "grade" : grade
            }
            subjects.append(subject_grade)
            i += 1

    def average_grade(self):
        
        
        