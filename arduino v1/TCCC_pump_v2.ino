// Simple arduino sketch that triggers a relay that controls a 12v pump.
// The pump is part of a Casaulty Care Course that simulates a beating heart
// making a training wound bleed. The system is incorporated into tourniquet
// and pressure dressing training.

// Created by: Jeff Faatz
// https://github.com/jeffreyfaatz
// version 2.0

const int RELAY_PIN = A5;    // Arduino pin to IN on relay
const char BUTTON_PIN = A4;  // Arduino pin to button
bool pressed = false;        // Variable is used to store the state of the button

void setup() {
  Serial.begin(115200);

  pinMode(RELAY_PIN, OUTPUT);         // Set pin A5 as an output
  pinMode(BUTTON_PIN, INPUT_PULLUP);  // Set pin A4 with internal pull up resistor
}

void loop() {
  bool currentState = digitalRead(BUTTON_PIN);  // Reads the current state of the button

  if (currentState == pressed) {
    digitalWrite(RELAY_PIN, LOW);   // Sets the RELAY_PIN to a low state, activating the relay
    Serial.println("On");
    delay(100);                     // Runs for 100 milliseconds (.1 second)
    digitalWrite(RELAY_PIN, HIGH);  // Sets the RELAY_PIN back to a high state, deactivating the relay
    Serial.println("Off");
    delay(1000);                    // Waits for 1000 milliseconds (1 second)
  }
}