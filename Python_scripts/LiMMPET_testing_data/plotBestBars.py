import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'Times New Roman',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

fig = plt.figure()
ax = fig.add_axes([0.125,0.125,0.8,0.8])

langs = ['1', '2', '3', '4', '5']
students = [312,113.5,131.76,113.5,281.7]
ax.bar(langs,students)
ax.set_ylabel('dV/dt (mV/s)', fontdict=font)
ax.set_xlabel('Run', fontdict=font)
#ax.set_title('Voltage growth rates', fontdict=font)

plt.show()

# calculate average and standard error
vavg = np.mean(students)
vstddev = np.std(students)
vstderror = vstddev/np.sqrt(len(students))
print(vavg)
print(vstderror)
