# SimonLab's approach to use RP

RedPitaya (RP) realtime MDDS, by the SimonLab (lastly updated : February 1, 2017)
> http://simonlab.uchicago.edu/FPGA.html

## File overview
**CLIENT-SIDE (COMPUTER) FILES:**
- DDSMulti_Sequencer.py -> Python 3 script to send data to RP
- MDDS_Test.py -> Python 3 script for testing (here you can configure the signal)
- JSocket.py -> Python 3 helper library for the preceding codes
- installscript -> Shell script that sends the necessary files to the RP, turns off unnecessary services, and starts the server

**SERVER-SIDE (RP) FILES:**
- JSocket.py -> Same as above, but used on the RP for communication as well
- RPServer.py -> The TCP-IP server that runs on the RP to process requests from the client (computer)
- SimonLab_MDDS.bit -> This is the .bit file which is the heart of the device, and acts to configure the reconfigurable hardware of the FPGA within the RP
- rc.local -> Helps the RP to keep the Server running


## SETUP  & TESTING
### Prerequisites
- The RP should be configured to run the latest stable build. For information on preparing a memory card for the RP see: https://redpitaya.readthedocs.io/en/latest/

- The RP must be connected up to the same router as the computer that you intend to use to communicate with it. (This isn't strictly true, but otherwise the communication will require properly routing packets through the router)

- The next step is to be certain that you can communicate between your computer and the redpitaya. Find the redpitaya's IP address by checking "Network manager" on the web-based application menu in your browser (rp-XXXXXX.local/ where XXXXXX is the last six digits of the MAC address) or by using terminal commands. To test the communication, ssh into the RP: in the shell, type `ssh root@rpIP`, and enter "root" as your password

### Testing
1. Next, go to the directory where you have unzipped these files, and in the shell, type `./installscript.sh rpIP` (where rpIP is replaced with the IP/hostname ascertained above)

2. To test out the MDDS, connect OUT1 of the RP to your spectrum analyzer, and in the shell (in the directory of the unzipped files), run (with rpIP replaced with the actual IP address, as above):
`python3 MDDS_Test.py RP_IP=rpRP SOFTWARETRIGGER='1/0' REBOOT='1/0'`,
whereas the default values are SOFTWARETRIGGER=1 and REBOOT=0. Rebooting cleans up the connection thoroughly and restarts the RP

## NOTES:
- If rebooting is enabled, one needs to wait for about 30sec until the RP is back again and may recieve signal sequences again
- To build your own script, simply copy MDDS_Test.py into a new file and modify it; the format of the data to be sent to the MDDS is explained within the .py file, or change the 'CHs_DATA' sequence in this file directly
- installscript.sh disables all web-server functionality for the memory card in RP, and replaces all FPGA functionality; if you would like to use the standard configuration (oscilloscope, signal generator, AWG, etc...) prepare a separate memory card for this purpose, however one can still access oscilloscope, spectrum analyzer etc. functionality by using Pyrpl (https://pyrpl.readthedocs.io/en/latest/index.html)
