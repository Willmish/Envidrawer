import pypubsub

# Controller class for actuators, subscribes to the data scraper events
class Controller():
    def __init__(self):
        self.update_freq = 50 # in Hz

    def spin(self):
        pass
