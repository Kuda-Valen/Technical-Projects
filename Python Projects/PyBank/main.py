import json as js

class User: 
    def __init__(self, name, surname, balance, acc_type, acc_no):
        self.name = name
        self.surname = surname
        self.balance = balance 
        self.acc_type = acc_type
        self.acc_no = acc_no

    def add_user():
        print("\n<-- Add new user -->\n")
        name = input("What is user's Name: ")
        surname = input("What is user's Surname: ")
        acc_type = input("User's account preference (A. Savings or B.Checking): ").lower()
        balance = 0

        