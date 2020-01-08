#!/bin/bash

if [ $1 == "alllightson" ]
then
    ssh dave@192.168.1.2 'bash /var/www/scripts/lights.sh alllightson'
fi

if [ $1 == "alllightsoff" ]
then
    ssh dave@192.168.1.2 'bash /var/www/scripts/lights.sh alllightsoff'
fi
