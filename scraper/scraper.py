import pypubsub
# Data scraper which collects data from sensors (with a given frequency and publishes them)
# periodically saving them to a DB

class Scraper():
    def __init__(self):
        self.update_freq = 50 # in Hz
        self.DB = None

    def spin(self):
        pass
