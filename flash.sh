#!/usr/bin/bash
scp -r sensor/ controller/ scraper/ storage/ envidrawer.py imports.py .env requirements.txt pi@$1:/home/pi/Envidrawer
