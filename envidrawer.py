import scraper
import controller

def main():
    envi_scraper = scraper.Scraper()
    envi_controller = controller.Controller()

    # run main loop
    try:
        while True:
            envi_controller.spin()
            # spin
            envi_scraper.spin()

    except KeyboardInterrupt:
        print("EXITING")

if __name__ == '__main__':
    main()
