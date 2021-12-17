from flask import Flask, request, render_template, jsonify
import json
from gpiozero import MCP3008
from time import sleep
"""
To use the MCP3008 chip, you need to enable the SPI interface in
raspberrypi settings, see
https://bc-robotics.com/tutorials/getting-started-raspberry-pi-16-channel-adc-hat-v2/
Howevre I found using the hardware interface a lit flakey, I couldn't initialise all
16 sensors, only the first 8
There might be problems running 2 SPI devices on the hardware
"""

app = Flask(__name__)

sensors=[]
for device in range(0,2):
    for channel in range(1,7):
        print("Creating sensor, " , device, channel)
        sensors.append(MCP3008(channel = channel, device = device))

#sensors.append(MCP3008(channel = 1, device = 1))
@app.route('/', methods=['GET'])
def index():
    """
    returns the main page, template/index.html
    """
    return render_template('index.html')


@app.route('/get_voltage', methods=['POST'])
def get_voltage():
    jsonstring = json.dumps(request.json)
    #index =json.loads(jsonstring).get('index', 0)
    index = int(jsonstring)
    voltage = 0.
    for i in range(5):
	#sample it 5 times for robustness. 
	#We could average it( divide it by 5) 
	#but it's not really necessary
        #voltage += sensors[index].value
        voltage += 0.05

        sleep(0.000)
    print ("index",index,"v=",voltage)
    returnjson = jsonify({'voltage': voltage})
    return returnjson


if __name__ == '__main__':
    app.run(port=5002, threaded=True, host='0.0.0.0')

