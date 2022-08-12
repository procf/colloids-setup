## Extract the results of a DPD simulation from the GSD file
##
## (2022)


######### MODULE LIBRARY
import numpy as np
import gsd.hoomd


######### INPUT PARAMETERS
filepath = '../Equilibrium.gsd'
period = 1 # from simulation
dt_Integration = 0.01 # from simulation
t1 = period * dt_Integration # timestep conversion factor


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
		dpdtime = (i+1)*t1
		# extract the the xy componenet of the pressure tensor
		# [0] = p_xx, [1] = p_xy, [2] = p_xz, [3] = p_yy, [4] = p_yz, [5] = p_zz
		Pr_xy=float(traj[i].log['md/compute/ThermodynamicQuantities/pressure_tensor'][1])	
		# extract the kinetic temperature (kT)
		KT=float(traj[i].log['md/compute/ThermodynamicQuantities/kinetic_temperature'][0])

		# write these values to the output file:
		f.write('{0:0.2f} {1} {2}\n'.format(dpdtime, Pr_xy, KT))


######### RUN CHECKS ON A SIMULATION

if __name__ == '__main__':	
	extract_properties_py(filepath)
