#!/bin/sh
echo "--- ENABLE PERMANTENT ACCESS; COPY ALL NECESSARY FILES; DISABLE SOME FEATURES; START SERVER ON RP ---"

ssh-copy-id root@$1

scp RPServer.py MDDS.bit JSocket.py root@$1:~
scp rc.local root@$1:/etc/rc.local

ssh root@$1 "systemctl disable redpitaya_nginx && systemctl disable redpitaya_scpi && systemctl disable jupyter"
ssh root@$1 "nohup python3 /root/RPServer.py < /dev/null  > /dev/null 2>&1 &"
