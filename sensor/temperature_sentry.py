from sentry.isentry import ISentry
from pubsub import pub

# Temperature sentry for both all sensor types

class TemperatureSentry(ISentry):
    def __init__(self):
        self.temperature_near = pub.subscribe(self.temperature_near, 'temperature_near')
        self.temperature_far = pub.subscribe(self.temperature_far, 'temperature_far')
        self.temperature_out = pub.subscribe(self.temperature_out, 'temperature_out') # TODO: other temperature points?
        self.current_temperature_near = 0.
        self.current_temperature_far = 0.
        self.current_temperature_out = 0.
        self.low_threshold = 0.5 # TODO: tweak
        self.high_threshold = 0.9 # TODO: tweak

    def temperature_near(self, data):
        self.current_temperature_near = data

    def temperature_far(self, data):
        self.current_temperature_far = data

    def temperature_out(self, data):
        self.current_temperature_out = data

    def check_conditions(self):
        # check if some conditions violated, then send adequate messages
        pass
