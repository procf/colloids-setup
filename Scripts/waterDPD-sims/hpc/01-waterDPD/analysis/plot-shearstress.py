# From a GSD file, plot the shear stress (-pressure_xy) 
# of a simulation versus DPD time
# NOTE: requires "gsd-properties.txt" created with the
#	sim-analysis.py script

import numpy as np
import matplotlib.pyplot as plt

dt_Integration = 0.01 # timestep from simulation
period = 1 # data recording interval from simulation

f = np.genfromtxt('gsd-properties.txt')

plt.plot(f[:,0]*dt_Integration*period, -f[0:,1], "bo", markersize="0.5")

plt.axhline(y=0.0, color="r")

plt.xlabel('DPD times')
plt.ylabel('shear stress')

#plt.savefig('shearstress.png',dpi=600, transparent=False)
plt.show()
