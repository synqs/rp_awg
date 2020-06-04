#!/bin/sh
echo "--- ENABLE SOME FEATURES; RESET FPGA ---"

ssh root@$1 "systemctl enable redpitaya_nginx && systemctl enable redpitaya_scpi && systemctl enable jupyter"
ssh root@$1 "cat /opt/redpitaya/fpga/fpga_0.94.bit > /dev/xdevcfg"
ssh root@$1 "reboot"
