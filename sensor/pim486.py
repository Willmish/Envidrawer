from sensor.isensor import ISensor
from bme280 import BME280
from ltr559 import LTR559
from pubsub import pub
from imports import logInfo, SensorData
from datetime import datetime

class PIM486(ISensor):
    def __init__(self):
        self.bme280 = BME280()
        self.ltr559 = LTR559()

    def poll(self): # some sensors are poll'able
        raw_temp = self.bme280.get_temperature()
        raw_humidity = self.bme280.get_humidity()
        raw_press = self.bme280.get_pressure()


        logInfo(f"PIM486 got temp {raw_temp}")
        data = SensorData("pim486", "bme280", "temperature", datetime.now(), raw_temp)
        pub.sendMessage('sensor_read', args=data)
        pub.sendMessage('temperature_out', raw_temp)

    def close(self):
        pass

    # TODO: add the LCD displaying
