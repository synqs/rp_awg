#!/bin/sh
echo "--- ENABLE PERMANTENT ACCESS; ENABLE SOME FEATURES; STOP SERVER ON RP; RESET FPGA; FILES REMAIN ---"

ssh root@$1 "cat /opt/redpitaya/fpga/fpga_0.94.bit > /dev/xdevcfg"
ssh root@$1 "systemctl enable redpitaya_nginx && systemctl enable redpitaya_scpi && systemctl enable jupyter"
ssh root@$1 "fuser -k 10000/tcp"
