#!/usr/bin/bash
scp -r sensor/ controller/ scraper/ storage/ envidrawer.py imports.py pi@$1:/home/pi/Envidrawer
