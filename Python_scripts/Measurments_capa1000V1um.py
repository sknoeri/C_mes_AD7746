import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCS_1um_348_174_100V.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()/10
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(2,len(capa),1)
## making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3369,label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()
# plt.show()


zero = [20/23,18/22,19/22,11/12,18/22,17/20,15/18,15/19,15/18,12/15,14/18,10/13,14/18,15/18,15/18,18/17,15/17,15/17]
hund = [14/17,14/17,14/17,14/17,15/17,15/17,14/17,14/16,14/17,15/18,15/17,14/18,13/17,14/18,14/18,16/18,17/18,15/17]
fhun = [13/14,13/14,14/15,16/18,15/16,16/19,15/17,16/19,13/16,12/14,12/13,14/15,14/15,14/15,15/16]
tous = [13/16,12/14,14/16,15/17,11/13,12/13,13/14,13/14,13/14,14/16,13/15,13/15,15/15,13/14,13/15,15/17,15/18]

ex0=np.ones(len(zero))
ex1=np.ones(len(hund))*2
ex5=np.ones(len(fhun))*3
ex10=np.ones(len(tous))*4
exmean=[1,2,3,4]
mean=[np.mean(zero),np.mean(hund),np.mean(fhun),np.mean(tous)]
plt.figure()
plt.plot(ex0,zero,'g x',label='0V applied')
plt.plot([1,1],[np.std(zero)+mean[0],-np.std(zero)+mean[0]],'r--o')
plt.plot(ex1,hund,'b x',label='100V applied')
plt.plot([2,2],[np.std(hund)+mean[1],-np.std(hund)+mean[1]],'r--o')
plt.plot(ex5,fhun,'y x',label='500V applied')
plt.plot([3,3],[np.std(fhun)+mean[2],-np.std(fhun)+mean[2]],'r--o')
plt.plot(ex10,tous,'k x',label='1000V applied')
plt.plot([4,4],[np.std(tous)+mean[3],-np.std(tous)+mean[3]],'r--o')
plt.plot(exmean,mean,'r-o',label='mean +- STD')
plt.ylabel('Peak ratio')
plt.xlabel('experiment #')
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.legend()
plt.grid()

# experient 2

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCS_1um_348_174_100V2.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()/10
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(30,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-3311,label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [dV]')
plt.ylabel('C [fF]/V [dV]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()
zero = [30/31,31/32,31/32,30/30,27/27,26/26,27/28,23/24,16/16,15/14,14/13,17/16,17/17,15/14,14/14]
hund = [19/18,17/16,17/17,11/11,17/18,18/19,18/18,16/16,22/23,16/17,14/14]
fhun = [18/19,18/18,19/19,16/16,18/18,20/20,16/16,13/13,18/18,18/18,18/18,16/15]
tous = [19/20,18/19,18/18,17/18,22/24,18/18,21/22,16/17]

ex0=np.ones(len(zero))
ex1=np.ones(len(hund))*2
ex5=np.ones(len(fhun))*3
ex10=np.ones(len(tous))*4
exmean=[1,2,3,4]
mean=[np.mean(zero),np.mean(hund),np.mean(fhun),np.mean(tous)]
plt.figure()
plt.plot(ex0,zero,'g x',label='0V applied')
plt.plot([1,1],[np.std(zero)+mean[0],-np.std(zero)+mean[0]],'r--o')
plt.plot(ex1,hund,'b x',label='100V applied')
plt.plot([2,2],[np.std(hund)+mean[1],-np.std(hund)+mean[1]],'r--o')
plt.plot(ex5,fhun,'y x',label='500V applied')
plt.plot([3,3],[np.std(fhun)+mean[2],-np.std(fhun)+mean[2]],'r--o')
plt.plot(ex10,tous,'k x',label='1000V applied')
plt.plot([4,4],[np.std(tous)+mean[3],-np.std(tous)+mean[3]],'r--o')
plt.plot(exmean,mean,'r-o',label='mean +- STD')
plt.ylabel('Peak ratio')
plt.xlabel('experiment #')
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.legend()
plt.grid()



## experient 3

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCS_1um_348_174_100V3.xlsx', 'rb'))
time = meas['t'].to_numpy()/0.011
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()/10
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(30,len(capa),1)
## making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3347,label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()
# plt.show()
# plt.show()

zero = [31/25,28/23,27/21,26/21,26/22,25/21,23/19,28/23,27/22,29/23,27/22,32/26,31/25,30/25,30/24,20/17]
hund = [33/27,30/25,28/23,25/20,27/22,24/19,27/22,25/20,31/25,27/22,29/23,27/21,17/15,29/23,26/21,24/19,17/15]
fhun = [27/22,27/22,22/18,24/19,11/10,28/23,26/21,29/23,25/21,30/24,25/20,27/22,26/21]
tous = [14/13,27/22,23/20,21/18,26/21,24/20,19/16,19/16,26/21,24/19,25/20,24/19,28/23,29/24,26/21,7/7,24/20,24/19,23/19,24/19,11/10]

ex0=np.ones(len(zero))
ex1=np.ones(len(hund))*2
ex5=np.ones(len(fhun))*3
ex10=np.ones(len(tous))*4
exmean=[1,2,3,4]
mean=[np.mean(zero),np.mean(hund),np.mean(fhun),np.mean(tous)]
plt.figure()
plt.plot(ex0,zero,'g x',label='0V applied')
plt.plot([1,1],[np.std(zero)+mean[0],-np.std(zero)+mean[0]],'r--o')
plt.plot(ex1,hund,'b x',label='100V applied')
plt.plot([2,2],[np.std(hund)+mean[1],-np.std(hund)+mean[1]],'r--o')
plt.plot(ex5,fhun,'y x',label='500V applied')
plt.plot([3,3],[np.std(fhun)+mean[2],-np.std(fhun)+mean[2]],'r--o')
plt.plot(ex10,tous,'k x',label='1000V applied')
plt.plot([4,4],[np.std(tous)+mean[3],-np.std(tous)+mean[3]],'r--o')
plt.plot(exmean,mean,'r-o',label='mean +- STD')
plt.ylabel('Peak ratio')
plt.xlabel('experiment #')
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.show()