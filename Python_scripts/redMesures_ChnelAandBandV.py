# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports # Serial library
import matplotlib.pyplot as plt
import tkinter as tk #tkinter for GUI
import pandas as pd # for writing into a .xml file
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import multiprocessing
import time

import numpy as np
Ts = 0.022
widowSize = 200
# initalize the serial port
serialInst = serial.Serial()
# registered variables
valuesA = []
valuesB = []
valuesV = []
t_valA = []
t_valB = []
t_valV = []
# conditions to start plotting or to stop it and to register measurements
recordStop = True
onOffPlot = False
comOpen = False

Path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'

# function that plots the Serial data from the arduino
def plotFunc(ta,data1,tb,data2,tv,data3):
    plot1.clear()
    plot1.set_title('Serial Data')
    plot1.set_xlabel('t')
    plot1.set_ylabel('data')
    plot1.plot(ta, data1, 'b', label='Chanel A C[fF]')
    if data2 is not None:
        plot1.plot(tb, data2, 'r', label='Chanel B C[fF]')
    if data3 is not None:
        plot1.plot(tv, data3, 'r', label='Voltage [V]')
    plot1.legend()
    plot1.grid()
    canvas.draw()
    # creating the Matplotlib toolbar
    root.update()

# Fuction triggered by GUI
def record_data(): # starts measurements when the start btton is applied
    ta = 0
    tb = 0
    tv = 0
    global recordStop
    global t_valA,t_valB,t_valV
    global valuesA,valuesB,valuesV
    global comOpen
    global widowSize
    if(recordStop == True and comOpen != False):# Starts record when COM is open and recod is enabled by GUI
        recordStop =False
        plt.close()
        record.config(image=on) # shows the ON button
        Output.insert("1.0","Start measurements \n") # puts string a beginning of text field
        valuesA = []
        valuesB = []
        valuesV = []
        t_valA = []
        t_valB = []
        t_valV = []
        ##t_plot = np.arange(0,widowSize*Ts,Ts)
        #v_plotA = np.zeros(widowSize)
    else:
        recordStop = True
        record.config(image=off) # shows the off button
    cnt=0
    cnt2=0
    while True: # infinite loop that reads the serial buffer of the Arduino and starts the plot
        cnt=cnt+1
        cnt2=cnt2+1
        if(recordStop == True or comOpen == False): # global variable that can interupt the measuremetn
            if comOpen == False:
                Output.insert("1.0","No arduino Uno connected \n") # puts string a beginning of text field
                break
            else:
                Output.insert("1.0","Rcording is interruped \n") # puts string a beginning of text field
                break
        if serialInst.in_waiting: # waits until charcters recived from Arduino
            ## Make function out of fhtis
            try:
                bites = serialInst.readline() # reads recived bytes
            except:
                recordStop=True
                record.config(image=off)  # shows the ON button
                Output.insert('1.0','Cant read line')
                break
            try:
                packet = str(bites.decode('utf')).replace('\r\n', '',1)  # decodes recived bytes and removes \n\r from the reading
            except:
                record.config(image=off)  # shows the ON button
                Output.insert('1.0', 'Cant decode line')
                break
            #########
            float_or_not = packet[1:].replace('.', '', 1).isdigit()  # checks if number is convertible to float
            if(packet[0]=='A'):
                l = True
            else:
                l = False
            if float_or_not == False: # if not float append 0 to data vector
                valuesA.append(0)
                valuesB.append(0)
                valuesV.append(0)
                t_valA.append(ta)
                t_valB.append(tb)
                t_valV.append(tv)
                Output.insert("1.0","Reciced data: "+packet +'\n') # puts string a beginning of text field
            else: # append data vector
                if packet[0] == 'A':
                    ta = ta + Ts
                    packet = packet[1:]
                    valuesA.append(float(packet))
                    t_valA.append(ta)
                if packet[0] == 'B':
                    tb = tb + Ts
                    packet = packet[1:]
                    valuesB.append(float(packet))
                    t_valB.append(tb)
                if packet[0] == 'V':
                    tb = tb + Ts
                    packet = packet[1:]
                    valuesV.append(float(packet))
                    t_valV.append(tv)
                # if (packet[0] != 'B' and packet[0] != 'A'):

            if onOffPlot == True: ## hadels the start and stop of the data plot
                a = len(t_valA)
                b = len(t_valB)
                v = len(t_valV)
                if(a>=widowSize):
                    t_plota = t_valA[a - widowSize:a]
                    v_plotA = valuesA[a - widowSize:a]
                else:
                    ## for the values of chanel A

                    v_plotA = np.zeros(widowSize)
                    v_plotA[widowSize-len(valuesA):widowSize] = valuesA
                    v_plotA[0:widowSize-len(valuesA)] = np.zeros(widowSize - len(valuesA))
                    t_plota = np.arange(widowSize)* Ts
                if(b>=widowSize):
                    t_plotb = t_valB[b - widowSize:b]
                    v_plotB = valuesB[b - widowSize:b]
                else:
                    # for the values of chanel B
                    v_plotB = np.zeros(widowSize)
                    v_plotB[widowSize - len(valuesB):widowSize] = valuesB
                    v_plotB[0:widowSize - len(valuesB)] = np.zeros(widowSize - len(valuesB))
                    t_plotb = np.arange(widowSize)*Ts
                if (v >= widowSize):
                    t_plotV = t_valV[v - widowSize:v]
                    v_plotV = valuesB[v - widowSize:v]
                else:
                    # for the values of chanel B
                    v_plotV = np.zeros(widowSize)
                    v_plotV[widowSize - len(valuesV):widowSize] = valuesV
                    v_plotV[0:widowSize - len(valuesV)] = np.zeros(widowSize - len(valuesV))
                    t_plotV = np.arange(widowSize) * Ts
                if cnt>1000:
                    # print('lenth of B'+str(len(t_plotb)))
                    # print('lenth of A'+str(len(t_plota)))
                    plotFunc(t_plota, v_plotA, t_plotb, v_plotB, t_plotV, v_plotV)  # actualize the plot after every reading
                    cnt=0
            else:
                if cnt > 1000:
                    #plt.clf()
                    root.update()
                    cnt2=0
# Turns on/off the plot
def OnOff_plot():
    global onOffPlot
    global widowSize
    if onOffPlot== False:
        plotOnOff.config(image=on) # shows the ON button
        float_or_not = plotSize.get().replace('.', '', 1).isdigit()
        if float_or_not:
            widowSize = int(plotSize.get())
        else:
            Output.insert('Plot range must be a number')
        onOffPlot = True
    else:
        plotOnOff.config(image=off) # shows the off button
        onOffPlot = False

def save_data(): # stp button is applyed the fucktion saves data to measurment file
    if (len(t_valA)>0):
        if(fileName.get()== ''):
            name = 'NoName'
        else:
            name = fileName.get()
        d = {'timeA': t_valA, 'A chanel': valuesA, 'timeB': t_valB, 'B channel': valuesB, 'timeV': t_valV,
             'Volts': valuesV}
        data = pd.DataFrame({k: pd.Series(v) for k, v in d.items()})
        data.to_excel(Path+'/' + name +'.xlsx')
        Output.insert("1.0","Register measurements to: \n"+Path+'/' + name +'.xlsx \n') # puts string a beginning of text field
    else:
        Output.insert("1.0","Emty file \n") # puts string a beginning of text field

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
        Output.insert("1.0","No port is conected \n") # puts string a beginning of text field

    for onePort in ports: # loops trough all connected ports and appends them to an array
        portName = str(onePort)
        portList.append(portName)
        if "Arduino Uno" in portName: # checks if one of the ports is an Arduino uno
            portVar = portName[0:5]
            Output.insert("1.0","Arduino Uno conneced to Port: " + portVar + '\n') # puts string a beginning of text field
        else:
            Output.insert("1.0","No Arduino Uno conected \n") # puts string a beginning of text field
    return portVar # false or portname
########### Initialise the Serial port if Arduino is connected
def comActive():
    global comOpen
    portVar = serialPortArduino()
    if(portVar == False or comOpen==True):
        startSerial.config(image=off) # shows the off button
        Output.insert('1.0','Serial port is closed\n')
        comOpen = False
        serialInst.close()
    else:
        try:
            serialInst.baudrate = int(baudText.get())
            serialInst.port = portVar
            serialInst.timeout = 1
            serialInst.open()
            serialInst.reset_input_buffer()
            startSerial.config(image=on) # shows the ON button
            Output.insert("1.0", "Baudrate is set to:" + baudText.get() + "\n")
            comOpen = True
        except:
            Output.insert("1.0", "Baudrate is not correct" + baudText.get() + "\n")  # puts string a beginning of text field("")


if __name__ == '__main__':
    #------ Creat buttons of little user interface to control the plot starts etc
    root = tk.Tk()
    root.title('Real time plot')
    root.config(background= 'light blue')
    root.geometry('1000x600') #set the window size

    #define fgures
    on = tk.PhotoImage(file=Path + "/Python_scripts/on.png")
    off = tk.PhotoImage(file=Path + "/Python_scripts/off.png")

    # Serial comunication start button
    serialLabel = tk.Label(root, text="Serial On/Off", font= ('calbiri', 15))
    serialLabel.place(x = 10, y = 20)
    root.update()
    startSerial = tk.Button(root, image=off, font= ('calbiri',12), command= lambda: comActive()) #text= "Serial On/Off",
    startSerial.place(x= serialLabel.winfo_x()+serialLabel.winfo_width()+20, y=10)

    # tell GUI the baude rate
    root.update()
    baudLabel = tk.Label(root, text="Set Baudrate",font=("Helvetica", 15))
    baudLabel.place(x = 10, y = serialLabel.winfo_y()+50)
    root.update()
    baudText = tk.Entry(root, width=20, borderwidth=2,font=("Helvetica", 15)) #bg="black", fg="white",
    baudText.place(x=baudLabel.winfo_x() + baudLabel.winfo_width() + 20, y=baudLabel.winfo_y())
    root.update()

    # record data start button
    root.update()
    recordLabel = tk.Label(root, text="Record On/Off", font= ('calbiri', 15))
    recordLabel.place(x = 10, y = baudLabel.winfo_y()+50)
    root.update()
    record = tk.Button(root, image=off,  command= lambda: record_data())
    record.place(x= recordLabel.winfo_x()+recordLabel.winfo_width()+20, y=recordLabel.winfo_y()-8)

    # Plot on off
    plotLabel = tk.Label(root, text="Plot On/Off", font= ('calbiri', 15))
    plotLabel.place(x = 10, y = recordLabel.winfo_y()+50)
    root.update()
    plotOnOff = tk.Button(root, image=off, font= ('calbiri',15), command= lambda: OnOff_plot())
    plotOnOff.place(x= plotLabel.winfo_x()+plotLabel.winfo_width()+20, y= plotLabel.winfo_y()-8)
    root.update()
    plotSize = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 15))
    plotSize.place(x=plotOnOff.winfo_x() + plotOnOff.winfo_width() + 20, y=plotOnOff.winfo_y() + 5)

    # save data button
    root.update()
    save = tk.Button(root, text= "Save", font= ('calbiri',15), command= lambda: save_data())
    save.place(x=10, y=plotLabel.winfo_y() + 50)

    # tell ui the name of the saved file
    root.update()
    fileName = tk.Entry(root, width=20, borderwidth=2, font=("Helvetica", 15))
    fileName.place(x=save.winfo_x() + save.winfo_width() + 20, y=save.winfo_y()+5 )
    root.update()

    #------ puttig the text log field ----
    Output = tk.Text(root, height=20,width=35,bg="light cyan",font=("Helvetica", 15))
    Output.place(x=10, y=fileName.winfo_y() + fileName.winfo_height() + 10)
    root.update()

    #------The figure on the user interface window------#
    fig = plt.figure()
    plot1 = fig.add_subplot(111)
    plot1.set_title('Serial Data')
    plot1.set_xlabel('t')
    plot1.set_ylabel('data')
    plot1.grid()
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master=root)
    canvas.get_tk_widget().place(x=baudText.winfo_x()+baudText.winfo_width()+20 , y=startSerial.winfo_y()) # placing the canvas on the Tkinter window
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    root.update()

    root.mainloop()


