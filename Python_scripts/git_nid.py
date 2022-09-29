# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports
import matplotlib.pyplot as plt
import tkinter as tk
import pandas as pd
import time

import numpy as np

# initalize the serial port
serialInst = serial.Serial()
pressure = []
t_val = []
cond = False
plotStrat = True
def plot(t,data):
    plt.ion()
    plt.clf()
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.xlabel('time')
    plt.plot(t,data)
    plt.show()
    plt.pause(0.01)
def plot_start(): # starts measurements when the start btton is applied
    t = 0
    global cond
    print("Start measurements")
    while True: # infinite loop that reads the serial buffer of the Arduino and starts the plot
        if cond == True: # global variable that can interupt the measuremetn
            print("Rcording is interruped: restart file")
            break
        if serialInst.in_waiting:
            t = t + 10
            bites = serialInst.readline()
            packet = str(bites.decode('utf')).replace('\r\n', '', 1)
            float_or_not = packet.replace('.', '', 1).isdigit()
            if float_or_not == False:
                pressure.append(0)
                t_val.append(t)
                print(packet)
            else:
                pressure.append(float(packet))
                t_val.append(t)
            plot(t_val, pressure)
    #cond = False

def plot_stop(): # stp button is applyed the fucktion saves data to measurment file
    global cond
    export = input("Save measurments? y/n") # ask user if he want to measure the ouput
    if export == 'y':
        data = pd.DataFrame({'time': t_val, 'pressure': pressure})
        Path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'
        data.to_excel(Path+'/data.xlsx')
        print("Register measurements")
    else:
        print("Measurements not saved")
    cond = True

def serialPortArduino(): # Searches if Arduino Uno is connecto or not
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
    return portVar # returns Fals if Arduion Uno is not connect, if connectd returns the port name


#------ Creat buttons of little user interface to control the plot starts etc
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

root.update()
stop = tk.Button(root, text= "Stop", font= ('calbiri',12), command= lambda: plot_stop())
stop.place(x= start.winfo_x()+start.winfo_reqwidth() + 20, y= 10)
root.update()
########### Initialise the Serial port if Arduino is connected
portVar = serialPortArduino()
if portVar == False:
    cond = True
else:
    serialInst.baudrate = 115200
    serialInst.port = portVar
    serialInst.open()
    serialInst.reset_input_buffer()
if portVar: # if Arduino is connected starts the GUI in loop
    root.mainloop()



