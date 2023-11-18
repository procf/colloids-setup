# HOOMD-blue Installation and Setup Guide

This is a guide to installing [HOOMD-blue] for use in the PRO-CF Colloids Team. This guide is optizimed for macOS and includes instructions for [installation on Discovery](/03-HOOMDblue-Install-Guide.md#installing-on-discovery) and [installation on your own computer](/03-HOOMDblue-Install-Guide.md#installing-on-your-local-computer).

[Last Update: November 2023]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh and streamlined and adapted for MPI by Dr. Deepak Mangal. This guide was compiled by Rob Campbell.

[HOOMD-blue]: https://glotzerlab.engin.umich.edu/hoomd-blue

## Contents
1. [HOOMD-blue Versions](/03-HOOMDblue-Install-Guide.md#hoomd-blue-versions)
2. [Installing on Discovery](/03-HOOMDblue-Install-Guide.md#installing-on-discovery)
	* [Setting Up File Management](/03-HOOMDblue-Install-Guide.md#disco-setting-up-file-management)
	* [Prerequisites](/03-HOOMDblue-Install-Guide.md#disco-prerequisites)
	* [Setting Up File Management](/03-HOOMDblue-Install-Guide.md#disco-setting-up-file-management)
	* [Installing hoomd3.1-basic](/03-HOOMDblue-Install-Guide.md#disco-installing-hoomd31-basic)
	* [Installing hoomd3.1-mod](/03-HOOMDblue-Install-Guide.md#disco-installing-hoomd31-mod)
	* [Installing the latest version](/03-HOOMDblue-Install-Guide.md#disco-installing-the-latest-version)
	* [Updating your installation](/03-HOOMD-blue-Install-Guide.md#disco-updating-your-installation)
3. [Installing on your local computer](/03-HOOMDblue-Install-Guide.md#installing-on-your-local-computer)
	* [Setting Up File Management](/03-HOOMDblue-Install-Guide.md#local-setting-up-file-management)
	* [Prerequisites](/03-HOOMDblue-Install-Guide.md#local-prerequisites)
	* [Setting Up File Management](/03-HOOMDblue-Install-Guide.md#local-setting-up-file-management)
	* [Installing hoomd3.1-basic](/03-HOOMDblue-Install-Guide.md#local-installing-hoomd31-basic)
	* [Installing hoomd3.1-mod](/03-HOOMDblue-Install-Guide.md#local-installing-hoomd31-mod)
	* [Installing the latest version](/03-HOOMDblue-Install-Guide.md#local-installing-the-latest-version)
	* [Updating your installation](/03-HOOMD-blue-Install-Guide.md#local-updating-your-installation)
8. [Next Steps](/03-HOOMDblue-Install-Guide.md#next-steps)
<br>

## HOOMD-blue Versions

In order to run most colloid simulations in the PRO-CF group, you will need e use a version of HOOMD-blue that has been modified. Each member of the group is developing their own modifications, but we try to collect the most important and commonly used changes into one core version of the software that is available to all group members on Github.

Until someone has the time to develop a plugin or work with the HOOMD-blue team to integrate these changes into the official software package, we will need to manually add these modifications to any new version of the HOOMD-blue software we decide to use. 
Our latest set of modifications were made to [HOOMD-blue version 4.2.1](https://hoomd-blue.readthedocs.io/en/v4.2.1/)

It is recommended that you install **at least 2 versions of HOOMD-blue**:
1. The standard [HOOMD-blue v4.2.1](https://hoomd-blue.readthedocs.io/en/v4.2.1/)
 (so that you have a reference for debugging)
2. Our core modified version, [hoomd4.2.1-mod](https://github.com/procf/hoomd4.2.1-mod/tree/main) 

(you can always install the [latest version of HOOMD-blue](https://hoomd-blue.readthedocs.io/en/latest/) or test other versions, as well)

All of the installation steps are outlined in the HOOMD-blue documentation, but we'll also walk through them here.
<br>
<br>
## Installing on Discovery

**You should install your own version(s) of HOOMD-blue in your folder on `/work/props`.**

Remember, you should **always** install software using a compute node and NOT the login node (either using an interactive srun session or an sbatch script). You will also need to load the modules for all the required software (i.e. Python, OpenMPI, etc.) before installing HOOMD-blue.

To simplify things we created sbatch scripts that completes all the steps for installation. They are available in the [Scripts/hpc](/Scripts/hpc) folder of this repository.

To access them on Discovery, clone this repository to your work folder
```bash
git clone git@github.com:procf/colloids-setup.git
```
and then copy the relevant scripts to the directory where you want to install HOOMD-blue. 

When you are ready to install, run the script with
```bash
sbatch script-name
```
etc.
<br>
<br>

## Installing on your local computer

### Setting Up File Management

This section gives recommendations for file organization. If you already have a file organization system you like to use you can skip this and jump to the[next section](/03-HOOMDblue-Install-Guide.md#local-prerequisites).

Whenever you open a new Terminal window you start in your `home` directory (AKA `~` or `Users/your_username`). To check this, open Terminal and enter the command for "present working directory" `pwd` to view your current location on the command line. It should look like this:
```bash
% pwd
/Users/your_username
```
You can view what is in the home directory with the command
```bash
ls
```

In the [Guide to Git and Github](https://github.com/procf/getting-started/blob/main/github-guide.md) we recommended keeping the `home` directory clean by creating a `src` or `repositories` directory to store your command line programming files. That is also where we recommend installing HOOMD-blue. 

Move to the `repositories` directory with
```bash
cd repositories
```
and make a new directory to for each HOOMD-blue version
```bash
mkdir hoomd4.2.1-basic
mkdir hoomd4.2.1-mod
```
We will install the two versions of HOOMD-blue in their respective directories. How you organize your simulation files from here is up to you. For backing up files to Github it is often best to keep software, simulation scripts, and data files all in separate repositories; however, some people prefer to keep things all those grouped into one directory. Here are two file management examples (`folders` and *files*):
<br>

ONE FOLDER
- `hoomd3.1-mod`
	- *software-installation*
	- `virtual-python-environment`
	- `sims`
		- `(simulation-project-name)`
			- *simulation-scripts*
			- *simulation-data-files*
			- *analysis-scripts*
			- *analysis-results*
<br>

SEPARATED FOLDERS
- `software`
	- `hoomd3.1-mod`
		- *software-installation*
		- `virtual-python-environment`
- `(simulation-project-name)`
	- `(project-name)-scripts` [backed-up-to-github]
		- *simulation-scripts*
		- *analysis-scripts*	
	- `sim-data`
		- `(simulation-run)`
			- *simulation-data-files*
			- `analysis`
				- *analysis-results*
		- `archive`
			- *archived-runs*
- `archive`
	- *old-projects*

**You can organize your files ANY way you like, just make sure you have some way of keeping track of what you're doing so you can find results later -- your future self will thank you!**
<br>
<br>
### Prerequisites

Our implementation of HOOMD-blue is currently **CPU only** (no GPU components), **with MPI enabled**.

Required for installation:
* macOS or Linux (this guide is optimized for macOS)
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


On a Mac most of these prerequisites will be installed with Xcode. See the [macOS System Setup Recommendations and Tips](/System-Setup/02-macOS-Setup.md) for information about getting a package manager (e.g. Homebrew) to instal software from the command line, and how to instal Xcode, set up Python 3, and instal CMake.

For more details on Git see the [Guide to Git and Github](https://github.com/procf/getting-started/blob/main/github-guide.md) in the "getting-started" repo.

You should install OpenMPI using [Homebrew](https://brew.sh/) or another package manager. 

NumPy can be added to your Python 3 installation with pip (see note on [virtual environments](/03-HOOMDblue-Install-Guide.md#creating-a-python-virtual-environment) below).

HOOMD-blue v3.1 comes with a script for installing pybind11, eigen, and cereal that we will use later on.

*Note: It is **not** recommended to install HOOMD-blue prerequisites with conda. See the HOOMD-blue docs page* [Installing from Binaries](https://hoomd-blue.readthedocs.io/en/v3.1.0/installation.html) *if you want to install with conda.*
<br>
<br>
### Installing hoomd3.1-basic

#### Getting the basic HOOMD-blue v3.1.0
The method of obtaining HOOMD-blue varies depending on which version you are trying to install.

To install HOOMD-blue 3.1.0 (an older version of HOOMD-blue) you need to use the release tarball for that version.

Move to your `hoomd3.1-basic` directory and download the HOOMD-blue v.3.1.0 tarball
```bash
curl -Lo hoomd-v3.1.0.tar.gz https://github.com/glotzerlab/hoomd-blue/releases/download/v3.1.0/hoomd-v3.1.0.tar.gz
```
Extract the files from the tarball (the "v" flag displays all the files being extracted)
```bash
tar -xvf hoomd-v3.1.0.tar.gz
```
You can then delete the tarball if you want
```bash
rm hoomd-v3.1.0.tar.gz
```

#### Creating a Python Virtual Environment
Before we install HOOMD-blue we need to create a virtual Python environment to work in. 

Virtual environments give you more control over which version of Python you are using (e.g. Python 3 vs Python 2) and let you create multiple different "development environments" with different packages installed (e.g. NumPy, SciPy, etc.). There are many ways to set up virtual Python environments (pyenv, venv, virtualenvwrapper, etc.), but HOOMD-blue recommends using venv. 

In your `hoomd3.1-basic` directory, create a new Python 3 virual environment called `hoomd-venv` with
```bash
python3 -m venv hoomd-venv
```
To use your virtual environment, source into it with
```bash
source hoomd-venv/bin/activate
```
The name of your virtual environment (hoomd-venv) will now appear in the command prompt
```bash
% source hoomd-venv/bin/activate
(hoomd-venv) % 
```
You can double check that you are now accessing the correct Python environment with the `which python` command
```bash
(hoomd-venv) % which python
/Users/your_username/repositories/hoomd3.1-basic/hoomd-venv/bin/python
```

#### Make sure you have Open-MPI installed
Make sure that you have installed Open-MPI
```
brew install open-mpi
```

#### Installing the basic HOOMD-blue v3.1.0
**Make sure you are in the `hoomd3.1-basic` directory and the correct vitual environemnt is activated**
```bash
(hoomd-venv) hoomd3.1-basic %
```

Install the remaining prerequisites (pybind11, eigen, cereal)
```bash 
python3 hoomd-v3.1.0/install-prereq-headers.py
```
(enter "y" to proceed when prompted)

Configure HOOMD-blue with cmake
```bash
cmake -B build/hoomd -S hoomd-v3.1.0 -DENABLE_MPI=on -DBUILD_HPMC=off -DBUILD_METAL=off -DBUILD_TESTING=off
```
Compile
```bash
cmake --build build/hoomd
```
And install
```bash
cmake --install build/hoomd
```

Upgrade pip and install required/useful Python packages
```bash
pip install --upgrade pip
pip3 install numpy
pip3 install gsd
pip3 install matplotlib
```
<br>

### Installing hoomd3.1-mod

#### Getting our modified HOOMD-blue v3.1
The method of obtaining HOOMD-blue varies depending on which version you are trying to install.

Our modifications for HOOMD-blue v.3.1.0 can be installed from the Github repository [hoomd3.1-mod](https://github.com/procf/hoomd3.1-mod) 

Move to your `hoomd3.1-mod` directory and clone our modifications from the Github repository
```bash
git clone git@github.com:procf/hoomd3.1-mod.git
```
**NOTE**: This filepath is a bit clunky (../hoomd3.1-mod/hoomd3.1-mod/), but it is the best way to keep your software installation and cloned git repo separate.
<br>

#### Creating a Python Virtual Environment
Before we install HOOMD-blue we need to create a virtual Python environment to work in. 

Virtual environments give you more control over which version of Python you are using (e.g. Python 3 vs Python 2) and let you create multiple different "development environments" with different packages installed (e.g. NumPy, SciPy, etc.). There are many ways to set up virtual Python environments (pyenv, venv, virtualenvwrapper, etc.), but HOOMD-blue recommends using venv. 

In your `hoomd3.1-mod` directory, create a new Python 3 virual environment called `hoomdmod-venv` with
```bash
python3 -m venv hoomdmod-venv
```
To use your virtual environment, source into it with
```bash
source hoomdmod-venv/bin/activate
```
The name of your virtual environment (hoomdmod-venv) will now appear in the command prompt
```bash
% source hoomdmod-venv/bin/activate
(hoomdmod-venv) % 
```
You can double check that you are now accessing the correct Python environment with the `which python` command
```bash
(hoomdmod-venv) % which python
/Users/your_username/repositories/hoomd3.1-mod/hoomdmod-venv/bin/python
```

#### Make sure you have Open-MPI installed
Make sure that you have installed Open-MPI
```
brew install open-mpi
```

#### Installing our modified HOOMD-blue v3.1
**Make sure you are in the `hoomd3.1-mod` directory and the correct vitual environemnt is activated**
```bash
(hoomdmod-venv) hoomd3.1-mod %
```

Install the remaining prerequisites (pybind11, eigen, cereal)
```bash 
python3 hoomd3.1-mod/hoomd-v3.1.0/install-prereq-headers.py
```
(enter "y" to proceed when prompted)

Configure HOOMD-blue with cmake
```bash
cmake -B build/hoomd -S hoomd3.1-mod/hoomd-v3.1.0 -DENABLE_MPI=on -DBUILD_HPMC=off -DBUILD_METAL=off -DBUILD_TESTING=off
```
Compile
```bash
cmake --build build/hoomd
```
And install
```bash
cmake --install build/hoomd
```

Upgrade pip and install required/useful Python packages
```bash
pip install --upgrade pip
pip3 install numpy
pip3 install gsd
pip3 install matplotlib
```
<br>

### Installing the latest version

To install the latest version of HOOMD-blue you can clone it directly from their Github repository. The installation steps after that are essentially the same, but with slightly different file paths.

Instructions for this are in the [HOOMD-blue docs](https://hoomd-blue.readthedocs.io/en/latest/building.html).
<br>
<br>
### Updating your installation

If you make any changes to HOOMD-blue's source code, you will need to recompile and reinstall the software.

**First, move to the directory for the version of HOOMD-blue you want to update is located (where the build directory is located), and source into the virtual environment**

Compile
```bash
cmake --build build/hoomd
```
And re-install
```bash
cmake --install build/hoomd
```
<br>

### Next Steps

You are now ready to use HOOMD-blue! See [Simulating waterDPD](/02-Simulating-waterDPD.md) for more information on running simulations and next steps.

