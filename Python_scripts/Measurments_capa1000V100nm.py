import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CSS_340_174_100nm1000V4_notfull.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()/10
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(2,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-2818-707-3,label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()
plt.show()

zero = [23/20,31/27,20/17,23/21,22/19,22/19,41/39,65/67,63/65,57/57,38/35,14/11,41/39,46/44,
        43/41,27/25,31/29,33/31,105/119,54/55,52/52,46/45,78/81,135/120,103/112]
zerou = [23,31,20,23,22,22,41,65,63,57,38,14,41,46,43,27,31,33,105,54,52,46,78]
hund = [70/72,69/70,60/61,55/55,33/32,33/28,32/29,34/32,25/24,22/20,15/15,25/24,77/78,63/62,
        69/69,46/45,42/40,13/13,55/60,47/50,48/47,28/27,25/24]
hundu = [70,69,60,55,33,33,32,34,25,22,15,25,77,63,69,46,42,13,55,47,48,28,25]
fhun = [66/76,53/57,50/50,49/50,45/43,54/57,54/56,66/73,77/124,57/61,24/24,56/78,55/66,53/57,
        48/47,71/98,56/60,88/152,78/88,48/63,31/31,90/142,56/60,32/32]
fhunu = [66,53,50,49,45,54,54,66,77,57,24,56,55,53,48,71,56,88,78,48,31,90,56,32]
tous = [83/176,87/176,63/94,110/145,51/85,54/60,60/184,64/107,79/96,63/89,310/342,152/260,
        116/204,125/252,135/204,24/20,83/160,113/119,113/162,133/174]
tousu = [83,87,63,110,51,54,60,64,79,63,310,152,116,125,135,24,83,113,113,133]


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
#
path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CSS_340_174_100nm1000V2.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(40,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-2715,label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
plt.ylabel('C [fF]/[V]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()
plt.show()
zero = [17/14,63/55,108/93,16/14,14/14,16/14,26/22,131/115,15/14,12/12,11/11
        ,12/12,145/132,10/11,14/13,148/131,70/45,36/29,61/52,152/137,106/90,102/86,79/67,29/24,146/258]
zerou = [17,63,108,16,14,16,26,131,15,12,11,12,145,10,14,148,70,36,61,152,106,102,79,29,146/258]
hund = [57/46,49/39,58/43,50/39,110/90,117/98,104/86,95/79,92/77,102/84,198/171,28/21,79/66,204/176,53/41,69/49,17/14
        ,190/159,72/59,76/62,84/68]
hundu = [57,49,58,50,110,117,104,95,92,102,198,28,79,204,53,69,17,190,72,76,84]
fhun = [401/1006,206/278,142/128,27/22,292/902,236/508,210/281,102/104,111/125,91/111,103/99,161/240,143/175,
        127/127,76/68,73/74,31/25,33/28]
fhunu = [401,206,142,27,292,236,210,102,111,91,103,161,143,127,76,73,31,33]
tous = [30/54,1423/2700,373/470,125/303,120/200,21/32,1149/2700,511/1370,256/202,24/24
        ,23/18,15/14,127/267,119/212,122/199,68/65]
tousu = [30,1423,373,125,120,21,1149,511,256]



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
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.grid()
# plt.show()


## experient 3

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff' #
meas=pd.read_excel(open(path+'/CSS_340_174_100nm1000V3.xlsx', 'rb'))
time = meas['t'].to_numpy()
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(30,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-3537,label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
plt.ylabel('C [fF]/[V]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()
plt.show()

zero = [91/84,60/51,129/121,41/34,42/36,20/17,23/17,54/46,17/14,57/49,17/14,10/9,31/25,21/16,76/71,51/43,27/21,
        76/71,51/43,27/21,166/163,65/58,35/28,25/19,80/72]
zerou = [91,60,129,41,42,20,23,54,17,57,17,10,31,21,76,51,27,76,51,27,166,65,35,25,80]
hund = [129/124,52/53,192/198,191/191,153/148,200/201,26/22,112/105,16/14,194/199,151/183,197/200,
        72/63,147/173,27/20,100/94]
hundu = [129,52,192,191,153,200,26,112,16,194,151,197,72,147,27,100]
fhun = [177/332,191/351,201/382,199/391,185/304,132/130,179/320,199/381,194/315,161/322,210/1066,201/494,60/61,
        210/2747,207/657,201/243,177/177]
fhunu = [177,191,201,199,185,132,179,199,194,161,210,201,60,210,207,201,177]
tous = [205/3537,113/256,118/248,80/104,22/20,60/90,55/53,124/260,22/20,169/2512,153/290,176/357,115/235,40/46,
        57/98,120/1291,91/3537,284/3537,184/393,181/399,57/160,67/87,135/260,167/2057]
tousu = [205,113,118,80,22,60,55,124,22,169,153,176,115,40,57,120,91,284,184,181,57,67,135,167]

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