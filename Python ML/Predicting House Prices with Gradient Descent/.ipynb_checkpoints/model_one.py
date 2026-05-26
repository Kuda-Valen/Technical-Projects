import numpy as np
import matplotlib.pyplot as plt

# 1. The Dataset
X = np.array([50, 60, 80, 100, 120, 140, 160, 180, 200])
y = np.array([150, 180, 210, 250, 310, 330, 360, 400, 450])

# 2. Then we Initialize parameters
m = 0
b = 0
alpha = 0.0000001
epochs = 1000
n = len(X)

# An array to store all cost function values
cost_history = []

print(f"\n")

# 3. The Gradient Descent Loop
for i in range(epochs):

    
    # Make predictions 
    y_pred = m * X + b

    
    # Compute cost (Mean Squared Error)
    cost = (1/n) * sum((y-y_pred)**2)

    # Compute gradients (dm, db)
    dm = (-2/n) * sum(X * (y - y_pred))
    db = (-2/n) * sum(y - y_pred)

    
    # Update m, b
    m = m - alpha * dm
    b = b - alpha * db

    # Append the cost to the cost_history
    cost_history.append(cost)

    if i % 100 == 0:
        print(f"Epoch {i}, Cost: {cost:.4f}, m: {m:.4f}, b: {b:.4f}")

option = 0

while input !=3:
    print("\n\n1. Use this ML")
    print("2. See the Cost History")
    print("3. Exit")

    option = int(input("Choose an option: "))

    if option == 1: 
        size_input = int(input("Enter the house size (m^2): "))
        predicted_price = m * size_input + b
        print(f"\nPredicted Price for house with {size_input}m^2 is: R{predicted_price:.2f}k")

    elif option == 2:
        print("\n====== Cost Function History ===============")
        
        for i, cost in enumerate(cost_history, start=1):
            print(f"Iteration {i}: {cost:.4f}")


    elif option == 3:
        print("Thank you for using this ML model")
        break

    else: 
        print("Invalid input, Enter valid input")