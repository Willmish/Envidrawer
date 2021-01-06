from pubsub import pub
from imports import logInfo, logWarning, logError
from sensor.capacitance_sensor import VerticalCapacitanceSensor, HorizontalCapacitanceSensor
import RPi.GPIO as GPIO

MOTOR2_PINS = (23, 22)
MOTOR1_PINS = (17, 27)
MOTOR1_FORWARD = (0, 1)
MOTOR1_STATIONARY = (0, 0)
MOTOR1_BACKWARD = (1, 0)
MOTOR2_FORWARD = (0, 1)
MOTOR2_STATIONARY = (0, 0)
MOTOR2_BACKWARD = (1, 0)

LED_PIN = 24
FAN_PIN = 13

# Controller class for actuators, subscribes to the data scraper events
class Controller():
    def __init__(self, horizontal_sensor: HorizontalCapacitanceSensor, vertical_sensor: VerticalCapacitanceSensor):
        self.update_freq = 50 # in Hz

        pub.subscribe(self.motion_status_listener, 'motion_status')

        pub.subscribe(self.fans_control, 'fans_control')
        pub.subscribe(self.leds_control, 'fans_control')

        # subscribe to sentry messages (warnings etc)
        self.is_done = False

        # Horizontal and vertical sensors for motor movement
        self.horizontal_sensor = horizontal_sensor
        self.vertical_sensor = vertical_sensor

        self.fan_pwm = GPIO.PWM(FAN_PIN, 200)

# spin here in a new thread
    def run(self):
        self.fan_pwm.start(0)
        import time
        while not self.is_done:
            time.sleep(0.5)

        self.fan_pwm.stop()

    def motion_status_listener(self, args, rest=None):
        # Motor messages: FORWARD, BACKWARD, STOP
        # Position Status: INSIDE, OUTSIDE
        # Message format: [MOTOR_STATUS, POSITION_STATUS]
        logInfo(f"Controller received motion_status message {args}")
        motor_status, position_status = args
        if motor_status == "OUT":
                # TODO remove this
                # IN CASE OF FUCKUP, move out without sensor
                GPIO.output(MOTOR1_PINS[0], MOTOR1_FORWARD[0])
                GPIO.output(MOTOR1_PINS[1], MOTOR1_FORWARD[1])

                GPIO.output(MOTOR2_PINS[0], MOTOR2_FORWARD[0])
                GPIO.output(MOTOR2_PINS[1], MOTOR2_FORWARD[1])

        if motor_status == "STOP":
            GPIO.output(MOTOR1_PINS[0], MOTOR1_STATIONARY[0])
            GPIO.output(MOTOR1_PINS[1], MOTOR1_STATIONARY[1])

            GPIO.output(MOTOR2_PINS[0], MOTOR2_STATIONARY[0])
            GPIO.output(MOTOR2_PINS[1], MOTOR2_STATIONARY[1])
            return
        if position_status == "INSIDE" and motor_status == "BACKWARD":
            logWarning(f"Controller received motion_status message {args}, but position_status is {position_status}\
                        and motor_status is {motor_status}")
            return

        if position_status == "OUTSIDE" and motor_status == "FORWARD":
            logWarning(f"Controller received motion_status message {args}, but position_status is {position_status}\
                        and motor_status is {motor_status}")
            return
        # MOTORS WILL RUN
        # Case 1:  POSITION INSIDE, MOTOR FORWARD
        if position_status == "INSIDE" and motor_status == "FORWARD":
            logInfo(f"Controller received motion_status message {args}, Begin moving outside!")
            pinda_val = self.vertical_sensor.poll()
            if not pinda_val:
                logError(f"Controller received motion_status message {args}, vertical capacitance sensor not triggered before motion began!")
                return
            while pinda_val:
                pinda_val = self.vertical_sensor.poll()
                GPIO.output(MOTOR1_PINS[0], MOTOR1_FORWARD[0])
                GPIO.output(MOTOR1_PINS[1], MOTOR1_FORWARD[1])

                GPIO.output(MOTOR2_PINS[0], MOTOR2_FORWARD[0])
                GPIO.output(MOTOR2_PINS[1], MOTOR2_FORWARD[1])

            GPIO.output(MOTOR1_PINS[0], MOTOR1_STATIONARY[0])
            GPIO.output(MOTOR1_PINS[1], MOTOR1_STATIONARY[1])

            GPIO.output(MOTOR2_PINS[0], MOTOR2_STATIONARY[0])
            GPIO.output(MOTOR2_PINS[1], MOTOR2_STATIONARY[1])
            self.vertical_sensor.close()
            logInfo(f"Controller received motion_status message {args}, Envidrawer is outside!")

        # Case 2:  POSITION OUTSIDE, MOTOR BACKWARD
        if position_status == "OUTSIDE" and motor_status == "BACKWARD":
            pinda_val = self.horizontal_sensor.poll()
            if pinda_val:
                logError(f"Controller received motion_status message {args}, horizontal capacitance sensor triggered before motion began!")
                return
            while not pinda_val:
                pinda_val = self.horizontal_sensor.poll()
                GPIO.output(MOTOR1_PINS[0], MOTOR1_BACKWARD[0])
                GPIO.output(MOTOR1_PINS[1], MOTOR1_BACKWARD[1])

                GPIO.output(MOTOR2_PINS[0], MOTOR2_BACKWARD[0])
                GPIO.output(MOTOR2_PINS[1], MOTOR2_BACKWARD[1])

            GPIO.output(MOTOR1_PINS[0], MOTOR1_STATIONARY[0])
            GPIO.output(MOTOR1_PINS[1], MOTOR1_STATIONARY[1])

            GPIO.output(MOTOR2_PINS[0], MOTOR2_STATIONARY[0])
            GPIO.output(MOTOR2_PINS[1], MOTOR2_STATIONARY[1])
            self.horizontal_sensor.close()
            logInfo(f"Controller received motion_status message {args}, Envidrawer is inside!")

    def fans_control(self, args, rest=None):
        logInfo(f"Controller received fans control message: duty_cycle {args}")
        self.fan_pwm.ChangeDutyCycle(args)

    def leds_control(self, args, rest=None):
        if args == 0:
            logInfo(f"Controller received LEDs control message OFF")
            GPIO.output(LED_PIN, GPIO.LOW)
        else:
            logInfo(f"Controller received LEDs control message ON")
            GPIO.output(LED_PIN, GPIO.HIGH)
