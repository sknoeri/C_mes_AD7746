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
recordStop = True
onOffPlot = False
comOpen = False
Path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'

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
def record_data(): # starts measurements when the start btton is applied
    t = 0
    pressure = []
    t_val = []
    global recordStop
    if(recordStop == True and comOpen != False):
        recordStop =False
        plt.close()
        record.config(image=on)
        print("Start measurements")
    else:
        recordStop = True
        record.config(image=off)
    while True: # infinite loop that reads the serial buffer of the Arduino and starts the plot
        if(recordStop == True or comOpen == False): # global variable that can interupt the measuremetn
            if comOpen == False:
                print("No arduino Uno connected")
            else:
                print("Rcording is interruped")
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
            if onOffPlot == True: ## hadels the start and stop of the data plot
                a = len(t_val)
                plot(t_val[a-200:a], pressure[a-200:a]) # actualize the plot after every reading
            else:
                #plt.clf()
                root.update()
# Turns on/off the plot
def OnOff_plot():
    global onOffPlot
    if onOffPlot== False:
        plotOnOff.config(image=on)
        onOffPlot = True
    else:
        plotOnOff.config(image=off)
        onOffPlot = False

def save_data(): # stp button is applyed the fucktion saves data to measurment file
    if (len(t_val)>0):
        if(inputtxt.get()==''):
            name = 'NoName'
        else:
            name = inputtxt.get()
        data = pd.DataFrame({'time': t_val, 'pressure': pressure})
        data.to_excel(Path+'/' + name +'.xlsx')
        print("Register measurements")
    else:
        print("Emty file")

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
########### Initialise the Serial port if Arduino is connected
def comActive():
    global comOpen
    portVar = serialPortArduino()
    if(portVar == False or comOpen==True):
        comOpen = False
        serialInst.close()
        startSerial.config(image=off)
    else:
        serialInst.baudrate = 115200
        serialInst.port = portVar
        serialInst.open()
        serialInst.reset_input_buffer()
        startSerial.config(image=on)
        comOpen = True

#------ Creat buttons of little user interface to control the plot starts etc
root = tk.Tk()
root.title('Real time plot')
root.config(background= 'light blue')
root.geometry('400x200') #set the window size

#define fgures
on = tk.PhotoImage(file=Path + "/Python_scripts/on.png")
off = tk.PhotoImage(file=Path + "/Python_scripts/off.png")

# Register data button
serialLabel = tk.Label(root, text="Serial On/Off", font= ('calbiri', 15))
serialLabel.place(x = 10, y = 20)
root.update()
startSerial = tk.Button(root, image=off, font= ('calbiri',12), command= lambda: comActive()) #text= "Serial On/Off",
startSerial.place(x= serialLabel.winfo_x()+serialLabel.winfo_width()+20, y=10)

# Start Button
root.update()
recordLabel = tk.Label(root, text="Record On/Off", font= ('calbiri', 15))
recordLabel.place(x = 10, y = serialLabel.winfo_y()+50)
root.update()
record = tk.Button(root, image=off,  command= lambda: record_data())
record.place(x= recordLabel.winfo_x()+recordLabel.winfo_width()+20, y=recordLabel.winfo_y()-8)

# Plot on off
plotLabel = tk.Label(root, text="Plot On/Off", font= ('calbiri', 15))
plotLabel.place(x = 10, y = recordLabel.winfo_y()+50)
root.update()
plotOnOff = tk.Button(root, image=off, font= ('calbiri',15), command= lambda: OnOff_plot())
plotOnOff.place(x= plotLabel.winfo_x()+plotLabel.winfo_width()+20, y= plotLabel.winfo_y()-8)

# save data button
root.update()
save = tk.Button(root, text= "Save", font= ('calbiri',12), command= lambda: save_data())
save.place(x=10, y=plotLabel.winfo_y() + 40)

# tell ui the name of the saved file
root.update()
inputtxt = tk.Entry(root,width=20, bg="black", fg="white", borderwidth=5)
inputtxt.place(x=save.winfo_x()+save.winfo_width()+20,y=save.winfo_y()+2)
root.update()

root.mainloop()


