from scraper.scraper import Scraper
from controller.controller import Controller
from sensor.isensor import ISensor

from typing import List
import threading
import time

def main() -> None:
    scraper: Scraper = Scraper()
    controller: Controller = Controller()
    sensors: List[ISensor] = []

    # register all sensors
    # TODO: add a real sensor and get data running - FAST

    # spawn two threads and run one for any external events (user input etc)
    # run main loop
    scraper_runner: threading.Thread = threading.Thread(target=scraper.run)
    controller_runner: threading.Thread = threading.Thread(target=controller.run)
    try:
        scraper_runner.start()
        controller_runner.start()
        while True:
            time.sleep(0.5)

    except KeyboardInterrupt:
        scraper.is_done = True
        controller.is_done = True
        scraper_runner.join()
        controller_runner.join()

        # deinit all sensors
        for s in sensors:
            s.close()

        print("EXITING")

if __name__ == '__main__':
    main()
