# Simulating waterDPD

*TO BE UPDATED*

This is a guide for running a simple particle simulation with HOOMD-blue in preparation for colloids research in the PRO-CF Colloids Team.

This guide is optimized for MacOS. See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for prerequisites.

[Last Update: June 2022]

**NOTE:** waterDPD.py will NOT run correctly on the modified version of HOOMD-blue. It is recommended that you start getting familiar with simulations by using the standard installation of HOOMD-blue and running the waterDPD.py file according to this guide *before* you move to the modified installation and more complex simulations. 

[HOOMD-blue]: http://glotzerlab.engin.umich.edu/hoomd-blue/

## Contents
1. [Simulating Water](/02-Simulating-waterDPD.md#simulating-water)
2. [Getting `waterDPD.py`](/02-Simulating-waterDPD.md#getting-waterdpdpy)
3. [About `waterDPD.py`](/02-Simulating-waterDPD.md#about-waterdpdpy)
4. [Running a Simulation](/02-Simulating-waterDPD.md#running-a-simulation)
5. [Modifying waterDPD.py](/02-Simulating-waterDPD.md#modifying-waterdpdpy)
6. [Next Steps](/02-Simulating-waterDPD.md#next-steps)

<br>

## Simulating Water

A dissipative particle dynamics (DPD) simulation uses discrete particles to represent clusters of atoms in a system. Simulating a colloidal system will require at least two different types of particles (one for colloidal particles, and one for solvent particles that represent the background fluid). The first step is therefore to start with an even simpler system of just one type of particle: water.

This tutorial guides you through using HOOMD-blue to run a DPD simulation of a random distribution of water molecules. You will need the `waterDPD.py` file provided in this repository to run this simulation.
<br>
<br>
## Getting `waterDPD.py`

If you haven't already, clone this repository (or a fork of this repository) to your computer.<br>
*Note: For help setting up command line Git with Github, see the* [Github Guide](https://github.com/procf/getting-started/blob/main/github-guide.md) in the PRO-CF getting-started repository.
```bash
% cd repositories/
% git clone git@github.com:procf/colloids-setup.git
```
Move to the simulations directory in your "HOOMDblue" repository and make a directory for the water simulation
```bash
% cd ~/repostiories/HOOMDblue/sims/
% mkdir water
```
Move to the "water" directory and copy `waterDPD.py` into that directory from the cloned copy of this repository
```bash
% cd water
% cp ~/repositories/colloids-setup/waterDPD.py .
% ls
waterDPD.py
```
<br>

## About `waterDPD.py`

## Running a Simulation

## Modifying waterDPD.py

## Next Steps

*Background Reading:*
* To learn more about how we use DPD simulations for colloidal gels, see: "[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions](https://sor.scitation.org/doi/10.1122/1.4931655)" (2015) and "[Viscosity measurement techniques in Dissipative Particle Dynamics](https://doi.org/10.1016/j.cpc.2015.05.027)" (2015) <br>
* For more general background on DPD simulations, see: "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation](https://doi.org/10.1063/1.474784)" (1997)

*Exploring HOOMD-blue's Capabilities:*
* Now that you are familiar with using HOOMD-blue to run the `waterDPD.py` example, learn more about HOOMD-blue's capabilities by working through the examples in the "[Introducing HOOMD-blue](https://github.com/glotzerlab/hoomd-examples/tree/master/00-Introducing-HOOMD-blue)" repository from HOOMD-blue's developers.

*Analyzing Simulation Data*
* For next steps analyzing simulation data, see the [VMD Installation Guide](/03-VMD-Install-Guide.md) and [Log Analysis with R](/05-Log-Analysis-with-R.md).
