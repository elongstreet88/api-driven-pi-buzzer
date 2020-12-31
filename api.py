import flask
from flask import request, jsonify
from time import sleep

#GPIO Zero
from gpiozero import *

#Humidity Sensor
#Borrowed from [https://pypi.org/project/dht11/]
import RPi.GPIO as GPIO
import dht11

#Functions
def read_dht11(pin):
    GPIO.setmode(GPIO.BCM)
    instance = dht11.DHT11(pin = pin)

    #We have to try this a few times as it doesn't always work
    #See [https://raspberrypi.stackexchange.com/questions/80037/frequent-missing-data-error-on-dht11]
    max_attempts = 10
    while True:
        result = instance.read()
        if result.is_valid():
            return result
        max_attempts -= 1
        
    return result

def read_dht11_temperature(pin):
    result = read_dht11(pin=pin)
    if result.is_valid():
        return "%-3.1f°F" % (result.temperature * 1.8 + 32)
    else:
        return "Error: %d" % result.error_code

def read_dht11_humidity(pin):
    result = read_dht11(pin=pin)
    if result.is_valid():
        return "%-3.1f%%" % result.humidity
    else:
        return "Error: %d" % result.error_code

#Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return """
<h1>Alarm Prototype</h1>

<h2>Ensure [Keyes buzzer] is hooked up to pin GPIO17 of RasberryPI GPIO.<h2>
<h2>Ensure [DHT11 Sensor] is hooked up to pin GPIO27 of RasberryPI GPIO.<h2>

<h3>To turn on: <a href="/api/v1/alarm/on">/api/v1/alarm/on</a></h3>
<h3>To turn off: <a href="/api/v1/alarm/off">/api/v1/alarm/off</a></h3>
<h3>Get Temperature: <a href="/api/v1/sensor/temperature">/api/v1/sensor/temperature</a></h3>
<h3>Get Humidity: <a href="/api/v1/sensor/humidity">/api/v1/sensor/humidity</a></h3>
"""

#Routes
@app.route('/api/v1/alarm/on', methods=['GET'])
def api_alarm_on():
    bz = Buzzer(pin=17)
    bz.on()
    sleep(1)
    return jsonify("on")

@app.route('/api/v1/alarm/off', methods=['GET'])
def api_alarm_off():
    bz = Buzzer(pin=17)
    bz.off()
    sleep(1)
    return jsonify("off")

@app.route('/api/v1/sensor/temperature', methods=['GET'])
def api_sensor_temperature():
    result = read_dht11_temperature(pin=27)
    return result

@app.route('/api/v1/sensor/humidity', methods=['GET'])
def api_sensor_humidity():
    result = read_dht11_humidity(pin=27)
    return result

app.run(host='0.0.0.0')