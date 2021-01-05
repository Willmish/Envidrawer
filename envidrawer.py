from scraper.scraper import Scraper
from controller.controller import Controller
from sensor.isensor import ISensor
from sentry.isentry import ISentry
# sensors
from sensor.pim486 import PIM486
from sensor.arduino_serial_sensors import ArduinoSerialInterface
from sensor.capacitance_sensor import VerticalCapacitanceSensor, HorizontalCapacitanceSensor
# sentries
from sentry.humidity_sentry import HumiditySentry
from sentry.light_sentry import LightSentry
from sentry.water_sentry import WaterSentry
from sentry.temperature_sentry import TemperatureSentry
# internal
from imports import logger, logInfo
from storage.db import DBStorage

from typing import List
import threading
import time

def main() -> None:

    logger.setLevel('INFO')
    scraper: Scraper = Scraper(DBStorage())
    controller: Controller = Controller()
    sensors: List[ISensor] = []
    sentries: List[ISentry] = []

    # TODO: add LCD display?

    # register all sensors
    sensors.append(PIM486())
    sensors.append(ArduinoSerialInterface())
    sensors.append(VerticalCapacitanceSensor())
    sensors.append(HorizontalCapacitanceSensor())

    # register all sentries
    sentries.append(HumiditySentry())
    sentries.append(LightSentry())
    sentries.append(WaterSentry())
    sentries.append(TemperatureSentry())

    # spawn two threads and run one for any external events (user input etc)
    # run main loop
    scraper_runner: threading.Thread = threading.Thread(target=scraper.run, name="Scraper")
    controller_runner: threading.Thread = threading.Thread(target=controller.run, name="Controller")
    try:
        scraper_runner.start()
        controller_runner.start()
        while True:
            for s in sensors:
                s.poll() # poll for data for most of the sensors

            time.sleep(0.5)

    # poll the sensors periodically, serve IRQ's from some most important - pindas etc
    except KeyboardInterrupt:
        scraper.is_done = True
        controller.is_done = True
        scraper_runner.join()
        controller_runner.join()

        # deinit all sensors
        for s in sensors:
            s.close()

        logInfo("Exiting")

if __name__ == '__main__':
    main()
