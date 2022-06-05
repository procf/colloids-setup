# Gelation and Shearing of Colloidal Particles

This is an overview of the PRO-CF Colloids Team's workflows for running gelation and shearing simulations of colloidal particles with HOOMD-blue.

This guide is optizimed for MacOS. Before running gelation or shearing simulations you should have already [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and [modified a version of HOOMD-blue](/06-Modifying-HOOMDblue.md) for more advanced simulations.

[Last Update: June 2022]

These workflows were developed by Mohammad (Nabi) Nabizadehi as part of his PhD thesis. They were further streamlined and adapted for MPI by Dr. Deepak Mangal. This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Overview](/07-Gelation-and-Shearing.md#overview) 
2. [About Gelation Simulations](/07-Gelation-and-Shearing.md#about-gelation-simulations)
3. [[1] Running a Gelation Simulation](/07-Gelation-and-Shearing.md#1-running-a-gelation-simulation)
4. [[2] Checking Gelation](/07-Gelation-and-Shearing.md#2-checking-gelation)
5. [[3] Updating Lifetimes](/07-Gelation-and-Shearing.md#3-updating-lifetimes)
6. [About Shearing Simulations](/07-Gelation-and-Shearing.md#about-shearing-simulations)
7. [[4] Running a Shearing Simulation](/07-Gelation-and-Shearing.md#4-running-a-shearing-simulation)
8. [[5] Checking Shearing](/07-Gelation-and-Shearing.md#5-checking-shearing)
9. [[6]-[7] Updating Shear Lifetimes](/07-Gelation-and-Shearing.md#6-7-updating-shear-lifetimes)
10. [Next Steps](/07-Gelation-and-Shearing.md#next-steps)


<br>

## Overview 

## About Gelation Simulations

## [1] Running a Gelation Simulation

## [2] Checking Gelation

## [3] Updating Lifetimes

## About Shearing Simulations

## [4] Running a Shearing Simulation

## [5] Checking Shearing

## [6]-[7] Updating Shear Lifetimes

## Next Steps

This covers the basic outline of colloidal gel simulations! The rest is up to you and your research.

*HPC Computing:*
* See the remaining guides for information about [accessing](/09-Accessing-Discovery.md) Northeastern's HPC cluster, "Discovery," and [working with](/10-Slurm-and-Disco.md) HPC simulations.
<br>

*Background Reading:*

If you haven't already, you should review the following papers for more background on DPD simulations of colloidal gel rheology
* Background on DPD
	* "[Viscosity measurement techniques in Dissipative Particle Dynamics]" (2015)
	* "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]" (1997)

* Background on simulating colloidal gel rheology
	* "[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]" (2017)
	* "[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]" (2020)
	* "[Life and death of colloidal bonds control the rate-dependent rheology of gels]" (2021)

[Viscosity measurement techniques in Dissipative Particle Dynamics]:https://doi.org/10.1016/j.cpc.2015.05.027
[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]:https://doi.org/10.1063/1.474784
[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]:https://doi.org/10.1103/PhysRevLett.118.048003
[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]:https://doi.org/10.1016/j.mtadv.2019.100026
[Life and death of colloidal bonds control the rate-dependent rheology of gels]:https://doi.org/10.1038/s41467-021-24416-x


