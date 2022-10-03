# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports # Serial library
import matplotlib.pyplot as plt
import tkinter as tk #tkinter for GUI
import pandas as pd # for writing into a .xml file
import time

import numpy as np
Ts = 0.100
# initalize the serial port
serialInst = serial.Serial()
# registered variables
pressure = []
t_val = []
# conditions to start plotting or to stop it and to register measurements
cond = False
cond2 = False
plotStrat = True

# function that plots the Serial data from the arduino
def plot(t,data):
    plt.ion()
    plt.clf()
    plt.title('Serial value from Arduino')
    plt.grid(True)
    plt.ylabel('Values')
    plt.xlabel('time')
    plt.plot(t,data)
    plt.show()
    plt.pause(0.001)
# Fuction triggered by GUI
def plot_start(): # starts measurements when the start btton is applied
    t = 0
    pressure = []
    t_val = []
    global cond
    cond = False
    plt.close()
    print("Start measurements")
    while True: # infinite loop that reads the serial buffer of the Arduino and starts the plot
        if cond == True: # global variable that can interupt the measuremetn
            print("Rcording is interruped: restart file")
            break
        if serialInst.in_waiting: # waits until charcters recived from Arduino
            t = t + Ts
            bites = serialInst.readline() # reads recived bytes
            packet = str(bites.decode('utf')).replace('\r\n', '', 1) # decodes recived bytes and removes \n\r from the reading
            float_or_not = packet.replace('.', '', 1).isdigit() # checks if number is convertible to float
            if float_or_not == False: # if not float append 0 to data vector
                pressure.append(0)
                t_val.append(t)
                print(packet)
            else: # append data vector
                pressure.append(float(packet))
                t_val.append(t)
            if cond2 == False:
                a = len(t_val)
                plot(t_val[a-200:a], pressure[a-200:a]) # actualize the plot after every reading
    #cond = False
def stop_plot():
    global cond2
    cond2 ^= True

def rec_data(): # stp button is applyed the fucktion saves data to measurment file
    global cond
    export = input("Save measurments? y/n") # ask user if he want to measure the ouput
    if export == 'y':
        name = input("Name of .xlsx file:")
        data = pd.DataFrame({'time': t_val, 'pressure': pressure})
        Path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'
        data.to_excel(Path+'/data.xlsx')
        print("Register measurements")
    else:
        print("Measurements not saved")
    cond = True

# fuction that searches if and where a Arduino is connected
def serialPortArduino(): # Searches if Arduino Uno is connecto or not
    """
    Function loops trough serial ports and checks if Arduino uno is connected or not
    Returns: portVar, returns Fals if Arduion Uno is not connect, if connectd returns the port name
    """
    ports = serial.tools.list_ports.comports() #all the aviable ports
    portVar = False
    portList = []
    if len(ports)==0:
        print("No port is conected")

    for onePort in ports: # loops trough all connected ports and appends them to an array
        portName = str(onePort)
        portList.append(portName)
        print(portName)
        if "Arduino Uno" in portName: # checks if one of the ports is an Arduino uno
            portVar = portName[0:5]
            print("Arduino Uno conneced to Port: " + portVar)
        else:
            print("No Arduino Uno conected")
    return portVar # false or portname


#------ Creat buttons of little user interface to control the plot starts etc
root = tk.Tk()
root.title('Real time plot')
root.config(background= 'light blue')
root.geometry('200x50') #set the window size

# Start Button
root.update()
start = tk.Button(root, text= "Start", font= ('calbiri',12), command= lambda: plot_start())
start.place(x= 10, y=10)

# Stop button
root.update()
record = tk.Button(root, text= "Save", font= ('calbiri',12), command= lambda: rec_data())
record.place(x= start.winfo_x()+start.winfo_reqwidth() + 20, y= 10)

# Register data button
root.update()
stop = tk.Button(root, text= "Stop", font= ('calbiri',12), command= lambda: stop_plot())
stop.place(x= record.winfo_x()+record.winfo_reqwidth() + 20, y= 10)
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



