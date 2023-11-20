# Gelation and Shearing of Colloidal Particles

This is an overview of the PRO-CF Colloids Team approach to colloid gelation and shearing simulations with HOOMD-blue.

Before running gelation or shearing simulations you should have already familiarized yourself with how to run and analyze basic simulations:
* [ran a basic DPD simulation of water](/04-Simulating-waterDPD.md)
* [installed VMD](/05-VMD-Install-Guide.md) 
* [visualized a simulation in VMD](/06-Using-VMD.md)
* [ran basic analysis checks](/07-Analysis-Guide.md) on the simulation to verify it ran correctly
* [installed our modified version of HOOMD-blue](/03-HOOMDblue-Install-Guide.md#installing-hoomd31-mod) 
* [learned the basics of how we apply shear flow](/Background-Reading/4-Shearing-4pg.pdf)
* and [run and analyzed a simple shearing simulation of water](/07-Analysis-Guide.md#shearing-waterdpd)

Once you have completed all those steps you should be familiar with the basics of DPD simulations and how to run them. This gives you the necessary background to understand our colloid simulations and run them yourself!

[Last Update: November 2023]

These workflows were first developed by Mohammad (Nabi) Nabizadehi as part of his PhD thesis. They were further optimized and adapted for MPI by Dr. Deepak Mangal and streamlined by Rob Campbell. This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Necessary Modifications for Colloid Simulations](/08-Gelation-and-Shearing.md#necessary-modifications-for-colloid-simulations) 
2. [Simulation Steps](/08-Gelation-and-Shearing.md#simulation-steps)
3. [Analysis](/08-Gelation-and-Shearing.md#analysis)
4. [Next Steps](/08-Gelation-and-Shearing.md#next-steps)
<br>

## Necessary Modifications for Colloid Simulations 

DPD simulations were originally designed for coarse-grained simulations of a single type of atom or molecule, e.g. water. The particle interactions are soft (particles effectively have no radius and can overlap with each other in space) and limited to Conservative, Dissipative, and Random Force contributions.

We want to take that solvent fluid and suspend hard colloid particles in it, which means we need to prevent our colloid particles from overlapping. We also want to add other interparticle forces to modify the behavior of our colloid particles so that we can form gels.

Making this happen is relatively straightforward, but it requires many changes to how the calculations work. A detailed summary of what these changes are and why we make them is available in the Background Readings on [DPD for colloids](/Background-Reading/2-DPD-for-Colloids-18pg.pdf) (18 pages) and [Morse Potential](/Background-Reading/3-Morse-Potential-2pg.pdf) (2 pages).

Once we've made a colloidal gel, we also need to make some changes to be able to shear the gel correctly and retain information about it's structure. You should be familiar with these from running a basic shearing simulation of water, and they are explained in the Background Reading on [Shear](/Background-Reading/4-Shearing-4pg.pdf) (4 pages).

Implementing these changes in HOOMD-blue requires modifying the source code: we have to add additional files for the new force calculation (to prevent particle overlaps and add new interparticle interaction forces) and we need to make sure those changes are accessible and consistent throughout the software. We also need to update how particles behave when they cross a boundary, so that shear flow occurs correctly. This is why we developed (and continue to develop) our [hoomd4.2.1-mod](https://github.com/procf/hoomd4.2.1-mod) software. 

Once we've made these changes to HOOMD-blue's source code, accessing them in a simulation requires additional parameters in our simulation scripts.
<br>
<br>
## Simulation Steps

Our simulations now have several steps, and it is easiest to separate them into different files so that we can check our results along the way (and avoid computational errors) AND so we can speed up certain parts of the simulation by using MPI parallelization.

Templates for each of these steps are avaialble in the [hoomd4.2.1-mod repository](https://github.com/procf/hoomd4.2.1-mod).

**Step 1 - Initializing a Simulation**
* Set the basic parameters (size, number of particles, etc.) and create a single frame of the simulation with particles randomly positioned throughout the space. Particles will overlap at this stage. 
* This step **must** be done serially (only use 1 node and 1 core).

**Step 2 - Bringing the Simulation to Thermal Equilibrium**
* Using the initialized system, we will resolve overlaps by running the simulation using contact force, but we will apply **zero** attraction between colloids and **zero** shear rate. These simulations are run until the particles have reached thermal equilibrium (i.e. the measured temperature of the system (kT) equals the value we chose, usually kT = 0.1)
* *Before moving to the next step*, visualize the simulation in VMD and use the analysis module to make sure the temperature (kT) has stabilized (at least within ~10% of the set value) and the average shear stress is zero.
* You can run this step with MPI and up to 27 cores per node; however, for smaller simulations you may not be able to divide it into 27 parts. If that happens and you get errors, try reducing the number of cores to 8 or fewer.

**Step 3 - Creating a Gel**
* Using the equilibrium state as our initial state, we run the simulation with all the interparticle forces added (and **zero** shear rate) until a stable gel is formed (typically around 500 colloid particle diffusion times)
* *Before moving to the next step*, visualize the simulation in VMD and use the analysis module to make sure the temperature (kT) has remained stable and the average coordination number (Z) has reached a fairly stable maximum (usually Z= 6 a single type of colloidal particle).
* For small simulations (e.g. L=30) you should use a small number of cores (e.g. 1 node and 8 cores), otherwise the simulation is divided into sections that are too small. For larger simulations (e.g. L=60) you can easily go up to at 27 cores per node.

**Step 4 - Shearing a Gel**
* Using the gelation state as our initial state, we apply a shear rate and run the simulation for a number of times equivalent to the desired number of strains on the system.
* *After shearing*, visualize the simulation in VMD and use the analysis module to bin the system (find average values for different layers/bins/slabs of the system) and to separate out the effects of colloids from solvent. You will then use those averages to check the stress-strain curve and the velocity profile. You may also want to check the average coordination number (Z)

Congratulations, you now have data!
<br>
<br>
## Analysis

As we discussed in the [Analysis Guide](/07-Analysis-Guide.md), we have to extract data from the GSD file before we can analyze and plot it.

In addition to the basic extraction and plotting of data that we ran for water, there are a number of more advance analyses that we frequently use: 
* mean squared displacement
* average coordination number
* radial distribution function g(r)
* number density fluctuations (AKA Index of Dispersion)
* Voronoi volume distribution
* pair correlation function
* (for shearing only) corrected kinetic temperature and pressure (colloid contributions only)
* (for shearing only) averaged solvent velocity profile


These analyses can all be done in Python, R, or other programming languages, but for computational speed and efficiency we have created a Fortran module that is extracts and calculates many of these values.

After compilation, the Fortran module is run with a Python script using [f2py](https://numpy.org/doc/stable/f2py/), a NumPy Fortran-to-Python interface. This Python script is set up a series of modules, with simulation specific inputs at the beginning. They are called at the bottom of the script, so you can easily limit which analyses you run by scrolling to the bottom of the script and commenting out the analyses you do not need. Running this script calls the relevant sections of the Fortran module and outputs data files for the selected analyses.

If you need to make any changes to these analyses, you will probably need to modify both the Python and Fortran codes. After modifying the Fortran code, remember to recompile the module before using it by running the command:
```bash
f2py -c module_analysis.f90 -m module
```

Copies of the standard Fortran and Python scripts are both available in the [hoomd4.2.1-mod repository](https://github.com/procf/hoomd4.2.1-mod)
<br>
<br>
## Next Steps

This covers the basic outline of colloidal gel simulations! The rest is up to you and your research.

*Background Reading:*

If you haven't already, you should review the [Background Reading](/Background-Reading) documents summarizing DPD, our modifications to DPD, the Morse Potential, and how we apply shear. 

You should also read the list of recommended papers:
* Background on DPD
	* "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]" (1997)

* Background on simulating colloidal gel rheology
	* "[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions]" (2015) 
	* "[Viscosity measurement techniques in Dissipative Particle Dynamics]" (2015)
	* "[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]" (2017)
	* "[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]" (2020)
	* "[Life and death of colloidal bonds control the rate-dependent rheology of gels]" (2021)

[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions]:https://sor.scitation.org/doi/10.1122/1.4931655 
[Viscosity measurement techniques in Dissipative Particle Dynamics]:https://doi.org/10.1016/j.cpc.2015.05.027
[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]:https://doi.org/10.1063/1.474784
[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]:https://doi.org/10.1103/PhysRevLett.118.048003
[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]:https://doi.org/10.1016/j.mtadv.2019.100026
[Life and death of colloidal bonds control the rate-dependent rheology of gels]:https://doi.org/10.1038/s41467-021-24416-x


