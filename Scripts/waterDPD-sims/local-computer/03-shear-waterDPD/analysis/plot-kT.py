# plot the kinetic temperature (kT) of a simulation
# (from GSD file) versus DPD time
# NOTE: requires "gsd-properties.txt" created with the
#	sim-analysis.py script

import numpy as np
import matplotlib.pyplot as plt

kT = 0.1 # from simulation

# NOTE: for shear analysis, we want time in terms of strain
# 	i.e. the trigger is "nframe_strain" not "period"
SR = 0.1 # from simulation
N_strains = 10 # from simulation
theta = 1.0 # from simulation
dt_Integration = 0.01 # from simulation
delta_T_shearing = round(theta/SR/dt_Integration)
nframe_strain = delta_T_shearing/10 # 20 frames per for each theta strain(s)
t1 = theta / nframe_strain * N_strains # timestep conversion to strains


f = np.genfromtxt('gsd-properties.txt')

plt.plot(f[:,0]*t1,f[0:,2], "bo", markersize="0.5")

plt.axhline(y=kT, color="r")

plt.yscale('log')
plt.xscale('log')

plt.xlabel('DPD times')
plt.ylabel('kT')

#plt.savefig('kT.png',dpi=600, transparent=False)
plt.show()
