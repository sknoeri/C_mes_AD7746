import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\C_mes_AD7746'
meas=pd.read_excel(open(path+'/2mmcpa_Oil348DI174_droplets_FF2.xlsx', 'rb'))
time = meas['time'].to_numpy()
capa = meas['pressure'].to_numpy()
plt.plot(time,capa)
plt.show()