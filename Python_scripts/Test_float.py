# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import serial
import matplotlib.pyplot as plt
import numpy as np

serInst = serial.Serial('COM10',timeout=0.1,baudrate=11520)
serInst.reset_input_buffer()
# serInst.open()
# serInst.close()
while True:
    if serInst.in_waiting:  # waits until charcters recived from Arduino    ## Make function out of fhtis
        bites = serInst.readline()  # reads recived bytes
        packet = str(bites.decode('utf')).replace('\r\n', '',1)  # decodes recived bytes and removes \n\r from the reading
        print(packet)