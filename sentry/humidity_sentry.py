from sentry.isentry import ISentry
from pubsub import pub

# Humidity sentry for both all sensor types

class HumiditySentry(ISentry):
    def __init__(self):
        self.humidity_int_near_sub = pub.subscribe(self.humidity_near, 'humidity_near')
        self.humidity_int_far_sub = pub.subscribe(self.humidity_far, 'humidity_far')
        self.humidity_out_sub = pub.subscribe(self.humidity_out, 'humidity_out')
        self.humidity_soil = pub.subscribe(self.humidity_soil, 'humidity_soil')
        self.current_humidity_near = 0.
        self.current_humidity_far = 0.
        self.current_humidity_out = 0.
        self.current_humidity_soil = 0.
        self.low_threshold = 0.5 # TODO: tweak
        self.high_threshold = 0.9 # TODO: tweak

    def humidity_near(self, data):
        self.current_humidity_near = data

    def humidity_far(self, data):
        self.current_humidity_far = data

    def humidity_out(self, data):
        self.current_humidity_out = data

    def humidity_soil(self, data):
        self.current_humidity_soil = data

    def check_conditions(self):
        # check if some conditions violated, then send adequate messages
        pass
