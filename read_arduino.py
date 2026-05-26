import serial
import time
from sklearn.linear_model import LinearRegression
import numpy as np

# -----------------------------
# 1️⃣ Connect to Arduino
# -----------------------------
arduino_port = '/dev/tty.usbserial-A5069RR4'  # Replace with your port
baud_rate = 9600

try:
    arduino = serial.Serial(arduino_port, baud_rate)
    time.sleep(2)  # Wait for Arduino to reset
    print("Connected to Arduino.")
except Exception as e:
    print(f"Error connecting to Arduino: {e}")
    exit()

# -----------------------------
# 2️⃣ Train a simple ML model
# -----------------------------
# Example training data: y = 2*x + 10
X_train = np.array([[0], [20], [40], [60], [80], [100]])
y_train = np.array([10, 50, 90, 130, 170, 210])

model = LinearRegression()
model.fit(X_train, y_train)
print("Linear Regression model trained.")

# -----------------------------
# 3️⃣ Real-time loop: Read → Predict → Send
# -----------------------------
print("Starting real-time prediction...")

while True:
    try:
        # Read data from Arduino
        if arduino.in_waiting > 0:
            data = arduino.readline().decode().strip()
            
            if data.isdigit():
                x = int(data)
                
                # Predict value using Linear Regression
                y_pred = model.predict(np.array([[x]]))[0]
                
                # Print both values
                print(f"Arduino sent: {x} | Predicted: {y_pred:.2f}")
                
                # Send prediction back to Arduino
                arduino.write(f"{int(y_pred)}\n".encode())
                
    except KeyboardInterrupt:
        print("\nExiting...")
        arduino.close()
        break
    except Exception as e:
        print(f"Error: {e}")
