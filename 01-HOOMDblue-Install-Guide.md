# HOOMD-blue Installation and Setup Guide

*to be added*

This is a guide to installing [HOOMD-blue] for use in the PRO-CF Colloids Team. This guide is optizimed for MacOS.

[Last Update: July 2022]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh and streamlined and adapted for MPI by Dr. Deepak Mangal. This guide was compiled by Rob Campbell.

[HOOMD-blue]: https://glotzerlab.engin.umich.edu/hoomd-blue

## Contents
1. [HOOMD-blue Versions](/01-HOOMDblue-Install-Guide.md#hoomd-blue-versions)
2. [Prerequisites](/01-HOOMDblue-Install-Guide.md#prerequisites)
3. [Setting Up Source Repositories](/01-HOOMDblue-Install-Guide.md#setting-up-source-repositories)
4. [Creating a Python Virtual Environment](/01-HOOMDblue-Install-Guide.md#creating-a-python-virtual-environment)
5. [Acquiring HOOMD-blue](/01-HOOMDblue-Install-Guide.md#acquiring-hoomd-blue)
6. [Installing HOOMD-blue](/01-HOOMDblue-Install-Guide.md#installing-hoomd-blue)
7. [Organizing Your Simulations](/01-HOOMDblue-Install-Guide.md#organizing-your-simulations)
8. [Next Steps](/01-HOOMDblue-Install-Guide.md#next-steps)
<br>

## HOOMD-blue Versions

HOOMD-blue is constantly being improved and updated! (there were 3 major updates releasted in the first six months of 2022)

Our implementation of HOOMD-blue includes several modifications to the base code specifically tailored for our approach to simulating colloidal systems. These changes are not yet collected into a published plugin for HOOMD-blue, nor have they been submitted to HOOMD-blue's team to be added to the main package. Until that happens, we need to manually add the modifications to any version of HOOMD-blue's base code we decide to use.

Our latest set of modifications were made to HOOMD-blue version 3.1

It is recommended that you install **at least 2 versions of HOOMD-blue**:
1. The [standard HOOMD-blue v3.1](https://hoomd-blue.readthedocs.io/en/v3.1.0/index.html) (so it is available for debugging)
2. The modified HOOMD-blue v3.1: available in the repository [hoomd3.1-mod](/procf/hoomd3.1-mod)

And if you're interested, you can always install the [latest version of HOOMD-blue](https://hoomd-blue.readthedocs.io/en/latest/) as well!

All of the installation steps are outlined in the HOOMD-blue documentation, but we'll walk through them here as well.

Our implementation of HOOMD-blue is currently **CPU only** (no GPU components), **with MPI enabled**.
<br>
<br>
## Prerequisites

## Setting Up Source Repositories

## Creating a Python Virtual Environment

## Acquiring HOOMD-blue

## Installing HOOMD-blue

## Organizing Your Simulations

## Next Steps

You are now ready to use HOOMD-blue! See [Simulating waterDPD](/02-Simulating-waterDPD.md) for more information on running simulations and next steps.

