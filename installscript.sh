#!/bin/sh
echo "--- COPY ALL NECESSARY FILES; DISABLE SOME FEATURES; START SERVER ON RP ---"

scp RPServer.py SimonLab_MDDS.bit JSocket.py root@$1:~

#ssh root@$1 "systemctl disable redpitaya_nginx"
#ssh root@$1 "systemctl disable redpitaya_scpi"
#ssh root@$1 "systemctl disable jupyter"

ssh root@$1 "nohup python3 /home/RPServer.py > foo.out 2> foo.err < /dev/null &"
