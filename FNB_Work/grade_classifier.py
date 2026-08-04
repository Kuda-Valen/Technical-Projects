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

def get_student_info():
    name = input("Enter Name: ").strip()
    subject1 = input("Enter Subject 1 Name: ").strip()
    subject1_marks = float(input("Enter Subject 1 Marks: ")).strip()
    subject2 = input("Enter Subject 2 Name: ").strip()
    subject2_marks = float(input("Enter Subject 2 Marks: ")).strip()
    subject3 = input("Enter Subject 3 Name: ").strip()
    subject3_marks = float(input("enter Subject 3 Marks: ")).strip()
    subjects = [subject1, subject2, subject3]
    subject_marks = [subject1_marks, subject2_marks, subject3_marks]

    average_mark = (subject1_marks+subject2_marks+subject3_marks)/3
    grade_letter = get_grade_letter(average_mark)
    pass_status = get_pass_status(average_mark)

    def get_grade_letter(average_mark):
        if average_mark >= 80:
            grade_letter = 'A'
        elif average_mark >= 70 and average_mark < 80:
            grade_letter = 'B'
        elif average_mark >= 60 and average_mark < 70:
            grade_letter = 'C'
        elif average_mark >= 50 and average_mark < 60:
            grade_letter = 'D'
        else:
            grade_letter = 'F'
        return grade_letter

    def get_pass_status(average_mark):
        if average_mark >= 50:
            pass_status = "Pass"

        else:
            pass_status = "Fail"
        return pass_status