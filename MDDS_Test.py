import DDSMulti_Sequencer
import re
import sys
import os

NUMCHANNELS=10 #hard-coded into the VERILOG. CANNOT BE CHANGED FOR NOW

############################################# HELPER FUNCTIONS #############################################
def getparmval(strIn,parmname,defaultval):
    strlist=re.findall(parmname+"=([\w\a\.-]*)",strIn)
    if(len(strlist)>0):
        outval=strlist[0]
    else:
        outval=defaultval
    print(parmname+": "+outval)
    return outval


############################################# MAIN ROUTINE #################################################
cmdstr=""
for tARG in sys.argv:
    cmdstr=cmdstr+" "+tARG
REDPITAYA_IP = getparmval(cmdstr, "RP_IP","10.22.1.178") #IF THE CALL TO DDS_SEQUENCER CONTAINS CMD LINE ARGUMENT "RP_IP=XXX.XXX.XXX.XXX" THAT IS USED INSTEAD OF THE DEFAULT AT RIGHT
SOFTWARETRIGGER = getparmval(cmdstr, "SOFTWARETRIGGER","1")
REBOOT = getparmval(cmdstr, "REBOOT","0")

#the next line of code generates the data for each of the 10 simultaneous DDS outputs. The format, for each channel, is:
#[[f_initial in Hz, Amp_initial as fraction of max amplitude],[[time of end of first ramp, freq to ramp to, amplitude to ramp to],[time of end of second ramp, freq to ramp to, amplitude to ramp to],...]]
CHs_DATA=[      [[30e6, 1.00], [[0.0, 30e6, 1.00]]], #ch0
                # [[10e6, 0.00], [[0.0, 10e6, 0.00]]], #ch1
                # [[15e6, 0.00], [[0.0, 15e6, 0.00]]], #ch2
                # [[20e6, 0.00], [[0.0, 20e6, 0.00]]], #ch3
                # [[25e6, 0.00], [[0.0, 25e6, 0.00]]], #ch4
                # [[30e6, 0.00], [[0.0, 30e6, 0.00]]], #ch5
                # [[35e6, 0.00], [[0.0, 35e6, 0.00]]], #ch7
                # [[40e6, 0.00], [[0.0, 40e6, 0.00]]], #ch6
                # [[45e6, 0.00], [[0.0, 45e6, 0.00]]], #ch8
                # [[50e6, 0.00], [[0.0, 50e6, 0.00]]]  #ch9
                    ]
# CHs_DATA=[[[(2*k)*10.0**6.0,0.05],[[4.0,(4*k)*10.0**6.0,0.05*(((k-4.5)**2)/25.0)],[8.0,(2*k)*10.0**6.0,0.05]]] for k in range(NUMCHANNELS)]

#always start server everytime we send a sequence...?
#os.system("ssh root@"+REDPITAYA_IP+" 'nohup python3 /root/RPServer.py < /dev/null > /dev/null 2>&1 &'")
DDSMulti_Sequencer.SendDataToRP(REDPITAYA_IP, SOFTWARETRIGGER, CHs_DATA, REBOOT)
