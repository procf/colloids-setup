## DPD simulation of shear flow in water using HOOMD-blue v3.1.0
## NOTE: Requires Equilibrium.gsd of water
## (2022)

#########  MODULE LIBRARY
# Use HOOMD-blue
import hoomd
import hoomd.md # molecular dynamics
import hoomd.custom
# Use GSD files
import gsd # provides Python API; MUST import sub packages explicitly (as below)
import gsd.pygsd # GSD reader in pure Python
import gsd.hoomd # read and write HOOMD schema GSD files
# Maths
import numpy
import math
import random # psuedo-random number generator


######### SIMULATION INPUTS
dt_Integration = 0.01 # integration timestep (dt)
period = 1 # the recording timestep
N_time_steps = 1000 # total number of timesteps

# shearing parameters
SR = 0.1 # shear parameter (shear rate = SR*L_X)
N_strains = 10 # number of strains
theta = 1.0 # xy tilt factor
delta_T_shearing = round(theta/SR/dt_Integration) # timestep for shear
nframe_strain = delta_T_shearing/10 # 10 frames in theta strains

# system parameters
KT = 0.1 # system temperature
r_c = 1 # cut-off radius
rho = 3 # number density
gamma = 45 # viscous dissipation parameter (dissipative force)

# simulation box size (side length L)
L_X = 10; 
L_Y = 10;
L_Z = 10;
V_total = L_X*L_Y*L_Z # simulation box volume

# solvent particles (e.g. water particles)
R_S = 0.5 # solvent particle radius
m_S = 1 # solvent particle mass
V_Solvents = V_total # volume occupied by solvent
N_Solvents = math.floor(rho * V_Solvents) # number of solvent particles

# total number of particles
N_total = N_Solvents


######### SIMULATION
## 1. Takes a solvent simulation at thermal equilibrium 
## 2. And applies shear flow

## 1. Create a new simulation from equilibrium

# create a CPU simulation
device = hoomd.device.CPU()
sim = hoomd.Simulation(device=device, seed=50) 
# NOTE: set seed to a fixed value for reproducible simulations

# start the simulation from the equilibrium system
sim.timestep = 0 # set initial timestep to 0
sim.create_state_from_gsd(filename='Equilibrium.gsd')

# assign particle types to groups 
groupA = hoomd.filter.Type(['A'])
all_ = hoomd.filter.All()

# DON'T thermalize the system (shearing is not at thermal equilibrium!)
#sim.state.thermalize_particle_momenta(filter=all_, kT=KT)

# create neighboring list
nl = hoomd.md.nlist.Tree(buffer=0.05);

# define DPD Morse force (attraction) interactions
morse = hoomd.md.pair.DPDMorse(nlist=nl, kT=KT, default_r_cut=1.0 * r_c, bond_calc=False)
# specify the conservative (A) and dissipative (gamma) parameters 
# for solvent particle interactios. NOTE: use gamma=45 not gamma=4.5
# (no Morse Potential for solvent, Morse parameters are zero or ignored)
morse.params[('A','A')] = dict(A0=25.0 * KT / r_c, gamma=45,
	D0=0, alpha=3.0, r0=0.0, eta=0.0, f_contact=0.0,
	a1=0.0, a2=0.0, rcut=r_c) # force calc
morse.r_cut[('A','A')] = r_c # used to assemble nl

# choose integration method for the end of each timestep
# (use the updated integrator with shear rate)
nve = hoomd.md.methods.NVE(filter=all_)
integrator = hoomd.md.Integrator(dt=dt_Integration, SR=SR*L_Y, forces=[morse], methods=[nve])
sim.operations.integrator = integrator

# set the simulation to log certain values
logger = hoomd.logging.Logger()
thermodynamic_properties = hoomd.md.compute.ThermodynamicQuantities(filter=all_)
sim.operations.computes.append(thermodynamic_properties)
logger.add(thermodynamic_properties, quantities=['kinetic_temperature',
                'pressure_tensor', 'virial_ind_tensor', 'potential_energy'])

# save outputs
gsd_writer = hoomd.write.GSD(trigger=nframe_strain, filename='Shearing'+str(SR)+'.gsd',
	filter=all_, mode='wb', dynamic=['property','momentum','attribute'])
sim.operations.writers.append(gsd_writer)
gsd_writer.log = logger

## 2. Apply shear

# set the box resize operation
initial_box = hoomd.Box.from_box(sim.state.box)
final_box = hoomd.Box.from_box(initial_box)
final_box.xy = theta
delta_T_shearing = round((final_box.xy-initial_box.xy)/SR/dt_Integration)
box_resize=hoomd.update.BoxResize(trigger=period, box1=initial_box, box2=final_box,
	variant=hoomd.variant.Ramp(A=0, B=1, t_start=sim.timestep, t_ramp=delta_T_shearing),
	filter=all_, SR=SR*L_Y)
sim.operations += box_resize

# shear one shear time (theta = 1.0, i.e. 1 strain)
sim.run(delta_T_shearing+1)

# clear the box-resize operation for the next round
sim.operations -= box_resize

remaining_strains = (N_strains - 1)/2

# continue to shear the system up to N_strains
for i in range(remaining_strains):
	# set the box resize operation
	initial_box = hoomd.Box.from_box(sim.state.box)
	initial_box.xy = -theta # oscillatory for more efficiency
	final_box = hoomd.Box.from_box(initial_box)
	final_box.xy = theta
	# delta_T_shearing is now in terms of 2*theta
	delta_T_shearing = round((final_box.xy-initial_box.xy)/SR/dt_Integration)
	box_resize = hoomd.update.BoxResize(trigger=period, box1=initial_box, box2=final_box,
		variant = hoomd.variant.Ramp(A=0, B=1, t_start=sim.timestep,
		t_ramp=delta_T_shearing), filter=all_, SR=SR*L_Y)
	sim.operations += box_resize

	# run for one shear times (theta = 1.0, i.e. 1 strain)
	sim.run(delta_T_shearing+1)

	# clear the box-resize operation for the next round
	sim.operations -= box_resize
