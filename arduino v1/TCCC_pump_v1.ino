// Simple arduino sketch that triggers a relay that controls a 12v pump.
// The pump is part of a Casaulty Care Course that simulates a beating heart 
// making a training wound bleed. The system is incorporated into tourniquet
// and pressure dressing training.

// Created by: Jeff Faatz
// https://github.com/jeffreyfaatz
// version 1.0

const int RELAY_PIN = A5;  // Arduino pin to the IN pin of relay

void setup() {
  pinMode(RELAY_PIN, OUTPUT);  // initialize pin A5 as an output
}

void loop() {
  digitalWrite(RELAY_PIN, LOW); // turn on pump for .1 second
  delay(100);
  digitalWrite(RELAY_PIN, HIGH);  // turn off pump for 1 second
  delay(1000);
}
