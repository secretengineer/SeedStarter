import RPi.GPIO as GPIO
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