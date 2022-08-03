# PRO-CF Colloids Simulation Setup Guide

Welcome to the PRO-CF Colloids simulation team! :tada:

These files will guide you through everything you need to know to start running dissipative particle dynamics (DPD) simulations of colloids with [HOOMD-blue] for research in our group.

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/

[Last Update: August 2022]
<br>
<br>
## Before you Begin

The [System Setup folder](/System-Setup) contains information for choosing a laptop or other workstation, and steps for setting up a new MacOS computer before installing HOOMD-blue.

The [Programming Resources folder](/Programming-Resources) contains a variety of resources that can help you with the command line, VIM, Python, R, C++, Git/Github, and other skills that are useful for our work.

The [Background Reading folder](/Background-Reading) contains a series of short explainers on the basics of what we do: i.e. what is DPD, what modifications do we make to DPD for colloids (and why), what is the Morse Potential we typically use, and how do we apply shear. 

Once you have received and set up your computer, the remaining files should help you install HOOMD-blue and VMD and give you the information you need to get started with colloids simulations (including example [Scripts](/Scripts))
<br>
<br>
## Installing Software and Running Simulations

These guides are numbered to follow the steps for getting set up with HOOMD-blue, VMD, the Discovery Research Cluster, and other related tools for running and analyzing simulation data:

1. The [HOOMD-blue Installation and Setup Guide](/01-HOOMDblue-Install-Guide.md)

2. An introduction to running a basic DPD simulation with HOOMD-blue: [Simulating waterDPD](/02-Simulating-waterDPD.md) (*to be updated for v3.0+*)

3. [The VMD Installation Guide](/03-VMD-Install-Guide.md)

4. An introduction to [Using VMD](/04-Using-VMD.md) to qualitiatively check your simulation results.

5. The [Analysis Guide](/05-Analysis-Guide.md) for quantitatively checking your results. 

6. An overview of simulating colloids: [Gelation and Shearing](/06-Gelation-and-Shearing.md)

7. [The Guide to Accessing "Discovery"](/07-Accessing-Discovery.md) (Northeastern's HPC cluster)

8. An [introduction to running HPC simulations](/08-Slurm-and-Disco.md)
