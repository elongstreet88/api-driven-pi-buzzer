import flask
from flask import request, jsonify
from time import sleep

#GPIO Zero
from gpiozero import *

#Humidity Sensor
import Adafruit_DHT

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
    sensor = Adafruit_DHT.DHT11
    pin = 27
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return jsonify(temperature)

@app.route('/api/v1/sensor/humidity', methods=['GET'])
def api_sensor_humidity():
    sensor = Adafruit_DHT.DHT11
    pin = 27
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return jsonify(humidity)

app.run(host='0.0.0.0')