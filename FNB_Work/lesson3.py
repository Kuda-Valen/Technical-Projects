# Adding two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def add(a, b):
    return a + b

print(f"Sum of {num1} and {num2} is: {add(num1, num2)}")

# String concatination is when you are adding two string, or call the add
# method to add two variables that are not integer datatypes to perform 
# the mathematical calculation
# Type casitng is labling a variable to a specific datatype
# Modulus division returns the remainder after division (%)
number = 1.12345
print("\nRounded 1.12345 to two decimals: ", round(number, 2))

print("\n--- Modulus division ---\n")
print(f"Remainder of 10/2 = {10%2}")
print(f"Normal Division of 5/3 = {5/3}")
print(f"Modulus Division of 5/3 = {5%3}")
