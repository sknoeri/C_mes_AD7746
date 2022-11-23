import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_OilDIdroplets'
meas=pd.read_excel(open(path+'/0.5capa_OIL374DI174_normalCD.xlsx', 'rb'))
time = meas['time'].to_numpy()
capa = meas['pressure'].to_numpy()


## making the plots of the measurements
plt.figure()
plt.plot(time,capa-3860)
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
plt.grid()
plt.show()