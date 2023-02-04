
import serial.tools.list_ports # Serial library
import matplotlib.pyplot as plt
import tkinter as tk #tkinter for GUI
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import numpy as np

#Deafult start variables
Ts = 0.011
widowSize = 200
volt = 0
# initalize the serial port
serialInst = serial.Serial()
# registered variables
cpacity = []
t_val = []
volts = []
# conditions to start plotting or to stop it and to register measurements
recordStop = True
onOffPlot = False
comOpen = False
Path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'

# function that plots the Serial data from the arduino
def plotFunc(t,data):
    """
    Args:Makes the plot of the figure defined by (t,data) on the tkinter GUI
        t: time list
        data: capacitance list, voltages measurements or inputs

    Returns: None plots a figure
    """
    plot1.clear()
    plot1.set_title('Serial Data')
    plot1.set_xlabel('t')
    plot1.set_ylabel('data')
    plot1.plot(t, data, 'b', label='capacitance fF')
    plot1.legend()
    plot1.grid()
    canvas.draw()
    # creating the Matplotlib toolbar
    root.update()
    return None

# Fuction triggered by GUI
def record_data(): # starts measurements when the start btton is applied
    """
    Reads and records the data of recived by the serial port. Is triggered by a button of the GUI
    that changes the global recordStop to True or False.
    Returns: recordStop bol, cpacity list, t_val list
    """
    t = 0
    global recordStop
    global t_val
    global cpacity
    global volts
    global volt
    global Ts
    global comOpen
    global widowSize
    if(recordStop == True and comOpen != False):#Starts record when COM is open and recod is enabled by GUI
        recordStop = False
        plt.close()
        record.config(image=on) # shows the ON button
        Output.insert("1.0","Start measurements \n")
        cpacity = []
        volts = []
        t_val = []
        ##t_plot = np.arange(0,widowSize*Ts,Ts)
        #p_plot = np.zeros(widowSize)
    else:
        recordStop = True
        record.config(image=off) # shows the off button
    cnt=0
    cnt2=0
    while True: #infinite loop that reads the serial buffer of the Arduino and starts the plot
        cnt=cnt+1
        cnt2=cnt2+1
        if(recordStop == True or comOpen == False):
            # global variable that can interupt the measuremetn
            if comOpen == False:
                Output.insert("1.0","No arduino Uno connected \n")
                break
            else:
                Output.insert("1.0","Rcording is interruped \n")
                break
        if serialInst.in_waiting: # waits until charcters recived from Arduino
            t = t + Ts
            ## Make function out of fhtis
            try:
                bites = serialInst.readline() # reads recived bytes
            except:
                recordStop=True
                record.config(image=off)  # shows the ON button
                Output.insert('1.0','Cant read line')
                break
            try:
                packet = str(bites.decode('utf')).replace('\r\n', '',1)
                # decodes recived bytes and removes \n\r from the reading
            except:
                record.config(image=off)  # shows the ON button
                Output.insert('1.0', 'Cant decode line')
                break
            #########
            float_or_not = packet.replace('.', '', 1).isdigit()
            #checks if number is convertible to float
            if float_or_not == False: # if not float append 0 to data vector
                cpacity.append(0)
                t_val.append(t)
                Output.insert("1.0","Reciced data: "+packet +'\n')
            else: # append data vector
                cpacity.append(float(packet))
                t_val.append(t)
            volts.append(volt)
            if onOffPlot == True: ## hadels the start and stop of the data plot
                a = len(t_val)
                if(a>widowSize):
                    t_plot = t_val[a-widowSize:a]
                    c_plot = cpacity[a - widowSize:a]
                    v_plot = volts[a - widowSize:a]
                else:
                    c_plot = np.zeros(widowSize)
                    c_plot[widowSize-len(cpacity):widowSize] = cpacity
                    c_plot[0:widowSize-len(cpacity)] = np.zeros(widowSize - len(cpacity))
                    v_plot = np.zeros(widowSize)
                    v_plot[widowSize - len(volts):widowSize] = volts
                    v_plot[0:widowSize - len(volts)] = np.zeros(widowSize - len(volts))
                    t_plot = np.arange(0,(widowSize-0.5)*Ts,Ts)
                if cnt>1000:
                    plotFunc(t_plot, c_plot)  # actualize the plot after every reading
                    cnt=0
            else:
                if cnt2 > 1000:
                    #plt.clf()
                    root.update()
                    cnt2=0
    return recordStop, t_val, cpacity
# Turns on/off the plot
def set_Ts():
    """
    Triggerd by the GUI. Puts the sample time configured on the Chip.
    Returns: Ts float
    """
    global Ts
    T = setTs.get()
    try:
       if(T.replace('.', '', 1).isdigit()==True):
           Ts=T
    except:
        Ts=0.011
    Output.insert('1.0', 'Sample time Ts set to: ' + str(Ts) + '\n')
    return Ts
def OnOff_plot():
    """
    Is triggerd by button on GUI
    Gets the size of plotted data entered into the GUI and updates it into windowSize.
    Starts the live plot or truns it off.
    Returns: onOffPlot bol, widowSize int
    """
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
    return onOffPlot, widowSize
def save_data():
    """
    Is triggrd by button on GUI. Saves data descibed path in code.
    Returns: None
    """
    if (len(t_val)>0):
        if(fileName.get()== ''):
            name = 'NoName'
        else:
            name = fileName.get()
        data = pd.DataFrame({'t': t_val, 'C': cpacity, 'V': volts})
        try:
            data.to_excel(Path+'/' + name +'.xlsx')
            Output.insert("1.0",
                          "Register measurements to: \n" + Path + '/' + name + '.xlsx \n')
        except:
            data.to_csv(Path+'/' + name +'.csv')
            Output.insert("1.0",
                          "Register measurements to: \n" + Path + '/' + name + '.csv \n')
    else:
        Output.insert("1.0","Emty file \n") # puts string a beginning of text field
    return None
def apply_V():
    """
    Triggerd by the GUI. Puts the applied voltage to list which is stored with cpavalues.
    Returns: volt float
    """
    global volt
    v = appVolt.get()
    try:
       if(v.replace('.', '', 1).isdigit()==True):
           volt=v
    except:
        volt=0
    Output.insert('1.0', 'Applied voltage set to:'+str(volt)+'\n')
    return volt

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

    for onePort in ports: # loops trougth all connected ports and appends them to an array
        portName = str(onePort)
        portList.append(portName)
        if "Arduino Uno" in portName: #checks if one of the ports is an Arduino uno
            portVar = portName[0:5]
            Output.insert("1.0","Arduino Uno conneced to Port: " + portVar + '\n')
        else:
            Output.insert("1.0","No Arduino Uno conected \n")
    return portVar # false or portname
########### Initialise the Serial port if Arduino is connected
def comActive():
    """
    Is triggerd by button on GUI. Sets the baudrate enterd in the GUI
    to the serial port where the Arduino is connected.
    Returns: comOpen bol
    """
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
            Output.insert("1.0", "Baudrate is not correct" + baudText.get() + "\n")
    return comOpen

if __name__ == '__main__':
    #Creat buttons of little user interface to control the plot starts etc
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
    startSerial = tk.Button(root, image=off, font= ('calbiri',12), command= lambda: comActive())
    startSerial.place(x= serialLabel.winfo_x()+serialLabel.winfo_width()+20, y=10)

    # tell GUI the baude rate
    root.update()
    baudLabel = tk.Label(root, text="Set Baudrate",font=("Helvetica", 15))
    baudLabel.place(x = 10, y = serialLabel.winfo_y()+50)
    root.update()
    baudText = tk.Entry(root, width=20, borderwidth=2,font=("Helvetica", 15))
    baudText.place(x=baudLabel.winfo_x() + baudLabel.winfo_width() + 20, y=baudLabel.winfo_y())
    root.update()

    # Apply volt button data button
    root.update()
    setTsB = tk.Button(root, text="Ts", font=('calbiri', 15), command=lambda: set_Ts())
    setTsB.place(x=10, y=baudText.winfo_y() + 50) # Apply volt button data button

    # Used sample time
    root.update()
    setTs = tk.Entry(root, width=10, borderwidth=2, font=("Helvetica", 15))
    setTs.place(x=setTsB.winfo_x() + setTsB.winfo_width() + 20, y=setTsB.winfo_y() + 5)
    root.update()

    # record data start button
    root.update()
    recordLabel = tk.Label(root, text="Record On/Off", font= ('calbiri', 15))
    recordLabel.place(x = 10, y = setTs.winfo_y()+50)
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
    fileName.place(x=save.winfo_x() + save.winfo_width() + 20, y=save.winfo_y() + 5)
    root.update()

    # Apply volt button data button
    root.update()
    apply = tk.Button(root, text="Apply", font=('calbiri', 15), command=lambda: apply_V())
    apply.place(x=10, y=save.winfo_y() + 50)

    # Aplied voltage to droptles on CCS device
    root.update()
    appVolt = tk.Entry(root, width=20, borderwidth=2, font=("Helvetica", 15))
    appVolt.place(x=apply.winfo_x() + apply.winfo_width() + 20, y=apply.winfo_y() + 5)
    root.update()

    #puttig the text log field
    Output = tk.Text(root, height=20,width=35,bg="light cyan",font=("Helvetica", 15))
    Output.place(x=10, y=appVolt.winfo_y() + appVolt.winfo_height() + 10)
    root.update()

    #The figure on the user interface window#
    fig = plt.figure()
    plot1 = fig.add_subplot(111)
    plot1.set_title('Serial Data')
    plot1.set_xlabel('t')
    plot1.set_ylabel('data')
    plot1.grid()
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,master=root)
    canvas.get_tk_widget().place(x=baudText.winfo_x()+baudText.winfo_width()+50 , y=startSerial.winfo_y())
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas,root)
    toolbar.update()
    root.update()

    root.mainloop()


