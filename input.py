from pubsub import pub
from RPi import GPIO

class Input():
    def __init__(self):
        self.status = "OUTSIDE"
        self.MOTOR1_PINS = [17, 27]
        self.MOTOR2_PINS = [23, 22]

    def user_prompt(self):
        try:
            while True:
                user_input = input("Welcome to Envidrawer what to do?\n" +
                                   "1 - Turn ON LEDs\n" +
                                   "2 - Turn OFF LEDs\n" +
                                   "3 - Turn ON Fans\n" +
                                   "4 - Turn OFF Fans\n" +
                                   "5 - Move FORWARDS\n" +
                                   "6 - Move BACKWARDS\n" +
                                   "7 - STOP\n" +
                                   "8 - Water pump ON\n" +
                                   "9 - Water pump OFF\n" +
                                   "10 - Move FORWARDS NO PINDA\n"
                                   )
                print(user_input)
                if int(user_input) < 1 or int(user_input) > 10:
                    user_input = None
                self.interpret_user_input(user_input)

        except KeyboardInterrupt:
            GPIO.write(self.MOTOR1_PINS, 0)
            GPIO.write(self.MOTOR2_PINS, 0)
            user_input = None
            return

    def interpret_user_input(self, inp):
        if inp is None:
            return

        inp = int(inp)
        if inp == 1:
            pub.sendMessage("leds_control", args=1)
        elif inp == 2:
            pub.sendMessage("leds_control", args=0)
        elif inp == 3:
            pub.sendMessage("fans_control", args=100) # TODO: fix pwm
        elif inp == 4:
            pub.sendMessage("fans_control", args=0) # TODO: fix pwm
        elif inp == 5:
            pub.sendMessage("motion_status", args=["FORWARD", self.status])
            self.status = "OUTSIDE"
        elif inp == 6:
            pub.sendMessage("motion_status", args=["BACKWARD", self.status])
            self.status = "INSIDE"
        elif inp == 7:
            pub.sendMessage("motion_status", args=["STOP", self.status])
        elif inp == 8:
            pass
            #pub.sendMessage("pump_control", args=1) # TODO: relay burned!!!?
        elif inp == 9:
            pass
            #pub.sendMessage("pump_control", args=0) # TODO: relay burned!!!?
        elif inp == 10:
            pub.sendMessage("motion_status", args=["OUT", self.status])
