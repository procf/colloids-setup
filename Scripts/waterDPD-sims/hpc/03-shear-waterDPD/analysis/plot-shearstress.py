# From a GSD file, plot the shear stress (-pressure_xy) 
# of a simulation versus DPD time
# NOTE: requires "gsd-properties.txt" created with the
#	sim-analysis.py script

import numpy as np
import matplotlib.pyplot as plt

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

plt.plot(f[:,0]*t1, -f[0:,1], "bo", markersize="0.5")

plt.axhline(y=0.0, color="r")

plt.xlabel('DPD times')
plt.ylabel('shear stress')

#plt.savefig('shearstress.png',dpi=600, transparent=False)
plt.show()
