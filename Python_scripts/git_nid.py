# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd
import numpy as np

# initalize the serial port
serialInst = serial.Serial()
pressure = []
time = []
cond = False
plotStrat = True
t = 0
def plot(t,data):
    plt.ion()
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.xlabel('time')
    plt.plot(t,data)
    plt.show()
    plt.pause(0.01)
def plot_start():
    global plotStrat
    plotStrat = True
    print("Start measurements")
def plot_stop():
    global cond
    export = input("Save measurments? y/n")
    if export == 'y':
        data = pd.DataFrame({'time': time, 'pressure': pressure})
        Path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'
        data.to_csv(Path+'/data.csv')
        print("Register measurements")
    else:
        print("Measurements not saved")
    cond = True

def serialPort():
    ports = serial.tools.list_ports.comports()
    portVar = False
    portList = []
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
    return portVar


#------ Creat buttons
root = tk.Tk()
root.title('Real time plot')
root.config(background= 'light blue')
root.geometry('130x50') #set the window size

root.update()
start = tk.Button(root, text= "Start", font= ('calbiri',12), command= lambda: plot_start())
start.place(x= 10, y=10)

root.update()
stop = tk.Button(root, text= "Stop", font= ('calbiri',12), command= lambda: plot_stop())
stop.place(x= start.winfo_x()+start.winfo_reqwidth() + 20, y= 10)

# cheks if port is aviable if not the while loop is never executed
portVar = serialPort()
if portVar == False:
    cond = True
else:
    serialInst.baudrate = 115200
    serialInst.port = portVar
    serialInst.open()
    serialInst.reset_input_buffer()


# While loop that recovers measurements
while True:
    if cond == True:
        print("Rcording is interruped: restart file")
        break
    if serialInst.in_waiting:
        t = t + 10
        bites = serialInst.readline()
        packet = str(bites.decode('utf')).replace('\r\n', '', 1)
        float_or_not = packet.replace('.', '', 1).isdigit()
        if float_or_not == False:
            pressure.append(0)
            time.append(t)
            print(packet)
        else:
            pressure.append(float(packet))
            time.append(t)
        plot(time,pressure)
root.mainloop()



