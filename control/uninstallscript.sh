#!/bin/sh
echo "UNINSTALLING-------------------------------------------------------------"

ssh root@$1 'rm ~/RPServer.py SimonLab_FIRVNA.bit JSocket.py'
ssh root@$1 'rm /etc/rc.local'
ssh root@$1 'rm /usr/bin/FPGAreporter.py'

ssh root@$1 systemctl enable redpitaya_nginx
ssh root@$1 systemctl enable redpitaya_wyliodrin
ssh root@$1 systemctl enable redpitaya_scpi


ssh root@$1 ps -ef |grep nohup
#ssh root@$1 nohup python RPServer.py </dev/null >/dev/null 2>&1 &
#ssh root@$1 nohup python /usr/bin/FPGAreporter.py </dev/null >/dev/null 2>&1 &
