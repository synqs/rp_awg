#!/bin/sh
echo "--- COPY ALL NECESSARY FILES; DISABLE SOME FEATURES; START SERVER ON RP ---"

scp RPServer.py SimonLab_MDDS.bit JSocket.py root@$1:~
scp rc.local root@$1:/etc/rc.local
scp FPGAreporter.py root@$1:/usr/bin/FPGAreporter.py

ssh root@$1 "systemctl disable redpitaya_nginx; systemctl disable redpitaya_scpi"

ssh root@$1 "chmod +x RPServer.py; chmod +x /usr/bin/FPGAreporter.py"

ssh root@$1 "nohup python3 RPServer.py < /dev/null > /dev/null 2>&1 &"
ssh root@$1 "nohup python3 /usr/bin/FPGAreporter.py < /dev/null > /dev/null 2>&1 &"
