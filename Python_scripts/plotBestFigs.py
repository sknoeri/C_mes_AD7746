import glob, os
import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'Arial',
        'color':  'black',
        'weight': 'bold',
        'size': 12,
        }

retval = os.getcwd()
print("current working direct %s" % retval)
mypath = "C:\\Users\\sean\\Box\\2019-2020\\Research\\LIMMPET\\Experimental Data\\test\\"

# Here's how:

# To navigate to a directory
#os.chdir(mypath)

# To loop over all text files in a directy and plot
file = (glob.glob("*.txt"))
substring = "8.9.19_v3_oil_20_hg_"
vt = []
Vrates = []
run = []

for index, item in enumerate(file, start=1):
    print(index)
    fullstring = file[index-1]
    print(substring)
    print(fullstring)
    if substring in fullstring:
        print(fullstring)
        datax, datay = np.loadtxt(item,dtype = float, skiprows=1, unpack=True)
        datax=np.abs(datax)
        maxV = np.amax(datax)
        maxVindex = np.where(datax == maxV)
        maxVt = np.abs(datay[maxVindex])
        Vrate = maxV/(maxVt+0.0001)
        print(Vrate)
        print(maxVt)
        print(maxV)
        if maxV > 7:
            plt.figure(1,figsize=(4.1,3.2),linewidth=5)
            plt.plot(datay,datax,'k',linewidth=3,markersize=5)
            vt = np.append(vt,maxVt)
            # plt.title('Damped exponential decay', fontdict=font)
            plt.xlabel('Time (s)', fontdict=font)
            plt.ylabel('Voltage (V)', fontdict=font)
            
            
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
