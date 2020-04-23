#!/bin/sh
echo "-----COPY REQUIRED FILES TO REDPITAYA-----"

scp rp_files/RPServer.py root@$1:~
scp rp_files/SimonLab_FIRVNA.bit root@$1:~
scp rp_files/JSocket.py root@$1:~
scp rp_files/rc.local root@$1:/etc/rc.local
scp rp_files/FPGAreporter.py root@$1:/usr/bin/FPGAreporter.py

ssh root@$1 systemctl disable redpitaya_nginx
#ssh root@$1 systemctl disable redpitaya_wyliodrin
ssh root@$1 systemctl disable redpitaya_scpi
ssh root@$1 nohup python3 RPServer.py </dev/null >/dev/null 2>&1 &
ssh root@$1 nohup python3 /usr/bin/FPGAreporter.py </dev/null >/dev/null 2>&1 &
