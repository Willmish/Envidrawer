import automationhat
from pubsub import pub
from imports import logInfo, SensorData
from datetime import datetime

class CapacitanceSensor(ISensor):
    # TODO may be necessary to tweak this during debugging,
    # make adjustable for different voltages
    threshold_voltage: float = 5.0
    def __init__(self):
        self.output_pin_no: int = None
        self.analog_input_pin_no: int = None


class HorizontalCapacitanceSensor(CapacitanceSensor):
    def __init__(self):
        super().__init__()
        self.output_pin_no = 2
        self.analog_input_pin_no = 2

    def poll(self):
        # Turns on the sensor (if not already on) and returns a reading
        if not automationhat.output[self.output_pin_no]:
            automationhat.output[self.output_pin_no].write(True)

        raw_data = True if automationhat.analog[analog_input_pin_no].read() < CapacitanceSensor.threshold_voltage else False
        logInfo(f"Horizontal PINDA got reading {raw_data}")
        data = SensorData("capacitance_sensor", "horizontal", "distance", datetime.now(), raw_data)
        pub.sendMessage("sensor_read", args=data)


