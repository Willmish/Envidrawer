# Interface for the sensor

class ISensor():
    def poll(self): # group all common functionalities, for closing them etc
        pass

    def close(self):
        pass
