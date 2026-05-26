int ledPin = 13; // Pin connected to LED

void setup() {
  Serial.begin(9600);      // Start serial communication at 9600 baud
  pinMode(ledPin, OUTPUT); // Set LED pin as output
  randomSeed(analogRead(0)); // Seed random number generator using analog noise
}

void loop() {
  // 1. Generate a random number between 0 and 100
  int number = random(0, 101);
  
  // 2. Send the number to Python via Serial
  Serial.println(number);

  // 3. Wait 1 second before next number
  delay(1000);

  // 4. Check if Python sent a prediction back
  if (Serial.available() > 0) {
    int predicted = Serial.parseInt(); // Read predicted value
    
    // 5. Control LED based on prediction
    if (predicted > 60) {
      digitalWrite(ledPin, HIGH); // LED ON
    } else {
      digitalWrite(ledPin, LOW);  // LED OFF
    }
  }
}
