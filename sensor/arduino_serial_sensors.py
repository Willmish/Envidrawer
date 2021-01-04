from sensor.isensor import ISensor
from pubsub import pub
from imports import logInfo
from time import sleep
import serial

class ArduinoSerialInterface(ISensor):
    get_msg = "get data"
    def __init__(self):
        # Assumes arduino connected to port /dev/tttyACM0, maybe add checking later
        self.arduino_serial: serial.Serial = None

    def serial_connect(self):
        self.arduino_serial = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

    def poll(self):
        self.arduino_serial.write((bytes(ArduinoSerialInterface.get_msg, 'ascii')))
        sleep(0.05) # Wait for arduino to process and send data
        data = self.arduino_serial.readline()#[:-2] # Cut out endline char 
        #data = str(data, encoding='ascii')
        if data:
            logInfo(f"Arduino sent data over serial: {data}")
            pub.sendMessage("sensor_read", args=data)

    def close(self):
        self.arduino_serial.close()
