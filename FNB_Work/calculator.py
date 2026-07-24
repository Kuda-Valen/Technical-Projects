"""
    THIS IS THE CORRECT ANSWER OF MULTI-FUNCTION-CALCULATOR
"""

def add(a, b):
    total = a + b
    return round(total, 2)

def subtract(a, b):
    diff = a - b
    return round(diff, 2)

def multiply(a, b):
    prod = a * b
    return round(prod, 2)

def divide(a, b):
    if b == 0:
        return "Error (Div/0)"
    quotient = a / b
    return round(quotient, 2)

def floor_div(a, b):
    if b == 0:
        return "Error (Div/0)"
    ans = a // b
    return round(ans, 2)

def modulus(a, b):
    if b == 0:
        return "Error (Div/0)"
    answ = a % b
    return round(answ, 2)

if __name__ == "__main__":
    print("\n==== Simple Calculator ===\n")

    # Safe float input collection
    try:
        a = float(input("Enter First number: "))
        b = float(input("Enter Second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        exit()

    # Pre-calculating results
    results = [
        ("Addition", "+", add(a, b)),
        ("Subtraction", "-", subtract(a, b)),
        ("Multiplication", "*", multiply(a, b)),
        ("Division", "/", divide(a, b)),
        ("Floor Division", "//", floor_div(a, b)),
        ("Modulus", "%", modulus(a, b))
    ]

    # Displaying a beautifully aligned f-string table
    print("\n" + "=" * 46)
    print(f"| {'Operation':<15} | {'Expression':<12} | {'Result':<11} |")
    print("=" * 46)
    
    for name, op, res in results:
        expr = f"{a} {op} {b}"
        # If the result is a float, format it to 2 decimal places in the table
        if isinstance(res, float):
            print(f"| {name:<15} | {expr:<12} | {res:<11.2f} |")
        else:
            print(f"| {name:<15} | {expr:<12} | {res:<11} |")
            
    print("=" * 46)
