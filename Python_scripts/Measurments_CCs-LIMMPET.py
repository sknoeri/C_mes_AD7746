import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '/Users\simon\Documents\Simels_daten\Epfl\sem_13_2022_Master_theis_USA\Master_thesis\Capacitance_measuring\Measurments_excel\Measures_CCS-LIMMPET'
meas=pd.read_excel(open(path+'/CCs_LIMMPET_CapaSerie_randomSpeed0_1um.xlsx', 'rb'))
timeA = meas['timeA'].to_numpy()
# timeB = meas['timeB'].to_numpy()
# timeV = meas['timeV'].to_numpy()
capaA = meas['A chanel'].to_numpy()
# capaB = meas['B channel'].to_numpy()
# Volts = meas['Volts'].to_numpy()


## making the plots of the measurements
plt.figure()

plt.plot(timeA, capaA-26)#, 'b', label='Sense A C[fF]'
# plt.plot(timeB, capaB+400, 'r', label='Sense B C[fF]')
# plt.plot(timeV, Volts, 'g', label='Volts [mV]')
plt.ylabel('C [fF]')
plt.xlabel('t [s]')
# plt.legend()
plt.grid()
plt.show()