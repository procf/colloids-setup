# HOOMD-blue Installation and Setup Guide

*to be added*

This is a guide to installing [HOOMD-blue] on **your own computer** for use in the PRO-CF Colloids Team. This guide is optizimed for MacOS. Information about using or re-installing HOOMD-blue on the Discovery HPC cluster is availabel in the guide to [Running Simulations on Discovery](10-Slurm-and-Disco.md).

[Last Update: July 2022]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh and streamlined and adapted for MPI by Dr. Deepak Mangal. This guide was compiled by Rob Campbell.

[HOOMD-blue]: https://glotzerlab.engin.umich.edu/hoomd-blue

## Contents
1. [HOOMD-blue Versions](/01-HOOMDblue-Install-Guide.md#hoomd-blue-versions)
2. [Prerequisites](/01-HOOMDblue-Install-Guide.md#prerequisites)
3. [Setting Up File Management](/01-HOOMDblue-Install-Guide.md#setting-up-file-management)
4. [Getting HOOMD-blue](/01-HOOMDblue-Install-Guide.md#getting-hoomd-blue)
5. [Creating a Python Virtual Environment](/01-HOOMDblue-Install-Guide.md#creating-a-python-virtual-environment)
6. [Installing HOOMD-blue](/01-HOOMDblue-Install-Guide.md#installing-hoomd-blue)
7. [Organizing Your Simulations](/01-HOOMDblue-Install-Guide.md#organizing-your-simulations)
8. [Next Steps](/01-HOOMDblue-Install-Guide.md#next-steps)
<br>

## HOOMD-blue Versions

HOOMD-blue is constantly being improved and updated! (there were 3 major updates releasted in the first six months of 2022)

Our implementation of HOOMD-blue includes several modifications to the base code specifically tailored for our approach to simulating colloidal systems. These changes are not yet collected into a published plugin for HOOMD-blue, nor have they been submitted to HOOMD-blue's team to be added to the main package. Until that happens, we need to manually add the modifications to any version of HOOMD-blue's base code we decide to use.

Our latest set of modifications were made to [HOOMD-blue version 3.1](https://hoomd-blue.readthedocs.io/en/v3.1.0/index.html)

It is recommended that you install **at least 2 versions of HOOMD-blue**:
1. The standard HOOMD-blue v3.1 (so it is available for debugging)
2. Our modified version of HOOMD-blue v3.1: [documented in the repository hoomd3.1-mod](https://github.com/procf/hoomd3.1-mod)

And if you're interested, you can always install the [latest version of HOOMD-blue](https://hoomd-blue.readthedocs.io/en/latest/)!

All of the installation steps are outlined in the HOOMD-blue documentation, but we'll walk through them here as well.
<br>
<br>
## Prerequisites

Our implementation of HOOMD-blue is currently **CPU only** (no GPU components), **with MPI enabled**.

Required for installation:
* MacOS or Linux (this guide is optimized for MacOS)
* (macOS only) Xcode
* A C++ compiler (HOOMD-blue is tested with gcc 7, 8, 9, 10, 11 / clang 6, 7, 8, 9, 10, 11, 12, 13)
* Python >= 3.6
* CMake >= 3.9
* Git
* OpenMPI
* NumPy >= 1.7
* pybind11 >= 2.2
* Eigen >= 3.2
* cereal >= 1.1

Xcode should incldue both clang and gcc on macOS. Python 2 is also included on macOS, but you will need to install Python 3 separately. See the [macOS System Setup Recommendations and Tips](/System-Setup/02-macOS-Setup.md) for information about getting a package manager for installing software from the command line (e.g. Homebrew), installing Xcode, setting up Python 3, and installing CMake.

You should already have set up git to access this repository. For more details on git see the [Guide to Git and Github](https://github.com/procf/getting-started/blob/main/github-guide.md) in the "getting-started" repo.

OpenMPI can be installed using [Homebrew](https://brew.sh/) or another package manager, and NumPy can be added to your Python 3 installation with pip (see note on [virtual environments](/01-HOOMDblue-Install-Guide.md#creating-a-python-virtual-environment) below).

HOOMD-blue v3.1 comes with a script for installing pybind11, eigen, and cereal that we will use later on.

*Note: It is not recommended to install HOOMD-blue prerequisites with conda. See the HOOMD-blue docs page* [Installing from Binaries](https://hoomd-blue.readthedocs.io/en/v3.1.0/installation.html) *if you want to install with conda.*
<br>
<br>
## Setting Up File Management

This section gives recommendations for file organization. If you already have a file organization system you like you can skip this-- open Terminal and move to the directory where you want to install HOOMD-blue, then skip to the [next section](/01-HOOMDblue-Install-Guide.md#getting-hoomd-blue)

Whenever you open a new Terminal window you start in your `home` directory (AKA `~` or `Users/your_username`). To check this, open Terminal and enter the command for "present working directory" `pwd` to view your current location on the command line. It should look like this:
```bash
% pwd
/Users/your_username
```
You can view what is in the home directory with the command
```bash
ls
```

In the [Guide to Git and Github](https://github.com/procf/getting-started/blob/main/github-guide.md) we recommended keeping the `home` directory clean by creating a `src` or `repositories` directory to store your command line programming files. This is where we recommend installing HOOMD-blue. 

Move to the `repositories` directory with
```bash
cd repositories
```
and make a new directory to for each HOOMD-blue version
```bash
mkdir hoomd3.1-basic
mkdir hoomd3.1-mod
```
We will install the two versions of HOOMD-blue in their respective directories. How you organize your simulation files from here is up to you. For backing up files to Github it is often best to keep simulation scripts and data files separate; however, some people prefer to keep things all in one directory. Here are two file management examples:
<br>

ONE FOLDER
- `hoomd3.1-mod`
	- *(software-installation)*
	- *(virtual-python-environment)*
	- `sims`
		- *(simulation-project-name)*
			- *(simulation-scripts)*
			- *(simulation-data-files)*
			- *(analysis-scripts)*
			- *(analysis-results)*
<br>

SEPARATED FOLDERS
- `software`
	- `hoomd3.1-mod`
		- *(software-installation)*
- *(simulation-project-name)*
	- *(project-name)*`-scripts` [backed-up-to-github]
		- *(simulation-scripts)*
		- *(analysis-scripts)*	
	- `sim-data`
		- *(simulation-run)*
			- *(simulation-data-files)*
			- `analysis`
				- *(analysis-results)*
		- `archive`
			- *(archived-runs)*
- `archive`
	- *(old-projects)*

**You can organize your files ANY way you like, just make sure you have some way of keeping track of what you're doing so you can find results later! Your future self will thank you!**

## Creating a Python Virtual Environment

## Acquiring HOOMD-blue

## Installing HOOMD-blue

## Organizing Your Simulations

## Next Steps

You are now ready to use HOOMD-blue! See [Simulating waterDPD](/02-Simulating-waterDPD.md) for more information on running simulations and next steps.

