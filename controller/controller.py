from pubsub import pub

# Controller class for actuators, subscribes to the data scraper events
class Controller():
    def __init__(self):
        self.update_freq = 50 # in Hz

        pub.subscribe(self.dummy_listener, 'dummy_topic')
        self.is_done = False

# spin here in a new thread
    def run(self):
        import time
        while not self.is_done:
            time.sleep(0.5)

    def dummy_listener(self, args, rest=None):
        print(f"Received message {args}")
