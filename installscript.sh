#!/bin/sh
echo "--- COPY ALL NECESSARY FILES; DISABLE SOME FEATURES; START SERVER ON RP ---"

scp RPServer.py SimonLab_MDDS.bit JSocket.py root@$1:~
scp rc.local root@$1:/etc/rc.local

ssh root@$1 "systemctl disable redpitaya_nginx"
ssh root@$1 "systemctl disable redpitaya_scpi"
ssh root@$1 "systemctl disable jupyter"

ssh root@$1 "chmod +x RPServer.py"

ssh root@$1 "nohup python3 RPServer.py < /dev/null > /dev/null 2>&1 &"
