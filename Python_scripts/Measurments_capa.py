# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports
import matplotlib.pyplot as plt
import numpy as np

# initalize the serial port
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []
portVar = False
pressure = []
time = []
t = 0
cond = True
plt.ion()
alpfhabet = ['a','b','c','d','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','+','!','*','?','/','$']

def plot():
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.xlabel('time')
    plt.plot(time,pressure)
    plt.show()
    plt.pause(0.01)

if len(ports)==0:
    print("No port is conected")
for onePort in ports:
    portName = str(onePort)
    portList.append(portName)
    print(portName)
    if "Arduino Uno" in portName:
        portVar = portName[0:5]
        print("Arduino Uno conneced to Port: " + portVar)
    else:
        print("No Arduino Uno conected")
    if portVar:
        serialInst.baudrate = 115200
        serialInst.port = portVar
        serialInst.open()
        serialInst.reset_input_buffer()
        while True:
            if serialInst.in_waiting:
                t = t+1
                bites = serialInst.readline()
                packet = str(bites.decode('utf')).replace('\r\n','',1)
                float_or_not = packet.replace('.','', 1).isdigit()
                if float_or_not == False:
                    pressure.append(0)
                    time.append(t)
                    print(packet)
                else:
                    pressure.append(float(packet))
                    time.append(t)
                plot()


