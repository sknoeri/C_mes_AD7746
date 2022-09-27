import glob, os
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

retval = os.getcwd()
print("current working direct %s" % retval)
mypath = "C:\\Users\\sean\\Box\\2019-2020\\Research\\LIMMPET\\Experimental Data\\test\\"

# Here's how:

# To navigate to a directory
#os.chdir(mypath)

# To loop over all text files in a directy and plot
file = (glob.glob("*.txt"))
substring = "_v3_"
for index, item in enumerate(file, start=1):
    fullstring = file[index]
    if substring in fullstring:
        datax, datay = np.loadtxt(item,dtype = float, skiprows=1, unpack=True)
        if np.amax(np.abs(datax)) > 1: 
            plt.figure(1)
            plt.plot(datay,datax,'b')
            plt.suptitle("{}".format(item))
            plt.xlabel('Time (s)')
            plt.ylabel('Potential (V)')
