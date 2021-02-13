#! /bin/bash

./config/setting.conf
NAME=$1

python3 irrp.py -r -g$RECV_PIN -f $VAL_FILE $NAME --no-confirm --post 130