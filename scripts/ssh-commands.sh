#!/bin/bash
touch /tmp/yep.txt
if [ $1 == "alllightson" ]
then
    touch /tmp/on.txt
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/all" -m "on" -q 1
fi

if [ $1 == "alllightsoff" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/all" -m "off" -q 1
fi
