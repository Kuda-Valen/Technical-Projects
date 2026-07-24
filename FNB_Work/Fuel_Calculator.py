"""
    THE SOUTH AFRICAN FUEL COST CALCULATOR
    ======================================

    Create a Quick calculator that:
    1. Ask user how many kilometers they want to drive
    2. Ask them for the current petrol price per liter (can be decima)
    3. Assume their car uses exaclty 1 liter of fuel every 10 kilometers driven
        (fomula: liters_needed = kilometers/10)
    4. Calculate the total cost (liters_needed*petro_price)
    5. Use type casting to ensure your numbers work, and use round() to format the final costs to 2 decimal places
"""

# Started at 1:08

def total_cost_of_fuel(price_per_liter, kilometers):
    liters_needed = kilometers/10
    total_costs = liters_needed * price_per_liter
    return round(total_costs, 2)

if __name__ == "__main__":

    while True:
        print("\n---- Fuel Cost Calculator ----\n")
        print("1. Fuel")
        print("2. Desiel")
        print("3. Exit")

        try:
            option = int(input("Choose an option: "))
            if option == 1:
                price = float(input("Enter price per liter: "))
                kilometers = float(input("Enter distance you want to travel in kilometers: "))
                cost = total_cost_of_fuel(price, kilometers)
                print(f"\nTo travel {kilometers}km, you will need fuel for: R{cost}")

            elif option == 2:
                price = float(input("Enter price per liter: "))
                kilometers = float(input("Enter distance you want to travel in kilometers: "))
                cost = total_cost_of_fuel(price, kilometers)
                print(f"To travel {kilometers}km, you will need fuel for: R{cost}")

            elif option == 3:
                print("Exiting...")
                break

            else:
                print("Enter a valid option:...")

        except ValueError as e:
            print(f"\nEncountered an error: {e}")