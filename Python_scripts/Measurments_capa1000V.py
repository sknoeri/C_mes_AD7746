import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCsKCl_2um_358_174100V.xlsx', 'rb'))
time = meas['t'].to_numpy()/0.011
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(2,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-3097-114,label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()


zero = [69/75,19/24,88/103,139/150,17/21,83/99,122/136,11/14,24/30,40/50,148/162]
hund = [156/172,60/74,175/190,27/33,12/12,16/16,19/20,16/18,18/21,23/27,15/18]
fhun = [96/102,94/100,11/12,15/18,14/15,140/137,163/161,124/135,159/178,10/12,10/11]
tous = [37/46,79/97,53/65,72/88,150/184,14/17,107/147,168/222,165/186,147/163,78/92]

ex0=np.ones(len(zero))
ex1=np.ones(len(zero))*2
ex5=np.ones(len(zero))*3
ex10=np.ones(len(zero))*4
plt.figure()
plt.plot(ex0,zero,'-o',label='Ratio 0V applied')
plt.plot(ex1,hund,'-o',label='Ratio 100V applied')
plt.plot(ex5,fhun,'-o',label='Ratio 500V applied')
plt.plot(ex10,tous,'-o',label='Ratio 1000V applied')
plt.ylabel('Peak ratio')
plt.xlabel('experiment #')
plt.legend()
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