"""
    Build a Python Calculator that takes two numbers as 
    input and performs all four basic arithmetic operations
    plus two advanced operations. The calculator mush handle
    user input safely using type casting and display results 
    clearly using f-strings.

    ================================
            Requirements
    - User float(input()) to collect numbers from user
    - Calculate and display: addition , subtractoin, multiplication
      and division
    - Calculate and display: floor division(//) and modulus(%)
    - Round all results to 2 decimal places using round()
    - Handle division by zero - if the second number is 0, display
      a friendly error message instead of crashing
    - Display all results in a formatted table using f-string
    ================================
    
"""

def add(a, b):
    total = a + b
    return round(total, 2)

def subtract(a, b):
    diff = a - b
    return round(diff, 2)

def multiply(a, b):
    prod = a*b
    return round(prod, 2)

def divide(a, b):
    if b == 0:
        return ("Cannot divide because second number is zero")

    else:
        qotient = a/b
        return round(qotient, 2)

def floor_div(a, b):
    if b == 0:
        return("Cannot divide because second number is zero")
    else:
        ans = a//b
        return round(ans, 2)

def modulus(a, b):
    if b == 0:
        return("Cannot divide because second number is zero")
    else:
        answ = a%b
        return round(answ, 2)

if __name__ == "__main__":
    print("\n==== Simple Calculator ===\n")

    a = float(input("Enter First number: "))
    b = float(input("Enter Second number: "))

    print("\n == Answers == \n")
    print(f"1. {a} + {b} = {add(a, b)}")
    print(f"2. {a} - {b} = {subtract(a, b)}")
    print(f"3. {a} x {b} = {multiply(a, b)}")
    print(f"4. {a} / {b} = {divide(a, b)}")
    print(f"5. {a} // {b} = {floor_div(a, b)}")
    print(f"6. {a} % {b} = {modulus(a, b)}")
