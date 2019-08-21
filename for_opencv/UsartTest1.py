#主关于pyseial
import serial.tools.list_ports
import serial
import sys
import os
import time
import re
def main():
    plist=list(serial.tools.list_ports.comports())
    print(plist)
    if len(plist)<=0:
        print('none')
    else:
        plist_0=list(plist[0])
        serialName=plist_0[0]
        serialFd = serial.Serial(serialName, 9600, timeout=60)
        print(serialFd.name)
  

def wait_for_cmd_OK():
    while True:
        line = ser.readline()
        try:
            print(line.decode('utf-8'),end='')
        except:
            pass
        if ( re.search(b'OK',line)):
            break
 
def sendAT_Cmd(serInstance,atCmdStr):
    serInstance.write(atCmdStr.encode('utf-8'))
    wait_for_cmd_OK()

ser = serial.Serial("/dev/ttyACM0",9600,timeout=30) #选择串口号及波特率，因为我是在ubuntu下使用，故串口号为/dev/ttyACM0
sendAT_Cmd(ser,'AT+CFUN=1\r')
ser.close()
    
    
    
    



if __name__=='__main__':
    main()
