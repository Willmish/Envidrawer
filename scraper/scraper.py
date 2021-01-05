from pubsub import pub
from imports import logInfo, SensorData
from storage.istorage import IStorage
#from storage.istorage import IStorage cannot import?
# Data scraper which collects data from sensors (with a given frequency and publishes them)
# periodically saving them to a DB

# Scraper subscribes to sensor messages, which define their type in the header
# the main loops just updates the data stuff, the callback threads do readouts of the sensor values

class Scraper():
    def __init__(self, storage: IStorage):
        self.update_freq = 50 # in Hz
        self.storage = storage # can hotswap the storage?
        self.is_done = False
        pub.subscribe(self.sensor_read_cb, 'sensor_read')
        self.message_queue = []

    def sensor_read_cb(self, args: SensorData=None):
        #logInfo(f"Obtained the reading! DATA: {args}")
        self.message_queue.append(args) # TODO:  thread safe list

# spin here in a new thread
    def run(self):
        import time
        while not self.is_done:
#            pub.sendMessage('dummy_topic', args="dupa")


            self.storage.write_all(self.message_queue)
            self.message_queue.clear()
            time.sleep(0.5)

        self.storage.write_all(self.message_queue) # do last one flush of data and die

