import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
# meas=pd.read_excel(open(path+'/CSS_400_174_100nm1000Vbignew1.xlsx', 'rb'))
# # time = meas['t'].to_numpy()
# # capa = meas['C'].to_numpy()
# # V = meas['V'].to_numpy()/10
# # time = meas['time'].to_numpy()
# # capa = meas['pressure'].to_numpy()
# # area=np.arange(2,len(capa),1)
# ## making the plots of the measurements
# # plt.figure()
# # plt.plot(time[area],capa[area]-3488,label='Capacitance signal [fF]')
# # plt.plot(time[area],V[area],'-o',label='Applied voltage [dV]')
# # plt.ylabel('C [fF]')
# # plt.xlabel('t [s]')
# # plt.legend()
# # plt.grid()
#
# #
# zero = [20/61,22/71,26/89,41/172,45/189,49/213,49/216,50/213,51/221,23/63,
#         33/103,40/133,31/98,35/116,34/112,19/53,15/19,22/32,27/42,62/93,159/214,107/213,52/80]
# hund = [109/1777,100/215,60/110,78/93,69/99,71/105,107/953,104/738,94/197,89/108,76/96
#         ,46/98,99/303,120/1332,109/320,89/208]
# fhun = [111/252,110/194,111/220,111/219,114/271,119/430,123/520,159/3468,152/517,133/86]
# tous = [110/31,119/32,122/50,126/61,125/44,139/95,141/119,144/218,146/275,144/268,144/244,144/210,138/85,106/30]
#
# ex0=np.ones(len(zero))
# ex1=np.ones(len(hund))*2
# ex5=np.ones(len(fhun))*3
# ex10=np.ones(len(tous))*4
# exmean=[1,2,3,4]
# mean=[np.mean(zero),np.mean(hund),np.mean(fhun),np.mean(tous)]
# plt.figure()
# plt.plot(ex0,zero,'g x',label='0V applied')
# plt.plot([1,1],[np.std(zero)+mean[0],-np.std(zero)+mean[0]],'r--o')
# plt.plot(ex1,hund,'b x',label='100V applied')
# plt.plot([2,2],[np.std(hund)+mean[1],-np.std(hund)+mean[1]],'r--o')
# plt.plot(ex5,fhun,'y x',label='500V applied')
# plt.plot([3,3],[np.std(fhun)+mean[2],-np.std(fhun)+mean[2]],'r--o')
# plt.plot(ex10,tous,'k x',label='1000V applied')
# plt.plot([4,4],[np.std(tous)+mean[3],-np.std(tous)+mean[3]],'r--o')
# plt.plot(exmean,mean,'r-o',label='mean +- STD')
# plt.ylabel('Peak ratio')
# plt.xlabel('experiment #')
# plt.ylim(top=3)
# plt.ylim(bottom=0)
# plt.legend()
# plt.grid()
#
# # # experient 2
# #
# path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
# # meas=pd.read_excel(open(path+'/CSS_400_174_100nm1000Vbignew2.xlsx', 'rb'))
# # time = meas['t'].to_numpy()/0.011
# # capa = meas['C'].to_numpy()
# # V = meas['V'].to_numpy()/10
# # time = meas['time'].to_numpy()
# # capa = meas['pressure'].to_numpy()
# # area=np.arange(30,len(capa),1)
# ## making the plots of the measurements
# # plt.figure()
# # plt.plot(time[area],capa[area]-3491,label='Capacitance signal [fF]')
# # plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
# # plt.ylabel('C [fF]')
# # plt.xlabel('t [s]')
# # plt.legend()
# # plt.grid()
#
# #
# zero = [12/17,12/19,14/25,18/36,22/47,26/62,28/64,74/163,95/218,88/221,63/222,56/169,60/177,60/174,65/191]
# hund = [33/45,39/74,43/69,51/70,40/71,65/121,61/111,38/56,27/57,33/61,35/61,64/129,117/225,99/215,70/80]
# fhun = [93/46,88/54,98/59,125/288,125/214,125/190,124/138,119/85,91/23,113/36,95/36,115/84,120/87,124/168,
#         129/308,129/274,127/115,118/59]
# tous = [184/3305,194/309,197/3480,215/2552,205/797,187/255,165/731,151/149,149/152,141/228,151/999,141/60,
#         153/67,167/91,151/821,154/239,164/1870,162/330,143/61]
# #
# ex0=np.ones(len(zero))
# ex1=np.ones(len(hund))*2
# ex5=np.ones(len(fhun))*3
# ex10=np.ones(len(tous))*4
# exmean=[1,2,3,4]
# mean=[np.mean(zero),np.mean(hund),np.mean(fhun),np.mean(tous)]
# plt.figure()
# plt.plot(ex0,zero,'g x',label='0V applied')
# plt.plot([1,1],[np.std(zero)+mean[0],-np.std(zero)+mean[0]],'r--o')
# plt.plot(ex1,hund,'b x',label='100V applied')
# plt.plot([2,2],[np.std(hund)+mean[1],-np.std(hund)+mean[1]],'r--o')
# plt.plot(ex5,fhun,'y x',label='500V applied')
# plt.plot([3,3],[np.std(fhun)+mean[2],-np.std(fhun)+mean[2]],'r--o')
# plt.plot(ex10,tous,'k x',label='1000V applied')
# plt.plot([4,4],[np.std(tous)+mean[3],-np.std(tous)+mean[3]],'r--o')
# plt.plot(exmean,mean,'r-o',label='mean +- STD')
# plt.ylabel('Peak ratio')
# plt.xlabel('experiment #')
# plt.ylim(top=3.5)
# plt.ylim(bottom=0)
# plt.legend()
# plt.grid()

#
#
# ## experient 3
#

#
zero = [12/32,15/37,15/41,19/50,50/127,59/184,59/186,57/176,34/175,11/23,
        21/51,20/46,19/43,25/60,34/91,49/148,37/102,18/42]
hund = [18/45,24/88,27/110,33/119,57/215,106/1461,83/313,84/457,94/1287,41/112,
        27/64,48/90,33/85,71/171,77/165,111/330,146/217,150/184,36/60]
fhun = [52/41,56/45,66/53,75/59,96/77,140/119,172/154,119/98,301/3790,]
tous = [64/44,136/40,147/58,149/42,126/77,152/65,143/116,151/134,152/117,
        154/141,152/134,155/134,158/880,165/451,171/462,169/735,160/183,142/103]
#
# ex0=np.ones(len(zero))
# ex1=np.ones(len(hund))*2
# ex5=np.ones(len(fhun))*3
# ex10=np.ones(len(tous))*4
# exmean=[1,2,3,4]
# mean=[np.mean(zero),np.mean(hund),np.mean(fhun),np.mean(tous)]
# plt.figure()
# plt.plot(ex0,zero,'g x',label='0V applied')
# plt.plot([1,1],[np.std(zero)+mean[0],-np.std(zero)+mean[0]],'r--o')
# plt.plot(ex1,hund,'b x',label='100V applied')
# plt.plot([2,2],[np.std(hund)+mean[1],-np.std(hund)+mean[1]],'r--o')
# plt.plot(ex5,fhun,'y x',label='500V applied')
# plt.plot([3,3],[np.std(fhun)+mean[2],-np.std(fhun)+mean[2]],'r--o')
# plt.plot(ex10,tous,'k x',label='1000V applied')
# plt.plot([4,4],[np.std(tous)+mean[3],-np.std(tous)+mean[3]],'r--o')
# plt.plot(exmean,mean,'r-o',label='mean +- STD')
# plt.ylabel('Peak ratio')
# plt.xlabel('experiment #')
# plt.legend()
# plt.ylim(top=3)
# plt.ylim(bottom=0)
# plt.grid()
# plt.show()
##### Nes device

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
# meas=pd.read_excel(open(path+'/CSS_400_174_100nm1000Vbignew3.xlsx', 'rb'))
# time = meas['t'].to_numpy()
# capa = meas['C'].to_numpy()
# V = meas['V'].to_numpy()/10
# # time = meas['time'].to_numpy()
# # capa = meas['pressure'].to_numpy()
# area=np.arange(30,len(capa),1)
# # making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3798,'-o',label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()
# plt.show()

# fier
zero = [46/34,59/46,99/81,177/154,197/174,242/232,249/245,60/41,93/73,117/99,202/181,
        260/260,308/271,105/85,107/88,121/97,131/99,237/209,277/242,240/221]
hund = [72/57,119/94,124/97,146/118,207/185,232/234,41/30,41/30,52/40,55/41,86/67,162/142,209/199,
        222/222,222/218,114/89]
fhun = [154/350,126/117,155/139,160/1531,158/333,146/667,158/261,148/246,157/268,142/117,150/92,131/140,
        15/14,18/13,56/18,71/42,194/207,221/231,226/240,230/241,218/215]
tous = [76/67,78/70,83/74,97/88,119/111,136/133,165/174,187/323,210/401,221/709,370/238,
        192/188,68/53,64/51,72/55]
#
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

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
# meas=pd.read_excel(open(path+'/CSS_400_174_100nm1000Vbig21.xlsx', 'rb'))
# time = meas['t'].to_numpy()
# capa = meas['C'].to_numpy()
# V = meas['V'].to_numpy()/10
# # time = meas['time'].to_numpy()
# # capa = meas['pressure'].to_numpy()
# area=np.arange(30,len(capa),1)
# # making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3645,label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()
# plt.show()

# 2
zero = [45/71,51/79,59/92,70/106,77/121,90/151,30/41,39/55,40/54,
        43/59,50/68,66/91,81/117,95/140,98/149,52/70,36/50,34/48,32/45,10/10]
hund = [27/40,24/33,26/40,26/35,24/35,23/31,42/67,39/61,40/62,50/79,62/100,
        68/112,77/133,83/146,30/75,88/136,95/161,80/128,16/20]
fhun = [46/68,30/47,29/55,31/68,31/68,33/71,37/71,76/119,56/114,62/143,67/154,116/237,126/264,
        91/236,97/263,97/284,90/240,58/73,47/85,40/61,39/69,42/46,43/73]
tous = [250/3645,279/714,279/245,252/470,230/599,240/637,237/736,224/829,32/25,47/33,56/52,55/57]
#
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




path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
# meas=pd.read_excel(open(path+'/CSS_400_174_100nm1000Vbig22.xlsx', 'rb'))
# time = meas['t'].to_numpy()
# capa = meas['C'].to_numpy()
# V = meas['V'].to_numpy()/10
# # time = meas['time'].to_numpy()
# # capa = meas['pressure'].to_numpy()
# area=np.arange(30,len(capa),1)
# # making the plots of the measurements
# plt.figure()
# plt.plot(time[area],capa[area]-3643,label='Capacitance signal [fF]')
# plt.plot(time[area],V[area],label='Applied voltage [V]')
# plt.ylabel('C [fF]')
# plt.xlabel('t [s]')
# plt.legend()
# plt.grid()
# plt.show()

#3
zero = [28/30,34/36,40/45,43/48,41/45,50/57,101/128,105/134,123/163,
        128/163,139/179,142/191,144/198,55/65,93/97,121/151,128/162,133/172,128/164]
hund = [48/58,71/92,83/108,93/124,102/138,120/158,124/165,127/171,129/175,
        126/170,30/33,33/38,29/32,32/37,151/175]
fhun = [28/35,20/19,76/75,103/94,150/127,195/163,186/255,52/71,41/53,52/66,73/94,83/116,
        128/144,121/160,114/160,120/166,121/1399]
tous = [121/100,96/76,76/69,65/65,67/66,76/67,35/31,27/31,141/145,150/155,171/206,
        182/352,185/1794,174/192]
#
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
