import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCsKCl_2um_358_174100V.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(2,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-3097-114,label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [dV]')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()
plt.plot()

zero = [69/75,19/24,88/103,139/150,17/21,83/99,122/136,11/14,24/30,40/50,148/162]
hund = [156/172,60/74,175/190,27/33,12/12,16/16,19/20,16/18,18/21,23/27,15/18]
fhun = [96/102,94/100,11/12,15/18,14/15,140/137,163/161,124/135,159/178,10/12,10/11]
tous = [37/46,79/97,53/65,72/88,150/184,14/17,107/147,168/222,165/186,147/163,78/92]

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
plt.ylim(top=3)
plt.ylim(bottom=0)
plt.legend()
plt.grid()

# experient 2

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCSKCl_2um_348_174_10002.xlsx', 'rb'))
time = meas['t'].to_numpy()/0.011
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()/10
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(30,len(capa),1)
## making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3411,label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()

zero = [40/17,44/19,42/18,35/15,36/15,33/15,30/13,38/16,19/9,24/10,27/12]
hund = [24/11,22/10,21/9,17/7,20/9,23/9,23/10,16/6,16/6,16/6,18/7,11/4,12/4,16/7,17/6]
fhun = [11/4,13/5,15/6,11/4,11/4,11/4,34/9,81/30,75/26,74/26,84/30,72/27,82/29]
tous = [59/24,51/21,50/21,49/20,72/28,61/24,56/23,67/26,72/27,62/24,61/24,62/24,51/21,52/21]

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
plt.ylim(top=3.5)
plt.ylim(bottom=0)
plt.legend()
plt.grid()


## experient 3

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CCSKCl_2um_348_174_10003.xlsx', 'rb'))
time = meas['t'].to_numpy()/0.011
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()/10
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(30,len(capa),1)
## making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3403,label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()
# plt.show()

zero = [57/23,53/22,54/22,50/21,74/28,64/25,59/24,47/19,57/22,60/23,65/25,56/23,54/22,50/20,50/21]
hund = [45/19,44/18,42/18,50/20,65/25,63/25,53/22,52/21,57/23,55/23,50/21,47/19,51/21,58/23,52/22,63/25,63/25,61/24]
fhun = [54/21,48/19,50/20,62/24,55/21,56/23,56/22,59/23,48/20,44/18,53/22,46/20,67/26,61/24,63/25,54/23,60/25,63/25]
tous = [77/29,52/22,60/25,59/25,50/21,49/21,49/21,50/22,48/20,67/27,64/26,57/24,54/22,51/22,64/26,52/22,59/24,61/25,57/23]

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
plt.legend()
plt.ylim(top=3)
plt.ylim(bottom=0)
plt.grid()
plt.show()