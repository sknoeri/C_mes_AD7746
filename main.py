# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def livPlot(i):


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portList = []
    portVar = None
    pressure = 0;

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
    #val = input("select Port: COM")
    if portVar:
        serialInst.baudrate = 115200
        serialInst.port = portVar
        serialInst.open()

        while True:
            if serialInst.in_waiting:
                packet = serialInst.readline()
                pressure = float(packet.decode('utf'))
                print(type(pressure))

    #print(val)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
