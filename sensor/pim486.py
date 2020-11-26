from isensor import ISensor
from bme280 import BME280
from pubsub import pub

class PIM486(ISensor):
    def __init__(self):
        self.bme280 = BME280()
        pass

    def poll(self): # some sensors are poll'able
        raw_temp = self.bme280.get_temperature()
        print(f"PIM486 got temp {raw_temp}")
        pub.sendMessage('sensor_read', args=raw_temp)


    def close(self):
        pass
