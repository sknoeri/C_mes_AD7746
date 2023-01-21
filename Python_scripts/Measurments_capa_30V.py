import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET\CapaDiff'
meas=pd.read_excel(open(path+'/CCs_2umKCl_358_174_30V.xlsx', 'rb'))
time = meas['t'].to_numpy()/0.011
capa = meas['C'].to_numpy()
V = meas['V'].to_numpy()
# time = meas['time'].to_numpy()
# capa = meas['pressure'].to_numpy()
area=np.arange(73095,73160,1)
area=np.arange(2,len(capa),1)
## making the plots of the measurements
plt.figure()
plt.plot(time[area],capa[area]-4003,'-o',label='Capacitance signal [fF]')
plt.plot(time[area],V[area],'-o',label='Applied voltage [V]')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
plt.legend()
plt.grid()


a=np.mean(capa[29518:29572]-4003)
b=np.mean(capa[30594:30639]-4003)

a1=np.mean(capa[50399:50453]-4003)
b1=np.mean(capa[51580:51627]-4003)
a2=np.mean(capa[50490:50545]-4003)
b2=np.mean(capa[51675:51722]-4003)
a3=np.mean(capa[50571:50630]-4003)
b3=np.mean(capa[51765:51817]-4003)

a4=np.mean(capa[72872:72928]-4003)
b4=np.mean(capa[74160:74209]-4003)
a5=np.mean(capa[72983:73043]-4003)
b5=np.mean(capa[74285:74339]-4003)
a6=np.mean(capa[73095:73160]-4003)
b6=np.mean(capa[74406:74467]-4003)

a7=np.mean(capa[78840:78901]-4003)
b7=np.mean(capa[80180:80236]-4003)
a8=np.mean(capa[78934:79000]-4003)
b8=np.mean(capa[80288:80347]-4003)

a9=np.mean(capa[83366:83424]-4003)
b9=np.mean(capa[84725:84777]-4003)
## 30 Volts
c=np.mean(capa[37665:37726]-4003)
d=np.mean(capa[38760:38800]-4003)
c1=np.mean(capa[37758:37810] - 4003)
d1=np.mean(capa[38860:38902] - 4003)
c2=np.mean(capa[37844:37909] - 4003)
d2=np.mean(capa[38967:39024] - 4003)

c3=np.mean(capa[43134:43182] - 4003)
d3=np.mean(capa[44273:44312] - 4003)
c4=np.mean(capa[43231:43280] - 4003)
d4=np.mean(capa[44379:44418] - 4003)
c5=np.mean(capa[43333:43384] - 4003)
d5=np.mean(capa[44494:44538] - 4003)

c6=np.mean(capa[57760:57807] - 4003)
d6=np.mean(capa[58942:58980] - 4003)
c7=np.mean(capa[57870:57932] - 4003)
d7=np.mean(capa[59098:59155] - 4003)

c8=np.mean(capa[62258:62306] - 4003)
d8=np.mean(capa[63480:63520] - 4003)
c9=np.mean(capa[62370:62420] - 4003)
d9=np.mean(capa[63609:63654] - 4003)
print(a/b)
print(a1/b1)
zero1=abs(a/b)
zero2=abs(a1/b1)
zero3=abs(a2/b2)
zero4=abs(a3/b3)
zero5=abs(a4/b4)
zero6=abs(a5/b5)
zero7=abs(a6/b6)
zero8=abs(a7/b7)
zero9=abs(a8/b8)
zero10=abs(a9/b9)
print(c/d)
print(c1/d1)
three1=abs(c/d)
three2=abs(c1/d1)
three3=abs(c2/d2)
three4=abs(c3/d3)
three5=abs(c4/d4)
three6=abs(c5/d5)
three7=abs(c6/d6)
three8=abs(c7/d7)
three9=abs(c8/d8)
three10=abs(c9/d9)
zero=[zero1,zero2,zero3,zero4,zero5,zero6,zero7,zero8,zero9,zero10]
three=[three1,three2,three3,three4,three5,three6,three7,three8,three9,three10]
data=[zero,three]
ex0=np.ones(len(zero))
ex3=np.ones(len(zero))*2
plt.figure()
plt.plot(ex0,zero,'-o',label='Ratio 0V applied')
plt.plot(ex3,three,'-o',label='Ratio 30V applied')
plt.ylabel('Peak ratio')
plt.xlabel('experiment #')
plt.legend()
plt.grid()
plt.show()
# fig, ax =plt.subplots()
# ax.boxplot(data)
# plt.grid()
# plt.show()
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