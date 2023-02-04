import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_OilDIdroplets' #\CapaDiff
meas=pd.read_excel(open(path+'/1mmCapa_speed.xlsx', 'rb'))
# time = meas['t'].to_numpy()
# capa = meas['C'].to_numpy()
# V = meas['V'].to_numpy()
time = meas['time'].to_numpy()
capa = meas['pressure'].to_numpy()
area=np.arange(2,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],(capa[area]-18836))#,label='Capacitance signal [fF]'
# plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
# plt.legend()
plt.grid()
plt.show()

# a=np.mean(capa[29343:29570]-4003)
# b=np.mean(capa[30333:30639]-4003)
# a1=np.mean(capa[50398:50630]-4003)
# b1=np.mean(capa[51578:51817]-4003)
# ## 30 Volts
# c=np.mean(capa[37664:37909]-4003)
# d=np.mean(capa[38758:39024]-4003)
#
# e=np.mean(capa[43133:43386]-4003)
# f=np.mean(capa[44272:44540]-4003)
#
# print(a/b)
# print(a1/b1)
# print(c/d)
# print(e/f)
##
# D1=np.array([0.25,1,2])
# D=np.array([0.25,0.5,1,2])
# scale=1000*np.log(1/D*1000+1)
# print(scale)
# C=[9575,643,3035,4346]
# C1=[10175,7740,5475]
# plt.figure()
# plt.plot(D1,C1,'o-r',label='Max capacitance changes [fF]')
# plt.plot(D,scale,'o--b',label='ALog(1/D+1)')
# plt.ylabel('C [fF]')
# plt.xlabel('D [mm]')
# plt.legend()
# plt.grid()
# plt.show()