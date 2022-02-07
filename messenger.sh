#!/bin/bash
COUNTER=1;
while :
do
    echo "INFO this is goot $COUNTER"
    sleep 1
    echo "ERROR this is bat $COUNTER"
    sleep 1
    ((COUNTER+=1))
done
