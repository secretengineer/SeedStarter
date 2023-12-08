import RPi.GPIO as GPIO
import time
import requests
import json
from datetime import datetime

# Pin definition
LIGHT_SENSOR_PIN = 7
SEEDLING_HEAT_MAT_PIN = 11
GREENHOUSE_LIGHT_PIN = 13

# Setup the pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)
GPIO.setup(SEEDLING_HEAT_MAT_PIN, GPIO.OUT)
GPIO.setup(GREENHOUSE_LIGHT_PIN, GPIO.OUT)

# Temperature and light thresholds
TEMP_THRESHOLD = 20
LIGHT_THRESHOLD = 300

# URL to access weather API
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather?q=CityName&appid=APIKEY"

def is_dark():
    try:
        response = requests.get(WEATHER_API_URL)
        data = response.json()
        sunset_time = data['sys']['sunset']
        current_time = time.time()

        return current_time > sunset_time
    except:
        print("Error occurred when trying to get weather data.")
        return False

def check_temperature():
    try:
        response = requests.get("http://YourRaspberryPiIPAddress/temperature")
        data = response.json()

        return data['temperature'] > TEMP_THRESHOLD
    except:
        print("Error occurred when trying to get temperature data.")
        return False

def monitor():
    while True:
        time.sleep(10)
        is_light_on = GPIO.input(LIGHT_SENSOR_PIN)
        temperature_check = check_temperature()
        dark = is_dark()

        if not is_light_on and temperature_check and dark:
            GPIO.output(SEEDLING_HEAT_MAT_PIN, GPIO.HIGH)
            GPIO.output(GREENHOUSE_LIGHT_PIN, GPIO.HIGH)
        else:
            GPIO.output(SEEDLING_HEAT_MAT_PIN, GPIO.LOW)
            GPIO.output(GREENHOUSE_LIGHT_PIN, GPIO.LOW)

monitor()