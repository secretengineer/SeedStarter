import RPi.GPIO as GPIOimport RPi.GPIO as GPIO # Import the GPIO module for Raspberry Pi
import dht22 # Import the DHT22 module for reading temperature and humidity
import tsl2561 # Import the TSL2561 module for reading light levels
import ph_sensor # Import the pH sensor module for reading pH levels
import lm35 # Import the LM35 module for reading temperature
import time # Import the time module for using the sleep function

# Define the GPIO pin numbers
DHT22_PIN = 17 # Set the DHT22 sensor pin to GPIO17
TSL2561_PIN = 4 # Set the TSL2561 sensor pin to GPIO4
LM35_PIN = 27 # Set the LM35 sensor pin to GPIO27
PH_SENSOR_PIN = 22 # Set the pH sensor pin to GPIO22
RELAY_PIN = 18 # Set the relay pin to GPIO18

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM) # Set the GPIO module to use the BCM (Broadcom) pin numbering scheme
GPIO.setup(DHT22_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set the DHT22 pin as an input and enable the pull-up resistor
GPIO.setup(TSL2561_PIN, GPIO.IN) # Set the TSL2561 pin as an input
GPIO.setup(LM35_PIN, GPIO.IN) # Set the LM35 pin as an input
GPIO.setup(PH_SENSOR_PIN, GPIO.IN) # Set the pH sensor pin as an input
GPIO.setup(RELAY_PIN, GPIO.OUT) # Set the relay pin as an output

# Main control loop
while True:
    # Read sensor data
    h, t = dht22.read_sensor(DHT22_PIN) # Read the temperature and humidity data from the DHT22 sensor
    l = tsl2561.read_sensor(TSL2561_PIN) # Read the light level data from the TSL2561 sensor
    s = lm35.read_sensor(LM35_PIN) # Read the temperature data from the LM35 sensor
    p = ph_sensor.read_sensor(PH_SENSOR_PIN) # Read the pH level data from the pH sensor

    # Determine if the relay should be on or off based on the sensor data
    if t > 25 or h > 60 or l < 100 or s > 25 or p < 6.5:
        GPIO.output(RELAY_PIN, GPIO.HIGH) # Turn the relay on if any of the sensor data meets the specified conditions
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW) # Turn the relay off if none of the sensor data meets the specified conditions

    # Wait for a while before taking the next reading
    time.sleep(5) # Wait for 5 seconds before taking the next reading
import dht22
import tsl2561
import ph_sensor
import lm35
import time

# Define the GPIO pin numbers
DHT22_PIN = 17
TSL2561_PIN = 4
LM35_PIN = 27
PH_SENSOR_PIN = 22
RELAY_PIN = 18

# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(DHT22_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TSL2561_PIN, GPIO.IN)
GPIO.setup(LM35_PIN, GPIO.IN)
GPIO.setup(PH_SENSOR_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Main control loop
while True:
    # Read sensor data
    h, t = dht22.read_sensor(DHT22_PIN)
    l = tsl2561.read_sensor(TSL2561_PIN)
    s = lm35.read_sensor(LM35_PIN)
    p = ph_sensor.read_sensor(PH_SENSOR_PIN)

    # Determine if the relay should be on or off based on the sensor data
    if t > 25 or h > 60 or l < 100 or s > 25 or p < 6.5:
        GPIO.output(RELAY_PIN, GPIO.HIGH)
    else:
        GPIO.output(RELAY_PIN, GPIO.LOW)

    # Wait for a while before taking the next reading
    time.sleep(5)