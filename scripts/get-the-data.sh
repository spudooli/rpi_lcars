#!/bin/bash

# Run by cron
# Every minute get the data

#Power consumption now
#Sscp dave@192.168.1.2:/var/www/spudooli/power.txt /home/pi/rpi_lcars/scripts/power.txt

#Something
#scp dave@192.168.1.2:/var/www/scripts/otherbalance.txt /home/pi/rpi_lcars/scripts/otherbalance.txt

#Weather
scp dave@192.168.1.2:/tmp/weather.txt /home/pi/rpi_lcars/scripts/weather.txt

scp dave@192.168.1.2:/tmp/saturday.txt /home/pi/rpi_lcars/scripts/saturday.txt
scp dave@192.168.1.2:/tmp/sunday.txt /home/pi/rpi_lcars/scripts/sunday.txt

scp dave@192.168.1.2://var/www/scripts/statusfile.json /home/pi/rpi_lcars/scripts/statusfile.json

#python /home/pi/rpi_lcars/scripts/assemble-the-status-file.py
