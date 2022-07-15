# Modifying HOOMD-blue 

***TO BE UPDATED***

This is a guide to installing the base PRO-CF Colloids Team's modifications for HOOMD-blue for simulating shearing of colloidal gels and tracking the lifetime of DPD particle interactions.

This guide is optizimed for macOS. 

Before modifying HOOMD-blue you must install the base version HOOMD-blue. See the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md) for information on installing the base version of HOOMD-blue.

**Note: It is recommended that you ALWAYS have two verions of HOOMD-blue installed on your computer, the base HOOMD-blue and a modified HOOMD-blue.**

[Last Update: June 2022]

The modifications to HOOMD-blue were developed by Mohammad (Nabi) Nabizadeh as part of his PhD thesis. They were further streamlined and adapted for MPI by Dr. Deepak Mangal. This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Why Make Modifications](/06-Modifying-HOOMDblue.md#why-make-modifications)
2. [What a Modified Simulation Does](/06-Modifying-HOOMDblue.md#what-a-modified-simulation-does)
3. [Installing Our Existing Modifications](/06-Modifying-HOOMDblue.md#installing-our-existing-modifications)
4. [Working with the Existing Modifications](/06-Modifying-HOOMDblue.md#working-with-the-existing-modifications)
5. [Next Steps](/06-Modifying-HOOMDblue.md#next-steps)

<br>

## Why Make Modifications

## What a Modified Simulation Does

## Installing Our Existing Modifications

## Working with the Existing Modifications

## Next Steps

You should now have [installed HOOMD-blue](/01-HOOMDblue-Install-Guide.md), run a [basic DPD simulation of water](/02-Simulating-waterDPD.md), [installed](/03-VMD-Install-Guide.md) and [worked with](/04-Using-VMD.md) VMD to visualize your simulation, [run basic checks on the simulation](/05-Log-Analysis-with-R.md) using R to verify it ran correctly, and modified a version of HOOMD-blue for more advanced simulations.

*Background Reading:* If you haven't already, you should read the following papers:

* Background on DPD
	* "[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions]" (2015) 
	* "[Viscosity measurement techniques in Dissipative Particle Dynamics]" (2015)
	* "[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]" (1997)

* Background on more advanced simulations
	* "[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]" (2017)
	* "[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]" (2020)
	* "[Life and death of colloidal bonds control the rate-dependent rheology of gels]" (2021)

[Microstructure and rheology of soft to rigid shear-thickening colloidal suspensions]:https://sor.scitation.org/doi/10.1122/1.4931655
[Viscosity measurement techniques in Dissipative Particle Dynamics]:https://doi.org/10.1016/j.cpc.2015.05.027
[Dissipative particle dynamics: Bridging the gap between atomistic and mesoscopic simulation]:https://doi.org/10.1063/1.474784
[Microstructural Rearrangements and their Rheological Implications in a Model Thixotropic Elastoviscoplastic Fluid]:https://doi.org/10.1103/PhysRevLett.118.048003
[Time-rate-transformation framework for targeted assembly of short-range attractive colloidal suspensions]:https://doi.org/10.1016/j.mtadv.2019.100026
[Life and death of colloidal bonds control the rate-dependent rheology of gels]:https://doi.org/10.1038/s41467-021-24416-x
<br>
*Running More Complex Simulations:*

* See the overview on [gelation and shearing simulations](/07-Gelation-and-Shearing.md) for guidance on running more complex simulations.
