from sentry.isentry import ISentry
from pubsub import pub

# Water level sentry for the tank

class WaterSentry(ISentry):
    def __init__(self):
        self.water_level_sub = pub.subscribe(self.water_level_cb, 'water_level')
        self.low_threshold = 0.5 # TODO: tweak
        self.high_threshold = 0.9 # TODO: tweak

    def water_level_cb(self, data):
        # if water is below some level, trigger warning
        if data < self.low_threshold:
            pub.sendMessage('water_low', data)
        # else if above trigger other warning
        elif data > self.high_threshold:
            pub.sendMessage('water_high', data) # TODO: display warnings
