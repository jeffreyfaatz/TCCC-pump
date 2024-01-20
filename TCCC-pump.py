import RPi.GPIO as GPIO
import time

# Define GPIO pins
relay_pin = 4
switch_pin = 17  # Replace 'button_pin' with 'switch_pin'

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set pin modes
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor

try:
    while True:
        switch_state = GPIO.input(switch_pin) == False  # Check switch state

        print("Switch state:", switch_state)  # Log switch state

        if switch_state:  # Switch is ON
            GPIO.output(relay_pin, GPIO.HIGH)  # Turn on pump
            print("Pump activated")
        else:  # Switch is OFF
            GPIO.output(relay_pin, GPIO.LOW)  # Turn off pump
            print("Pump deactivated")

        time.sleep(0.1)  # Short delay for stability

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on exit
