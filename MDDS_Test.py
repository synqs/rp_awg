import DDSMulti_Sequencer
import re
import sys

NUMCHANNELS=10 #hard-coded into the VERILOG. CANNOT BE CHANGED FOR NOW

############################################# MAIN ROUTINE #################################################

REDPITAYA_IP = "10.22.1.178" #input RP's IP to run procedure
SOFTWARETRIGGER=1
#the next line of code generates the data for each of the 10 simultaneous DDS outputs. The format, for each channel, is:
#[[f_initial in Hz, Amp_initial as fraction of max amplitude],[[time of end of first ramp, freq to ramp to, amplitude to ramp to],[time of end of second ramp, freq to ramp to, amplitude to ramp to],...]]
CHs_DATA=[[     [50e6, 1.00], [[4.0, 50e6, 1.00]], #ch0
                [10e6, 0.00], [[4.0, 10e6, 0.00]], #ch1
                [15e6, 0.00], [[4.0, 15e6, 0.00]], #ch2
                [20e6, 0.00], [[4.0, 20e6, 0.00]], #ch3
                [25e6, 0.00], [[4.0, 25e6, 0.00]], #ch4
                [30e6, 0.00], [[4.0, 30e6, 0.00]], #ch5
                [35e6, 0.00], [[4.0, 35e6, 0.00]], #ch6
                [40e6, 0.00], [[4.0, 40e6, 0.00]], #ch7
                [45e6, 0.00], [[4.0, 45e6, 0.00]], #ch8
                [50e6, 0.00], [[4.0, 50e6, 0.00]]  #ch9
                    ]]

DDSMulti_Sequencer.SendDataToRP(REDPITAYA_IP, SOFTWARETRIGGER, CHs_DATA)
