#!/bin/bash

# Run by cron
# Every minute get the data

#Power consumption now
scp dave@192.168.1.2:/var/www/spudooli/power.txt /home/pi/rpi_lcars/scripts/power.txt

#Something
scp dave@192.168.1.2:/var/www/scripts/otherbalance.txt /home/pi/rpi_lcars/scripts/otherbalance.txt

#Weather



