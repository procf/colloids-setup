## DPD simulation of water using HOOMD-blue v3.1.0
## (2022)

#########  MODULE LIBRARY
import hoomd
import hoomd.md
import numpy
import math
import gsd
import gsd.hoomd
import random

######### SIMULATION INPUTS
dt_Integration = 0.01 # integration timestep (dt)
period = 1 # the recording timestep
N_time_steps = 1000 # total number of timesteps

KT = 0.1 # system temperature
r_c = 1 # cut-off radius
rho = 3 # number density

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
## 1. Creates a random distribution of solvent particles
## 2. Brings them to thermal equilibrium

## 1. Initialization

# initialize a snapshot of the system
snapshot = gsd.hoomd.Frame()
# create the simulation box
snapshot.configuration.box = [L_X, L_Y, L_Z, 0, 0, 0]
# add all particles to the snapshot
snapshot.particles.N=N_total
# set the particle types
snapshot.particles.types = ['A']
# assign particles to each type
typeid = []
typeid.extend([0]*N_Solvents)
snapshot.particles.typeid = typeid
# set a mass for each particle type
mass = []
mass.extend([m_S]*N_Solvents)
snapshot.particles.mass = mass
# set a diameter for each particle type
diameter = []
diameter.extend([2.0*R_S]*N_Solvents)
snapshot.particles.diameter = diameter
# randomly distribute all the particles in 3D space
pos_arr = numpy.zeros((N_total,3))
pos_arr[:,0] = numpy.random.uniform(-0.5*L_X, 0.5*L_X, N_total)
pos_arr[:,1] = numpy.random.uniform(-0.5*L_Y, 0.5*L_Y, N_total)
pos_arr[:,2] = numpy.random.uniform(-0.5*L_Y, 0.5*L_Y, N_total)
snapshot.particles.position = pos_arr
# save the snapshot of the initialized system
with gsd.hoomd.open(name='init.gsd', mode='wb') as f:
  f.append(snapshot)


## 2. Run to thermal equilibrium

# create a CPU simulation
device = hoomd.device.CPU()
sim = hoomd.Simulation(device=device, seed=50) 
# NOTE: set seed to a fixed value for reproducible simulations

# start the simulation from the initialized system
sim.timestep = 0 # set initial timestep to 0
sim.create_state_from_gsd(filename='init.gsd')

# assign particle types to groups 
groupA = hoomd.filter.Type(['A'])
all_ = hoomd.filter.All()

# thermalize the system (aka bring to thermal equilibrium)
sim.state.thermalize_particle_momenta(filter=all_, kT=KT)

# create neighboring list
nl = hoomd.md.nlist.Tree(buffer=0.05);

# define DPD interaction
dpd = hoomd.md.pair.DPD(nlist=nl, kT=KT, default_r_cut=r_c);
# specify the conservative (A) and dissipative (gamma) parameters 
# for solvent particle interactios
dpd.params[('A', 'A')] = dict(A=25.0, gamma=4.5)

# choose integration method for the end of each timestep
nve = hoomd.md.methods.ConstantVolume(filter=all_, thermostat=None)
integrator = hoomd.md.Integrator(dt=dt_Integration, methods=[nve], forces=[dpd])
sim.operations.integrator = integrator

# set the simulation to log certain values
logger = hoomd.logging.Logger()
thermodynamic_properties = hoomd.md.compute.ThermodynamicQuantities(filter=all_)
sim.operations.computes.append(thermodynamic_properties)
logger.add(thermodynamic_properties, quantities=['kinetic_temperature',
                'pressure_tensor', 'potential_energy'])

# save outputs
gsd_writer = hoomd.write.GSD(trigger=period, filename="Equilibrium.gsd",
	filter=all_, mode='wb', dynamic=['property','momentum','attribute'])
sim.operations.writers.append(gsd_writer)
gsd_writer.log = logger

# run the simulation!
sim.run(N_time_steps)
