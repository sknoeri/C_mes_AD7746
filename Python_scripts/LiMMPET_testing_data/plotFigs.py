import glob, os
import matplotlib.pyplot as plt
import numpy as np


retval = os.getcwd()
print("current working direct %s" % retval)
mypath = "C:\\Users\\sean\\Box\\2019-2020\\Research\\LIMMPET\\Experimental Data\\test\\"

# Here's how:

# To navigate to a directory
#os.chdir(mypath)

# To loop over all text files in a directy and plot
file = (glob.glob("*.txt"))
substring = "_v3_"
vt = []

for index, item in enumerate(file, start=1):
    print(index)
    fullstring = file[index-1]
    print(substring)
    print(fullstring)
    if substring in fullstring:
        print(fullstring)
        datax, datay = np.loadtxt(item,dtype = float, skiprows=1, unpack=True)
        maxV = np.amax(datax)
        maxVindex = np.where(datax == maxV)
        maxVt = np.abs(datay[maxVindex])
        Vrate = maxV/(maxVt+0.0001)
        print(Vrate)
        print(maxVt)
        print(maxV)
        if maxV < 200:
            plt.plot(maxVt,maxV,linestyle='none', marker='o')
            vt = np.append(vt,maxVt)
        else:
            print ("not here")
 # ------------------------------
 
"""
 
t = np.array([121, 103, 242, 183, 69, 99, 234, 189, 420, 333, 156, 87, 213])
v = np.array([10, 10, 10, 8.3, 6.7, 9.90, 4.56, 1.89, 4.20, 8.33, 12.6, 8.7, 4.13])
vrate = np.true_divide(v,t)
vrate = vrate*1000
vavg = np.mean(vrate)
vav = np.ones(len(vrate)) * vavg
run = np.linspace(1,len(vrate),len(vrate))
runavg = np.linspace(0,len(vrate)+1,len(vrate))
plt.figure(2)
plt.bar(run,vrate)
plt.xticks(run,('1','2','3','4','5','6','7','8','9','10','11','12','13'))
plt.plot(runavg,vav,'r--')
plt.axes.Axes.set_xlim(0.5, 13.5)

"""

