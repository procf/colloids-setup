# Simulating waterDPD

This is a guide for running a simple DPD simulation of water with HOOMD-blue in preparation for colloids research in the PRO-CF Colloids Team.

This guide is optimized for MacOS and useses the **basic installation of HOOMD-blue** (See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for prerequisites).

[Last Update: November 2023]

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/

## Contents
1. [Simulating Water](/04-Simulating-waterDPD.md#simulating-water)
2. [About sim-waterDPD.py](/04-Simulating-waterDPD.md#about-sim-waterdpdpy)
2. [Running sim-waterDPD.py on Discovery](/04-Simulating-waterDPD.md#running-sim-waterdpdpy-on-discovery)
3. [Running sim-waterDPD.py locally](/04-Simulating-waterDPD.md#running-sim-waterdpdpy-locally)
5. [Next Steps](/04-Simulating-waterDPD.md#next-steps)

<br>

## Simulating Water

Our group primarily uses two different types of simulations: Dissipative Particle Dynamics (DPD) simulations and Brownian Dynamics (BD) simulations. Both of these methods create many discrete particles to represent clusters of atoms in a system. The biggest difference between Brownian Dyanmics (BD) and Dissipative Particle Dynamics (DPD) is that we use DPD to create particles for two types of particles: one for colloidal particles, and one for solvent particles that represent the background fluid; however, in BD sims we only simulate colloid particles and calculate the effect of the background fluid separately. There are pros and cons to both methods, but our group started out focusing on DPD sims, so this tutorial also starts with DPD sims.

Since our DPD colloid simulations require at least two different types of particles and a number of modifications to the standard DPD methods included in HOOMD-blue, the first step is to start with an even simpler system with only one type of particle (more similar to a Brownian Dynamics system, but using standard DPD math) -- this is a simulation of water.

To understand the basics of how DPD simulations work, read the [into to DPD](/Background-Reading/1-DPD-8pg.pdf) (8 pages) PDF in the Background Reading folder.

This tutorial guides you through using HOOMD-blue to run a DPD simulation of a random distribution of water molecules. You will need the `sim-waterDPD.py` file provided in this repository to run this simulation.
<br>
<br>
## About sim-waterDPD.py

The Scripts folder contains files for running three different DPD simulations of water on Discovery or on your local computer. Both methods use the same Python scripts to run the simulations. The only difference is that the HPC version of the files includes a job script (an sbatch script similar to what we used to install HOOMD-blue).

Before we run these simulations, you can start by looking at the [first sim-waterDPD.py script here](/Scripts/waterDPD-sims/local-computer/01-waterDPD/sim-waterDPD.py)

You can view sim-waterDPD.py on Github using the link above, or download and open the file with an integrated development environment (IDE) such as [Spyder](https://www.spyder-ide.org/), [Eclipse](https://www.eclipse.org/downloads/), or [Pycharm](https://www.jetbrains.com/pycharm/), or with a built-in text editor such as [Vim](https://www.vim.org/)
To examine the file with Vim, in the Terminal use the command
```bash
cd [path-to-colloids-setup]
vim Scripts/waterDPD-sims/local-computer/01-waterDPD/sim-waterDPD.py 
```
*Note: In Vim, if you do not already have line numbering enabled you can turn it on with the command* `:set number` *or* `:set nu`<br>
(for more information on Vim basics, see the [macOS Setup guide](/System-Setup/02-macOS-Setup.md#text-editors) and the resources in [Foundational CS Skills](/Programming-Resources#foundational-cs-skills))

You will see that the `waterDPD.py` Python script is divided into 3 sections:
1. Module Library: importing a list of packages
2. Simulation Inputs: defining a set of input parameters
3. Simulation: our DPD simulation, divided into
	1. initializing a new system
	2. running a simulation with that system:
		* defining particle interactions
		* choosing how to integrate through time
		* setting up outputs 
		* and running the simulation

Our only output file is the GSD file, the native file format for HOOMD-blue. It stores the trajectories of all the particles in the system as a binary file with efficient random access to frames. We can use the GSD file with visualization tools (like VMD) to visually inspect the simulation, but later we will need to extract our quantitative data from the GSD file with the GSD Python API.
<br>
<br>
## Running sim-waterDPD.py on Discovery

Log in to Discovery and create a new folder for your waterDPD simulations:
```bash
ssh -Y your_username@login.discovery.neu.edu
```
```bash
cd /work/props/your_name/
mkdir waterDPD
cd waterDPD
```
Now copy the waterDPD scripts into this folder
```bash
cp -r /work/props/your_name/colloids-setup/Scripts/waterDPD-sims/hpc/* .
ls
```

sim-waterDPD.py uses the **basic installation** of HOOMD-blue. You will need to use Vim or another editor to update the path in the job script to match the path to your installation of hoomd4.2.1-basic:
```bash
cd 01-waterDPD
vim job-waterDPD
```

Once you have update the job script, you can go ahead and run it.
```bash
sbatch job-waterDPD
```

This should run very quickly! Successfully running the file will add the two output files to the directory: init.gsd and Equilibrium.gsd
```bash
(hoomd-venv) % ls
Equilibrium.gsd init.gsd waterDPD.py
```

If you open one of these GSD files with Vim, it will look like binary gibberish. To visualize the results, you will need the software VMD.

**NOTE: If you rerun waterDPD.py in the same folder, it will overwrite the output files**
<br>
<br>
## Running sim-waterDPD.py locally

If you haven't already, clone this repository to your computer. (see the [Github Guide](https://github.com/procf/getting-started/blob/main/github-guide.md) for help with git).
```bash
cd repositories/
git clone git@github.com:procf/colloids-setup.git
```
And copy the waterDPD scripts from the cloned copy of this repository into your repositories directory to create your own waterDPD project folder
```bash
cp -r ~/repositories/colloids-setup/Scripts/waterDPD-sims/local-computer waterDPD
```
<br>

waterDPD.py uses the **basic installation** of HOOMD-blue.

To run a simulation, source into your basic installation of HOOMD-blue:
```bash
source ~/repositories/hoomd4.2.1-basic/hoomd-venv/bin/activate
```

And run the simulation with
```bash
python sim-waterDPD.py
```

Successfully running the file will add the two output files to the directory: init.gsd and Equilibrium.gsd
```bash
(hoomd-venv) % ls
Equilibrium.gsd init.gsd waterDPD.py
```

If you open one of these GSD files with Vim, it will look like binary gibberish.

**NOTE: If you rerun waterDPD.py in the same folder, it will overwrite the output files**
<br>
<br>
## Next Steps

*Background Reading:*
* If you haven't already, read the [background guide on DPD](/Background-Reading/1-DPD-8pg.pdf) (8 pages)
* For more detail, see the journal paper: "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation](https://doi.org/10.1063/1.474784)" (1997)

*Exploring HOOMD-blue's Capabilities:*
* You can learn more about HOOMD-blue from the [HOOMD-blue docs Tutorials](https://hoomd-blue.readthedocs.io/en/latest/tutorial/00-Introducing-HOOMD-blue/00-index.html). 

*Visualizing Simulation Data*
* See the [VMD Installation Guide](/05-VMD-Install-Guide.md) to install VMD and get ready to visualize our simulation results.
