""" Parking Lot Management System 

This is a system to be used by University to manage their parking lot

It is for Employees; Students; Visitors

There are specific lot for employees, students, and visitors"""

import datetime

class Driver():
    def __init__(self):
        print()

class Permit():
    def __init__(self, permit_id: str, driver_id: str, start_date: datetime, end_date: datetime, permit_amount: float, parking_lot: chr):
        self.permit_id = permit_id
        self.driver_id = driver_id
        self.start_date = start_date
        self.end_date = end_date
        self.permit_amount = permit_amount
        self.parking_lot = parking_lot

class EmployeePermit(Permit):
    def __init__(self, permit_id: str, driver_id:str, start_date: datetime, end_date: datetime, permit_amount: float, parking_lot: chr, employee_name):
        super().__init__(permit_id, driver_id, start_date, end_date, permit_amount, parking_lot)
        self.employee_name = employee_name

class StudentPermit(Permit):
    def __init__(self, permit_id: str, driver_id: str, start_date: datetime, end_date: datetime, permit_amount: float, parking_lot: chr, student_name):
        super().__init__(permit_id, driver_id, start_date, end_date, permit_amount, parking_lot)
        self.student_name = student_name

