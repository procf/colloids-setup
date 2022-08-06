# Simulating waterDPD

This is a guide for running a simple DPD simulation of water with HOOMD-blue in preparation for colloids research in the PRO-CF Colloids Team.

This guide is optimized for MacOS and useses the **basic installation of HOOMD-blue** (See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for prerequisites).

[Last Update: August 2022]

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/

## Contents
1. [Simulating Water](/02-Simulating-waterDPD.md#simulating-water)
2. [Getting waterDPD Scripts](/02-Simulating-waterDPD.md#getting-waterdpd-scripts)
3. [About waterDPD](/02-Simulating-waterDPD.md#about-waterdpd)
4. [Running a Simulation](/02-Simulating-waterDPD.md#running-a-simulation)
5. [Modifying waterDPD.py](/02-Simulating-waterDPD.md#modifying-waterdpdpy)
6. [Next Steps](/02-Simulating-waterDPD.md#next-steps)

<br>

## Simulating Water

A dissipative particle dynamics (DPD) simulation uses discrete particles to represent clusters of atoms in a system. Simulating a colloidal system will require at least two different types of particles (one for colloidal particles, and one for solvent particles that represent the background fluid) and a number of modifications to standard DPD. Therefore, the first step is to start with an even simpler system of just one type of particle: water.

To understand the basics of how DPD simulations work, read the Background Reading [into to DPD](/Background-Reading/1-DPD-8pg.pdf) (8 pages).

This tutorial guides you through using HOOMD-blue to run a DPD simulation of a random distribution of water molecules. You will need the `waterDPD.py` file provided in this repository to run this simulation.
<br>
<br>
## Getting waterDPD Scripts

If you haven't already, clone this repository to your computer. (see the [Github Guide](https://github.com/procf/getting-started/blob/main/github-guide.md) for help with git).
```bash
cd repositories/
git clone git@github.com:procf/colloids-setup.git
```
Copy the waterDPD scripts from the cloned copy of this repository to make your own waterDPD project folder
```bash
cp -r ~/repositories/colloids-setup/Scripts/waterDPD .
```
<br>

## About waterDPD

Inside the waterDPD folder is the script waterDPD.py and an analysis folder (we'll come to the analysis folder in the next step)
```bash
% ls
analysis waterDPD.py
```

You can examine waterDPD.py with an integrated development environment (IDE) such as [Spyder](https://www.spyder-ide.org/), [Eclipse](https://www.eclipse.org/downloads/), or [Pycharm](https://www.jetbrains.com/pycharm/), or with a built-in text editor such as [Vim](https://www.vim.org/)
To examine the file with Vim, in the Terminal use the command
```bash
vim waterDPD.py
```
*Note: If you are viewing or editing* `waterDPD.py` *in an IDE you should already have line numbering enabled by default. If you are using Vim you will need to turn on line numbers with the command* `:set number` *or* `:set nu`<br>
(for more information on Vim basics, see the [macOS Setup guide](/System-Setup/02-macOS-Setup.md#text-editors) and the resources in [Foundational CS Skills](/Programming-Resources#foundational-cs-skills))

You will see that the `waterDPD.py` Python script is divided into 4 sections:
1. Module Library: importing a list of packages
2. Simulation Inputs: defining a set of input parameters
3. Simulation: our DPD simulation, divided into
	1. initializing a new system
	2. running a simulation with that system:
		* defining particle interactions
		* choosing how to integrate through time
		* setting up outputs 
		* and running the simulation

Our only output file is the GSD file, the native file format for HOOMD-blue. It stores the trajectories of all the particles in the system as a binary file with efficient random access to frames. This lets us use the GSD file with visualization tools (like VMD), but we will later need to extract data from the with the GSD Python API for qunatitative analysis of the system.
<br>
<br>
## Running a Simulation

To run a simulation, source into your basic installation of HOOMD-blue:
```bash
source [path-to-software]/hoomd3.1-basic/hoomd-venv/bin/activate
```

And run the simulation with
```bash
python waterDPD.py
```

Successfully running the file will add the two output files to the directory: init.gsd and Equilibrium.gsd
```bash
(hoomd-venv) % ls
Equilibrium.gsd init.gsd waterDPD.py
```

If you open one of these GSD files with vim, it will look like binary gibberish.
<br>
<br>
## Modifying waterDPD.py




## Next Steps

*Background Reading:*
* If you haven't already, read the [background guide on DPD](/Background-Reading/1-DPD-8pg.pdf) (8 pages)
* For more detail, see the journal paper: "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation](https://doi.org/10.1063/1.474784)" (1997)

*Exploring HOOMD-blue's Capabilities:*
* You can learn more about HOOMD-blue from the [HOOMD-blue docs Tutorials](https://hoomd-blue.readthedocs.io/en/latest/tutorial/00-Introducing-HOOMD-blue/00-index.html) and their matching Jupyter Notebooks available in the "[Introducing HOOMD-blue](https://github.com/glotzerlab/hoomd-examples/tree/master/00-Introducing-HOOMD-blue)" repository from HOOMD-blue's developers.

*Visualizing Simulation Data*
* See the [VMD Installation Guide](/03-VMD-Install-Guide.md) to install VMD and get ready to visualize our simulation results.
