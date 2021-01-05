from sentry.isentry import ISentry
from pubsub import pub

# Light sentry for both all sensor types

class LightSentry(ISentry):
    def __init__(self):
        self.light_int_sub = pub.subscribe(self.light_int, 'light_int')
        self.light_out_sub = pub.subscribe(self.light_out, 'light_out')
        self.current_luminosity_int = 0.
        self.current_luminosity_out = 0.
        self.low_threshold = 0.5 # TODO: tweak
        self.high_threshold = 0.9 # TODO: tweak

    def light_int(self, data):
        self.current_luminosity_int = data

    def light_out(self, data):
        self.current_luminosity_out = data

    def check_conditions(self):
        # check if some conditions violated, then send adequate messages
        pass
