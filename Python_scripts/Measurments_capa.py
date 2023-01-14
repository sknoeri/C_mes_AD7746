import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff'
meas=pd.read_excel(open(path+'/CCS_diff_2um_KClDI_Oil_3max30V.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()

## making the plots of the measurements
plt.figure()
plt.plot(time,capa-3963,'-o')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
plt.grid()
plt.show()

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