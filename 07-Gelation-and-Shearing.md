# Gelation and Shearing of Colloidal Particles

This is an overview of the PRO-CF Colloids Team approach to colloid gelation and shearing simulations with HOOMD-blue.

Before running gelation or shearing simulations you should have already familiarized yourself with how to run and analyze basic simulations:
* [installed the basic version of the HOOMD-blue software](/01-HOOMDblue-Install-Guide.md)
* read the [guide to standard DPD](/Background-Reading/1-DPD-8pg.pdf) and ran a [DPD simulation of water](/02-Simulating-waterDPD.md)
* [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation results
* [analyzed the results](/05-Log-Analysis-with-R.md) to verify that it ran correctly
* and [installed our in-house modified version of HOOMD-blue](/01-HOOMDblue-Install-Guide.md##installing-hoomd31-mod) for running colloid simulations

Once you have completed all those steps you should be familiar with the basics of DPD simulations and how to run them. This gives you the necessary background to understand our colloid simulations and run them yourself!

[Last Update: August 2022]

These workflows were first developed by Mohammad (Nabi) Nabizadehi as part of his PhD thesis. They were further optimized and adapted for MPI by Dr. Deepak Mangal and streamlined by Rob Campbell. This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Necessary Modifications for Colloid Simulations](/07-Gelation-and-Shearing.md#necessary-modifications-for-colloid-simulations) 
2. [Simulation Steps](/07-Gelation-and-Shearing.md#simulation-steps)
3. [Next Steps](/07-Gelation-and-Shearing.md#next-steps)
<br>

## Necessary Modifications for Colloid Simulations 

DPD simulations were originally designed for coarse-grained simulations of a single type of atom or molecule, e.g. water. The particle interactions are soft (particles effectively have no radius and can overlap with each other in space) and limited to Conservative, Dissipative, and Random Force contributions.

We want to take that solvent fluid and suspend hard colloid particles in it, which means we need to prevent our colloid particles from overlapping. We also want to add other interparticle forces to effect the behavior of the colloid particles so that we can form gels.

Making this happen is relatively straightforward, but it requires many changes to how the calculations work. A detailed summary of what these changes are and why we make them is available in the Background Readings on [DPD for colloids](/Background-Reading/2-DPD-for-Colloids-18pg.pdf) (18 pages) and [Morse Potential](/Background-Reading/3-Morse-Potential-2pg.pdf) (2 pages).

Once we've made a colloidal gel, we also need to make some changes to be able to shear the gel correctly and retain information about it's structure. These changes are explained in the Background Reading on [Shear](/Background-Reading/4-Shearing-4pg.pdf) (4 pages).

Implementing these changes in HOOMD-blue requires modifying the source code: we have to add additional files for the new force calculation (to prevent particle overlaps and add new interparticle interaction forces) and we need to make sure those changes are accessible and consistent throughout the software. We also need to update how particles behave when they cross a boundary, so that shear flow occurs correctly. This is why we developed (and continue to develop) our [hoomd3.1-mod](https://github.com/procf/hoomd3.1-mod) software. 

Accessing these changes in a simulation requires additional parameters in our simulation scripts.
<br>
<br>
## Simulation Steps

**1 - Initializing a Simulation**
* Set the basic parameters (size, number of particles, etc.) and create a single frame of the simulation with particles randomly positioned throughout the sapce. Particles will overlap at this stage. 
* This step **must** be done serially (only use 1 node and 1 core).

**2 - Bringing the Simulation to Thermal Equilibrium**
* Using the initialized system, we will resolve overlaps by running the simulation with contact force but **zero** attraction between colloids and **zero** shear rate. These simulations are run until the particles have reached thermal equilibrium (i.e. the measured temperature of the system (kT) equals the value we chose, usually kT = 0.1)
* *Before moving to the next step*, visualize the simulation in VMD and use the analysis module to make sure the temperature (kT) has stabilized (at least within ~10% of the set value)
* For small simulations (e.g. L=30) you should use a small number of cores (e.g. 1 node and 8 cores), otherwise the simulation is divided into sections that are too small. For larger simulations (e.g. L=60) you can easily go up to at 27 cores per node.

**3 - Creating a Gel**
* Using the equilibrium state as our initial state, we run the simulation with all the interparticle forces added (and **zero** shear rate) until a stable gel is formed (typically around 500 diffusion times)
* *Before moving to the next step*, visualize the simulation in VMD and use the analysis module to make sure the temperature (kT) has remained stable and the average coordination number (Z) has reached a fairly stable maximum (usually Z= 6 a single type of colloidal particle).
* For small simulations (e.g. L=30) you should use a small number of cores (e.g. 1 node and 8 cores), otherwise the simulation is divided into sections that are too small. For larger simulations (e.g. L=60) you can easily go up to at 27 cores per node.

**4 - Shearing a Gel**
* Using the gelation state as our initial state, we apply a shear rate and run the simulation for a number of times equivalent to the desired number of strains on the system.
* *After shearing*, visualize the simulation in VMD and use the analysis module to find averages for different layers/bins/slabs of the system and use those averages to check the stress-strain curve and the velocity profile. You may also want to check the average coordination number (Z)

Congratulations, you now have data!
<br>
<br>
## Next Steps

This covers the basic outline of colloidal gel simulations! The rest is up to you and your research.

*HPC Computing:*
* See the remaining guides for information about [accessing](/09-Accessing-Discovery.md) Northeastern's HPC cluster, "Discovery," and [working with](/10-Slurm-and-Disco.md) HPC simulations.
<br>

*Background Reading:*

If you haven't already, you should review the [Background Reading](/Background-Reading) documents summarizing DPD, our modifications to DPD, the Morse Potential, and how we apply shear. 

You should also read the following papers for more background on DPD simulations of colloidal gel rheology
* Background on DPD
	* "[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions]" (2015) 
	* "[Viscosity measurement techniques in Dissipative Particle Dynamics]" (2015)
	* "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]" (1997)

* Background on simulating colloidal gel rheology
	* "[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]" (2017)
	* "[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]" (2020)
	* "[Life and death of colloidal bonds control the rate-dependent rheology of gels]" (2021)

[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions]:https://sor.scitation.org/doi/10.1122/1.4931655 
[Viscosity measurement techniques in Dissipative Particle Dynamics]:https://doi.org/10.1016/j.cpc.2015.05.027
[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]:https://doi.org/10.1063/1.474784
[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]:https://doi.org/10.1103/PhysRevLett.118.048003
[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]:https://doi.org/10.1016/j.mtadv.2019.100026
[Life and death of colloidal bonds control the rate-dependent rheology of gels]:https://doi.org/10.1038/s41467-021-24416-x


