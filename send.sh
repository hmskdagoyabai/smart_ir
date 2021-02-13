
#! /bin/bash

. ./config/setting.conf
NAME=$1

python3 irrp.py -p -g$SEND_PIN -f $VAL_FILE $NAME
