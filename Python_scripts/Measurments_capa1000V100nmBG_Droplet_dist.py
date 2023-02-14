import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


zero = [46/34,59/46,99/81,177/154,197/174,242/232,249/245,60/41,93/73,117/99,202/181,
        260/260,308/271,105/85,107/88,121/97,131/99,237/209,277/242,240/221]
zerou = [46,59,99,177,197,242,249,60,93,117,202,
        260,308,105,107,121,131,237,277,240]
X=np.array([np.ones(len(zerou)),zerou]).T
zpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
plotvec=np.arange(1,308)
zplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(zpoly, zero)
z_pred = model.predict(zplpoly)

hund = [72/57,119/94,124/97,146/118,207/185,232/234,41/30,41/30,52/40,55/41,86/67,162/142,209/199,
        222/222,222/218,114/89]
hundu = [72,119,124,146,207,232,41,41,52,55,86,162,209,
        222,222,114]
X=np.array([np.ones(len(hundu)),hundu]).T
hpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
hplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(hpoly, hund)
h_pred = model.predict(hplpoly)

fhun = [154/350,126/117,155/139,160/1531,158/333,146/667,158/261,148/246,157/268,142/117,150/92,131/140,
        15/14,18/13,56/18,71/42,194/207,221/231,226/240,230/241,218/215]
fhunu = [154,126,155,160,158,146,158,148,157,142,150,131,
        15,18,56,71,194,221,226,230,218]
X=np.array([np.ones(len(fhunu)),fhunu]).T
fpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
fplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(fpoly, fhun)
f_pred = model.predict(fplpoly)

tous = [76/67,78/70,83/74,97/88,119/111,136/133,165/174,187/323,210/401,221/709,
        192/188,68/53,64/51,72/55]
tousu = [76,78,83,97,119,136,165,187,210,221,
        192,68,64,72]
X=np.array([np.ones(len(tousu)),tousu]).T
tpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
tplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(tpoly, tous)
t_pred = model.predict(tplpoly)




plt.figure()
plt.plot(zerou,zero,'g x',label='0V applied')
plt.plot(plotvec,z_pred,'g',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')

# plt.figure()
plt.plot(hundu,hund,'b x',label='100V applied')
plt.plot(plotvec,h_pred,'b',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(fhunu,fhun,'y x',label='500V applied')
plt.plot(plotvec,f_pred,'y',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(tousu,tous,'k x',label='1000V applied')
plt.plot(plotvec,t_pred,'k',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
plt.xlim(right=309)
plt.xlim(left=0)
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
# plt.show()
# experient 2

zero = [45/71,51/79,59/92,70/106,77/121,90/151,30/41,39/55,40/54,
        43/59,50/68,66/91,81/117,95/140,98/149,52/70,36/50,34/48,32/45,10/10]
zerou = [45,51,59,70,77,90,30,39,40,
        43,50,66,81,95,98,52,36,34,32,10]
X=np.array([np.ones(len(zerou)),zerou]).T
zpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
plotvec=np.arange(1,300)
zplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(zpoly, zero)
z_pred = model.predict(zplpoly)

hund = [27/40,24/33,26/40,26/35,24/35,23/31,42/67,39/61,40/62,50/79,62/100,
        68/112,77/133,83/146,30/75,88/136,95/161,80/128,16/20]
hundu = [27,24,26,26,24,23,42,39,40,50,62,
        68,77,83,30,88,95,80,16]
X=np.array([np.ones(len(hundu)),hundu]).T
hpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
hplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(hpoly, hund)
h_pred = model.predict(hplpoly)

fhun = [46/68,30/47,29/55,31/68,31/68,33/71,37/71,76/119,56/114,62/143,67/154,116/237,126/264,
        91/236,97/263,97/284,90/240,58/73,47/85,40/61,39/69,42/46,43/73]
fhunu = [46,30,29,31,31,33,37,76,56,62,67,116,126,
        91,97,97,90,58,47,40,39,42,43]
X=np.array([np.ones(len(fhunu)),fhunu]).T
fpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
fplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(fpoly, fhun)
f_pred = model.predict(fplpoly)

tous = [250/3645,279/714,279/245,252/470,230/599,240/637,237/736,224/829,32/25,47/33,56/52,55/57]
tousu = [250,279,279,252,230,240,237,224,32,47,56,55]
X=np.array([np.ones(len(tousu)),tousu]).T
tpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
tplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(tpoly, tous)
t_pred = model.predict(tplpoly)



plt.figure()
plt.plot(zerou,zero,'g x',label='0V applied')
plt.plot(plotvec,z_pred,'g',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(hundu,hund,'b x',label='100V applied')
plt.plot(plotvec,h_pred,'b',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# a=fhunu.sort()
# print(a)
# plt.figure()
plt.plot(fhunu,fhun,'y x',label='500V applied')
plt.plot(plotvec,f_pred,'y',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(tousu,tous,'k x',label='1000V applied')
plt.plot(plotvec,t_pred,'k',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
plt.xlim(right=300)
plt.xlim(left=0)
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.show()

#
# # ## experient 3

#
zero = [28/30,34/36,40/45,43/48,41/45,50/57,101/128,105/134,123/163,
        128/163,139/179,142/191,144/198,55/65,93/97,121/151,128/162,133/172,128/164]
zerou = [28,34,40,43,41,50,101,105,123,
        128,139,142,144,55,93,121,128,133,128]
X=np.array([np.ones(len(zerou)),zerou]).T
zpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
plotvec=np.arange(1,300)
zplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(zpoly, zero)
z_pred = model.predict(zplpoly)


hund = [48/58,71/92,83/108,93/124,102/138,120/158,124/165,127/171,129/175,
        126/170,30/33,33/38,29/32,32/37,151/175]
hundu = [48,71,83,93,102,120,124,127,129,
        126,30,33,29,32,151]
X=np.array([np.ones(len(hundu)),hundu]).T
hpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
hplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(hpoly, hund)
h_pred = model.predict(hplpoly)

fhun = [28/35,20/19,76/75,103/94,150/127,195/163,186/255,52/71,41/53,52/66,73/94,83/116,
        128/144,121/160,114/160,120/166,121/1399]
fhunu = [28,20,76,103,150,195,186,52,41,52,73,83,
        128,121,114,120,121]
X=np.array([np.ones(len(fhunu)),fhunu]).T
fpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
fplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(fpoly, fhun)
f_pred = model.predict(fplpoly)

tous = [121/100,96/76,76/69,65/65,67/66,76/67,35/31,27/31,141/145,150/155,171/206,
        182/352,185/1794,174/192]
tousu = [121,96,76,65,67,76,35,27,141,150,171,
        182,185,174]
X=np.array([np.ones(len(tousu)),tousu]).T
tpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(X)
tplpoly = PolynomialFeatures(degree=1, include_bias=False).fit_transform(np.array([np.ones(len(plotvec)),plotvec]).T)
model = LinearRegression().fit(tpoly, tous)
t_pred = model.predict(tplpoly)

plt.figure()
print(z_pred.shape)
plt.plot(zerou,zero,'g x',label='0V applied')
plt.plot(plotvec,z_pred,'g',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(hundu,hund,'b x',label='100V applied')
plt.plot(plotvec,h_pred,'b',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(fhunu,fhun,'y x',label='500V applied')
plt.plot(plotvec,f_pred,'y',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
# plt.figure()
plt.plot(tousu,tous,'k x',label='1000V applied')
plt.plot(plotvec,t_pred,'k',label='Model')
plt.ylabel('Peak ratio')
plt.xlabel('Peak size sense A')
plt.xlim(right=300)
plt.xlim(left=0)
plt.ylim(top=2)
plt.ylim(bottom=0)
plt.legend()
plt.grid()
plt.show()