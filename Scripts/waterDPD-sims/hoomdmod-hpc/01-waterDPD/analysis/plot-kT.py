# plot the kinetic temperature (kT) of a simulation
# (from GSD file) versus DPD time
# NOTE: requires "gsd-properties.txt" created with the
#	sim-analysis.py script

import numpy as np
import matplotlib.pyplot as plt

kT = 0.1 # from simulation
dt_Integration = 0.01 # timestep in simulation
period = 1 # data recording interval from simulation

f = np.genfromtxt('gsd-properties.txt')

plt.plot(f[:,0]*dt_Integration*period,f[0:,2], "bo", markersize="0.5")

plt.axhline(y=kT, color="r")

plt.yscale('log')
plt.xscale('log')

plt.xlabel('DPD times')
plt.ylabel('kT')

#plt.savefig('kT.png',dpi=600, transparent=False)
plt.show()
