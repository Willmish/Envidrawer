from pubsub import pub
#from storage.istorage import IStorage cannot import?
# Data scraper which collects data from sensors (with a given frequency and publishes them)
# periodically saving them to a DB

class Scraper():
    def __init__(self):
        self.update_freq = 50 # in Hz
        self.storage = None # can hotswap the storage?
        self.is_done = False

# spin here in a new thread
    def run(self):
        import time
        while not self.is_done:
            pub.sendMessage('dummy_topic', args="dupa")
            time.sleep(0.5)
