import DDSMulti_Sequencer
import re
import sys

NUMCHANNELS=10 #hard-coded into the VERILOG. CANNOT BE CHANGED FOR NOW

############################################# MAIN ROUTINE #################################################

REDPITAYA_IP = "10.22.1.178" #input RP's IP to run procedure
SOFTWARETRIGGER=1
#the next line of code generates the data for each of the 10 simultaneous DDS outputs. The format, for each channel, is:
#[[f_initial in Hz, Amp_initial as fraction of max amplitude],[[time of end of first ramp, freq to ramp to, amplitude to ramp to],[time of end of second ramp, freq to ramp to, amplitude to ramp to],...]]
CHs_DATA=[[[4e6,1],[[4.0,4e6,1]]] * NUMCHANNELS]

DDSMulti_Sequencer.SendDataToRP(REDPITAYA_IP, SOFTWARETRIGGER, CHs_DATA)
