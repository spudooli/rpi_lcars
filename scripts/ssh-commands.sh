#!/bin/bash
touch /tmp/yep.txt
if [ $1 == "alllightson" ]
then
    touch /tmp/on.txt
    ssh dave@192.168.1.2 'bash /var/www/scripts/lights.sh alllightson'
fi

if [ $1 == "alllightsoff" ]
then
    ssh dave@192.168.1.2 'bash /var/www/scripts/lights.sh alllightsoff'
fi
