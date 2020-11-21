from scraper.scraper import Scraper
from controller.controller import Controller
import threading
import time

def main():
    scraper = Scraper()
    controller = Controller()

    # spawn two threads and run one for any external events (user input etc)
    # run main loop
    scraper_runner = threading.Thread(target=scraper.run)
    controller_runner = threading.Thread(target=controller.run)
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
        print("EXITING")

if __name__ == '__main__':
    main()
