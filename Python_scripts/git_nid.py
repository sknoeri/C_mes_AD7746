# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as bk
import tkinter as tk
import numpy as np


# Global variables
data = np.array([])
cond = True

## plot data
def plot_data():
    global cond
    global data

    if(cond == False):
        paket = '0'
        if serialInst.in_waiting:
            a = serialInst.readline()
            paket = a.decode('utf').replace('\r\n','',1)
            if paket.replace('.', '', 1).isdigit()==False:
                print(paket)
                paket=0
        if(len(data) < 100):
            data = np.append(data,float(paket))
        else:
            data[0:99] = data[1:100]
            data[99] = float(paket)

        lines.set_xdata(np.arange(0,len(data)))
        lines.set_ydata(data)
        canvas.draw()
    root.after(1,plot_data())
def plot_start():
    global cond
    cond = True
    serialInst.reset_input_buffer()
def plot_stop():
    global cond
    cond = False

# Mais GUI code

root = tk.Tk()
root.title('Real time plot')
root.config(background= 'light blue')
root.geometry('700x500') #set the window size

# Creat plot objet on GUI
# add figure canvas
fig = plt.figure()
ax = fig.add_subplot(111)

#ax parameters
ax.set_title('Serial Data')
ax.set_xlabel('Sample')
ax.set_ylabel('Pressure')
ax.set_xlim(0,100)
ax.set_ylim(-0.5,800)
lines = ax.plot([],[])[0]

canvas = bk.FigureCanvasTkAgg(fig, master=root) # a tk. DrawingArea
canvas.get_tk_widget().place(x= 10, y= 10, width= 500, height= 400)
canvas.draw()

#------ Creat buttons
root.update()
start = tk.Button(root, text= "Start", font= ('calbiri',12), command= lambda: plot_start())
start.place(x= 100, y=450)

root.update()
stop = tk.Button(root, text= "Stop", font= ('calbiri',12), command= lambda: plot_stop())
stop.place(x= start.winfo_x()+start.winfo_reqwidth() + 20, y= 450)


# initalize the serial port
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []
portVar = False
pressure = 0

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

root.after(1, plot_data())
root.mainloop()



