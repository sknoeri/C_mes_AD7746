import matplotlib.pyplot as plt
import numpy as np

"""
This program plots the average voltage growth for several different capacitors
"""

fileName = '8.9.19_v3_oil_20_hg_13.txt'
datax, datay = np.loadtxt(fileName,dtype = float, skiprows=1, unpack=True)

zero_index = []

for index, item in enumerate(datay, start=0):
    if datay[index] < 0.01 and datay[index] > -0.01:
        zero_index.append(index)


"""
for index, item in enumerate(zero_index, start=1):
    if zero_index[index] - zero_index[index-1]>30:
        fileID = 'file' + str(index)
        x = datax[zero_index[index-1]:zero_index[index]]
        exec("%s = %d" % (fileID,x))
"""

    
plt.plot(datay,datax)

