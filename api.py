import flask
from flask import request, jsonify
from gpiozero import *
from time import sleep

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return """
<h1>Alarm Prototype</h1>

<h2>Ensure buzzer is hooked up to pin 17 of RasberryPI GPIO<h2>

<h3>To turn on: <a href="/api/v1/alarm/on">/api/v1/alarm/on</a></h3>
<h3>To turn off: <a href="/api/v1/alarm/off">/api/v1/alarm/off</a></h3>
    """


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/alarm/on', methods=['GET'])
def api_alarm_on():
    bz = Buzzer(17)
    bz.on()
    sleep(1)
    return jsonify("on")

@app.route('/api/v1/alarm/off', methods=['GET'])
def api_alarm_off():
    bz = Buzzer(17)
    bz.off()
    sleep(1)
    return jsonify("off")

app.run(host='0.0.0.0')