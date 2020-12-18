from sensor.isensor import ISensor
from bme280 import BME280
from pubsub import pub
from imports import logInfo, SensorData
from datetime import datetime

class PIM486(ISensor):
    def __init__(self):
        self.bme280 = BME280()

    def poll(self): # some sensors are poll'able
        raw_temp = self.bme280.get_temperature()
        logInfo(f"PIM486 got temp {raw_temp}")
        data = SensorData("pim486", "bme280", "temperature", datetime.now(), raw_temp)
        pub.sendMessage('sensor_read', args=data)

    def close(self):
        pass
