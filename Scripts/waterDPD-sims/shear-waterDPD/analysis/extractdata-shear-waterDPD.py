## Extract the results of a DPD simulation from the GSD file
##
## (2022)


######### MODULE LIBRARY
import numpy as np
import gsd.hoomd
import math

######### INPUT PARAMETERS
filepath = 'Shearing0.1.gsd'

# NOTE: for shear analysis, we want time in terms of strain
# 	i.e. the trigger is "nframe_strain" not "period"
SR = 0.1 # from simulation
L_Y = 10 # from simulation
theta = 1.0 # from simulation
dt_Integration = 0.01 # from simulation
delta_T_shearing = round(theta/(SR*L_Y)/dt_Integration)
N_strains = 10 # number of strains
nframe_strain = delta_T_shearing/N_strains # number of frames per theta
t1 = theta / nframe_strain # timestep conversion to strains


######### DEFINE SIM CHECKS
## extract thermodynamic properties (temperature and pressure (AKA -stress) components)
def extract_properties_py(filename):
	# open the simulation GSD file as "traj" (trajectory)
	traj = gsd.hoomd.open(filename, 'rb')
	# get the number of frames
	nframe = len(traj)
	
	# create a file to save the thermodynamic properties
	f=open('gsd-properties.txt', 'w')
	f.write('DPD-time pressure_xy temperature\n')

	# for each frame
	for i in range(0, nframe):
		# get the straintime
		straintime = (i+1)*t1
		# extract the the xy componenet of the pressure tensor
		# [0] = p_xx, [1] = p_xy, [2] = p_xz, [3] = p_yy, [4] = p_yz, [5] = p_zz
		Pr_xy=float(traj[i].log['md/compute/ThermodynamicQuantities/pressure_tensor'][1])	
		# extract the kinetic temperature (kT)
		KT=float(traj[i].log['md/compute/ThermodynamicQuantities/kinetic_temperature'][0])

		# write these values to the output file:
		f.write('{0:0.2f} {1} {2}\n'.format(straintime, Pr_xy, KT))


######### RUN CHECKS ON A SIMULATION

if __name__ == '__main__':	
	extract_properties_py(filepath)
