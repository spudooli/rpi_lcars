#!/bin/bash

if [ $1 == "alllightson" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/all" -m "on" -q 1
fi

if [ $1 == "alllightsoff" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/all" -m "off" -q 1
fi

if [ $1 == "outsidelightsson" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/outside" -m "on" -q 1
fi

if [ $1 == "outsidelightsoff" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/outside" -m "off" -q 1
fi

if [ $1 == "livingroomlightson" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/livingroom" -m "on" -q 1
fi

if [ $1 == "livingroomlightsoff" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/livingroom" -m "off" -q 1
fi

if [ $1 == "frontdoorlighton" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/frontdoorlighton" -m "on" -q 1
fi

if [ $1 == "frontdoorlightoff" ]
then
    mosquitto_pub -h 192.168.1.2 -p 1883 -t "house/lights/frontdoorlightoff -m "off" -q 1
fi