# PRO-CF Colloids Simulation Setup Guide

Welcome to the PRO-CF Colloids simulation team! :tada:

These files will guide you through everything you need to know to start running colloid simulations with [HOOMD-blue] for research in our group.

Dissipative Particle Dynamics (DPD) or Brownian Dynamics (BD)

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/

[Last Update: November 2023]
<br>
<br>
## Before you Begin

If you are ordering or setting up a new computer:
* The [System Setup folder](/System-Setup) contains information for choosing a laptop or other workstation, and steps for setting up a new MacOS computer before installing HOOMD-blue.

If you are new to programming:
* The [Programming Resources folder](/Programming-Resources) contains some references that can help you get started the command line, VIM, Python, R, C++, Git/Github, and other skills that are useful for our work.

If you are running DPD sims:
* The [Background Reading folder](/Background-Reading) contains a quick overview of our DPD sims: what is DPD, what modifications do we make to DPD for colloids (and why), what is the Morse Potential we typically use, and how do we apply shear. The README in this folder also contains a list of important papers you should read at some point. 

The remaining files will help you install HOOMD-blue and VMD and start running colloid simulations.
<br>
<br>
## Installing Software and Running Simulations

Follow these guides to get set up with the Discovery Research Cluster, HOOMD-blue, VMD, and other tools:

1. [Accessing "Discovery"](/01-Accessing-Discovery.md) (Northeastern's HPC cluster)

1. The [HOOMD-blue Installation and Setup Guide](/01-HOOMDblue-Install-Guide.md)

2. An introduction to running a basic DPD simulation with HOOMD-blue: [Simulating waterDPD](/02-Simulating-waterDPD.md) (*to be updated for v3.0+*)

3. [The VMD Installation Guide](/03-VMD-Install-Guide.md)

4. An introduction to [Using VMD](/04-Using-VMD.md) to qualitiatively check your simulation results.

5. The [Analysis Guide](/05-Analysis-Guide.md) for quantitatively checking your results. 

6. An overview of simulating colloids: [Gelation and Shearing](/06-Gelation-and-Shearing.md)

7. [The Guide to Accessing "Discovery"](/07-Accessing-Discovery.md) (Northeastern's HPC cluster)

8. An [introduction to running HPC simulations](/08-Slurm-and-Disco.md)
