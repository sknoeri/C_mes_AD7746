# This is a sample Python script.
import numpy as np

# Press Umschalt+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import serial
# import matplotlib.pyplot as plt
# import numpy as np
#
# serInst = serial.Serial('COM10',timeout=0.1,baudrate=11520)
# serInst.reset_input_buffer()
# # serInst.open()
# # serInst.close()
# while True:
#     if serInst.in_waiting:  # waits until charcters recived from Arduino    ## Make function out of fhtis
#         bites = serInst.readline()  # reads recived bytes
#         packet = str(bites.decode('utf')).replace('\r\n', '',1)  # decodes recived bytes and removes \n\r from the reading
#         print(packet)
#
# a = 'A1312.12'
# float_or_not = a[1:].replace('.', '', 1).isdigit()
# print(a[0])
# print(a.replace('.', '', 1).replace('A','',1))
Ts=0.022
widowSize = [1,2,3,4]
print(type(widowSize))
