# plot the kinetic temperature (kT) of a simulation
# (from GSD file) versus DPD time
# NOTE: requires "gsd-properties.txt" created with the
#	sim-analysis.py script

import numpy as np
import matplotlib.pyplot as plt

f = np.genfromtxt('gsd-properties.txt')
plt.plot(f[:,0],f[0:,2], "bo", markersize="0.5")
plt.axhline(y=0.1, color="r")
plt.xlabel('DPD times')
plt.ylabel('kT')
#plt.savefig('kT.png',dpi=600, transparent=False)
plt.show()
