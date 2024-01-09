import RPi.GPIO as GPIO
import time
from pygatt import BLEDevice

# Define GPIO pin for the pump relay
PUMP_PIN = 17  # Change to the GPIO pin you've connected to the relay

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)

# Bluetooth settings
REMOTE_MAC_ADDRESS = 'XX:XX:XX:XX:XX:XX'  # Replace with your remote Bluetooth address
BUTTON_CHAR_UUID = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'  # Replace with your remote button characteristic UUID

def handle_data(sender, data):
    # Handle button press event
    if data[0] == 1:
        GPIO.output(PUMP_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(PUMP_PIN, GPIO.LOW)
        time.sleep(1)

try:
    device = BLEDevice(REMOTE_MAC_ADDRESS)
    device.subscribe(BUTTON_CHAR_UUID, callback=handle_data)

    while True:
        time.sleep(1)  # Keep the script running

except KeyboardInterrupt:
    pass
finally:
    # Cleanup GPIO on script exit
    GPIO.cleanup()
