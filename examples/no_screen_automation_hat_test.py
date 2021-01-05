#!/usr/bin/env python3
import automationhat
from time import sleep, time
sleep(0.1) # Short pause after ads1015 class creation recommended
on = True
automationhat.output[0].write(on)
automationhat.output[1].write(on)

print("begin loop!")
before = time()
while True:
    if (time()-before >=0.5):
        before = time()
        reading1 = automationhat.analog[0].read()
        reading2 = automationhat.analog[1].read()
        print(f"Pinda vertical: {reading1}\nPinda horizontal: {reading2}")
