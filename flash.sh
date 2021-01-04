#!/usr/bin/bash
scp -r sensor/ controller/ scraper/ storage/ envidrawer.py imports.py .env pi@$1:/home/pi/Envidrawer
