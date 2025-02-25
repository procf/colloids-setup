# HOOMD-blue Installation and Setup Guide

This is a guide to installing [HOOMD-blue] for use in the Rheoinformatic Colloids Team. This guide is optizimed for macOS and includes instructions for [installation on Discovery](/03-HOOMDblue-Install-Guide.md#installing-on-discovery) and [installation on your own computer](/03-HOOMDblue-Install-Guide.md#installing-on-your-local-computer).

[Last Update: November 2023]

The standard implementation of HOOMD-blue was adapted for our colloids simulations by Mohammad (Nabi) Nabizadeh and streamlined and adapted for MPI by Dr. Deepak Mangal. This guide was compiled by Rob Campbell.

[HOOMD-blue]: https://glotzerlab.engin.umich.edu/hoomd-blue

## Contents
1. [HOOMD-blue Versions](/03-HOOMDblue-Install-Guide.md#hoomd-blue-versions)
2. [Setting Up File Management](/03-HOOMDblue-Install-Guide.md#setting-up-file-management)
2. [Installing on Discovery](/03-HOOMDblue-Install-Guide.md#installing-on-discovery)
	* [Creating the software directory](/03-HOOMDblue-Install-Guide.md#disco-creating-the-software-directory)
	* [Prerequisites](/03-HOOMDblue-Install-Guide.md#disco-prerequisites)
	* [Installing hoomd basic](/03-HOOMDblue-Install-Guide.md#disco-installing-hoomd-basic)
	* [Installing hoomd mod](/03-HOOMDblue-Install-Guide.md#disco-installing-hoomd-mod)
	* [Updating your installation](/03-HOOMDblue-Install-Guide.md#disco-updating-your-installation)
3. [Installing on your local computer](/03-HOOMDblue-Install-Guide.md#installing-on-your-local-computer)	
	* [Creating the software directory](/03-HOOMDblue-Install-Guide.md#local-creating-the-software-directory)
	* [Prerequisites](/03-HOOMDblue-Install-Guide.md#local-prerequisites)
	* [Installing hoomd basic](/03-HOOMDblue-Install-Guide.md#local-installing-hoomd-basic)
	* [Installing hoomd mod](/03-HOOMDblue-Install-Guide.md#local-installing-hoomd-mod)
	* [Updating your installation](/03-HOOMDblue-Install-Guide.md#local-updating-your-installation)
8. [Next Steps](/03-HOOMDblue-Install-Guide.md#next-steps)
<br>

## HOOMD-blue Versions

In order to run most colloid simulations in the Rheoinformatic group, you will need e use a version of HOOMD-blue that has been modified. Each member of the group is developing their own modifications, but we try to collect the most important and commonly used changes into one core version of the software that is available to all group members on Github.

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
## Setting Up File Management

We will install the two versions of HOOMD-blue in their respective directories. How you organize your simulation files from here is up to you. For backing up files to Github it is often best to keep software, simulation scripts, and data files all in separate directories; however, some people prefer to keep things all those grouped into one directory. Here are two file management examples (filenames are marked as `folders` or *files*):
<br>

ONE FOLDER
- `hoomd4.2.1-mod`
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
	- `hoomd4.2.1-mod`
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
## Installing on Discovery

**You should install your own version(s) of HOOMD-blue in your folder on `/work/props`.**

The easiest way to do that is by cloning a copy of the existing hoom4.2.1-mod repository. You can then easily download changes made by others and add your changes to the main copy.

**NOTE:** If you plan on making your own changes to the source code you should either (a) move to a new branch of the hoomd4.2.1-mod repo, or (b) fork an independent copy of the hoomd4.2.1-mod repo that you can edit separate from the core mods. **Please discuss with the other members of the group if you have any questions about these options**

To simplify things we created sbatch scripts that complete all the steps for installation. You can also install HOOMD-blue using srun (if you copy and paste the commands from the sbatch scripts and run them individually). The rest of the Discovery installation guide will show you how to use the sbatch scripts, and the local guide will go through the commands step-by-step.

Remember, you should **always** install software using a compute node and NOT the login node (either using an interactive srun session or an sbatch script). You will also need to load the modules for all the required software (i.e. Python, OpenMPI, etc.) before installing HOOMD-blue.<
<br>
<br>
### [DISCO] Creating the software directory

When you login to Discovery you will start in your `home` directory. This is NOT a good place to install software. Instead you should move to your folder on either `scratch` or `work` (it is better to use `work` if you have access to it, because files on `scratch` will be deleted at the end of each month).
```bash
cd /work/props/your_username
mkdir software
mkdir software/hoomd4.2.1-basic
mkdir software/hoomd4.2.1-mod
```
You can also view what is in the current directory with the command
```bash
ls
```
<br>

### [DISCO] Prerequisites

Our implementation of HOOMD-blue is currently **CPU only** (no GPU components), **with MPI enabled**.

Required for installation:
* macOS or Linux (Discovery uses Linux)
* A C++ compiler (HOOMD-blue is tested with gcc 7, 8, 9, 10, 11 / clang 6, 7, 8, 9, 10, 11, 12, 13)
* Python >= 3.6
* CMake >= 3.9
* Git
* OpenMPI
* NumPy >= 1.7
* pybind11 >= 2.2
* Eigen >= 3.2
* cereal >= 1.1

On Discovery most of these prerequisites are available as modules. The sbatch scripts will load Python 3.8.1, CMake 3.18.1, gcc 11.1.0, and OpenMPI 4.1.2

HOOMD-blue v4.2.1 comes with a script for installing pybind11, eigen, and cereal that the sbatch scripts will use to fulfill those prerequisites.

And then the sbatch script will use pip to install NumPy and other useful python packages.
<br>
<br>
### [DISCO] Installing hoomd basic

The sbatch script for installing the standard HOOMD-blue v4.2.1 (what we call hoom4.2.1-basic) is available in this repository in the [Scripts/install-update-hoomd4.2.1basic](/Scripts/install-update-hoomd4.2.1basic) folder.

To use it, first make sure you are in your `work` or `scratch` directory:
```bash
cd /work/props/your_username
pwd
```
Then, clone this repository to create a new copy of the colloids-setup folder:
```bash
git clone git@github.com:procf/colloids-setup.git
```
NOTE: you need to link Git on Discovery with your Github account before doing this, because the colloids-setup repo is not public. See the [guide to accessing Discovery](/01-Accessing-Discovery.md#git-and-github-on-discovery) for more details.

Now move to the hoomd4.2.1-basic directory and copy the sbatch installation script from the colloids-setup folder.
```bash
cd software/hoomd4.2.1-basic
cp /work/props/your_username/colloids-setup/Scripts/hoomd-blue-4.2.1.tar.gz .
cp /work/props/your_username/colloids-setup/Scripts/install-hoomd-basic .
```

And run the installation script:
```bash
sbatch install-hoomd-basic
```

This job should take between 20-40min.
<br>
<br>
### [DISCO] Installing hoomd mod

The sbatch script for installing the modified version of HOOMD-blue v4.2.1 (what we call hoomd4.2.1-mod) is included as part of the hoomd4.2.1-mod repo.

To use it, make sure you are in your hoomd4.2.1-mod directory:
```bash
cd /work/props/your_username/software/hoomd4.2.1-mod
pwd
```
Then, clone the hoomd4.2.1-mod repository into that folder:
```bash
git clone git@github.com:procf/hoomd4.2.1-mod.git
```
NOTE: you need to link Git on Discovery with your Github account before doing this, because the hoomd4.2.1-mod repo is not public. See the [guide to accessing Discovery](/01-Accessing-Discovery.md#git-and-github-on-discovery) for more details.

Now, move to the `scripts` subfolder where the install script is located
```bash
cd /hoomd4.2.1-mod/scripts/install-update/
```

And run the installation script:
```bash
sbatch install-hoomd-mod
```

This job should take between 20-40min.

**NOTE:** After you are finished and confirm there were no errors, you should delete the log files that are created in this folder ([jobid].err and [jobid].out)
```bash
rm *.err
rm *.out
```

You should also run all your simulation scripts OUTSIDE the github folder (i.e. put them inside /work/props/your_username/software/hoomd4.2.1/ and do NOT put them in /work/props/your_username/software/hoomd4.2.1/hoomd4.2.1/ ) 
<br>
<br>
### [DISCO] Updating your installation

To update either of your installations (i.e. after making any additional changes) you only need to "build" and "install" the software. You can use the provided update scripts for this:

For hoomd4.2.1-basic:
```bash
cd /work/props/your_username/software/hoomd4.2.1-basic
cp /work/props/your_username/colloids-setup/Scripts/update-hoomd-basic .
sbatch update-hoomd-basic
```

For hoomd4.2.1-mod:
```bash
cd /work/props/your_username/software/hoomd4.2.1-mod/hoomd4.2.1-mod/scripts/install-update
sbatch update-hoomd-mod
```
And then remove the log files after the update is completed successfully:
```bash
rm *.err
rm *.out
```
<br>

## Installing on your local computer

### [LOCAL] Creating the software directory

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
<br>

### [LOCAL] Prerequisites

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


On a Mac most of these prerequisites will be installed with Xcode. Mac computers come with both Python 2 and Python 3. You should NEVER use Python 2, only Python 3, and you may need to install a new version of Python 3 to run HOOMD-blue. See the [macOS System Setup Recommendations and Tips](/System-Setup/02-macOS-Setup.md) for information about getting a package manager (e.g. Homebrew) to instal software from the command line, and for information on how to instal Xcode, set up Python 3, and install CMake.

For more details on Git see the [Guide to Git and Github](https://github.com/procf/getting-started/blob/main/github-guide.md) in the "getting-started" repo.

You should install OpenMPI using [Homebrew](https://brew.sh/) or another package manager. 

NumPy can be added to your Python 3 installation with pip (see note on [virtual environments](/03-HOOMDblue-Install-Guide.md#creating-a-python-virtual-environment) below).

HOOMD-blue v4.2.1 comes with a script for installing pybind11, eigen, and cereal that we will use later on.

*Note: It is **not** recommended to install HOOMD-blue prerequisites with conda. See the HOOMD-blue docs page* [Installing from Binaries](https://hoomd-blue.readthedocs.io/en/v4.2.1/installation.html) *if you want to install with conda.*
<br>
<br>
### [LOCAL] Installing hoomd basic

#### Getting the basic HOOMD-blue v4.2.1
The method of obtaining HOOMD-blue varies depending on which version you are trying to install.

To install HOOMD-blue 4.2.1 (an older version of HOOMD-blue) you need to use the release tarball for that version.

Move to your `hoomd4.2.1-basic` directory and download the HOOMD-blue v.4.2.1 tarball
```bash
curl -Lo hoomd-v4.2.1.tar.gz https://github.com/glotzerlab/hoomd-blue/releases/download/v4.2.1/hoomd-v4.2.1.tar.gz
```
Extract the files from the tarball (the "v" flag displays all the files being extracted)
```bash
tar -xvf hoomd-v4.2.1.tar.gz
```
You can then delete the tarball if you want
```bash
rm hoomd-v4.2.1.tar.gz
```

#### Creating a Python Virtual Environment
Before we install HOOMD-blue we need to create a virtual Python environment to work in. 

Virtual environments give you more control over which version of Python you are using (e.g. Python 3 vs Python 2) and let you create multiple different "development environments" with different packages installed (e.g. NumPy, SciPy, etc.). There are many ways to set up virtual Python environments (pyenv, venv, virtualenvwrapper, etc.), but HOOMD-blue recommends using venv. 

In your `hoomd4.2.1-basic` directory, create a new Python 3 virual environment called `hoomd-venv` with
```bash
python3 -m venv hoomd4.2.1-venv
```
To use your virtual environment, source into it with
```bash
source hoomd4.2.1-venv/bin/activate
```
The name of your virtual environment (hoomd4.2.1-venv) will now appear in the command prompt, like this
```bash
% source hoomd4.2.1-venv/bin/activate
(hoomd-venv) % 
```
You can double check that you are now accessing the correct Python environment with the `which python` command
```bash
(hoomd-venv) % which python
/Users/your_username/repositories/hoomd4.2.1-basic/hoomd4.2.1-venv/bin/python
```

#### Make sure you have Open-MPI installed
Make sure that you have installed Open-MPI
```
brew install open-mpi
```

#### Installing the basic HOOMD-blue v4.2.1
**Make sure you are in the `hoomd4.2.1-basic` directory and the correct vitual environemnt is activated**
```bash
(hoomd4.2.1-venv) hoomd4.2.1-basic %
```

Install the remaining prerequisites (pybind11, eigen, cereal)
```bash 
python3 hoomd-v4.2.1/install-prereq-headers.py
```
(enter "y" to proceed when prompted)

Configure HOOMD-blue with cmake
```bash
cmake -B build/hoomd -S hoomd-v4.2.1 -DENABLE_MPI=on -DBUILD_HPMC=off -DBUILD_METAL=off -DBUILD_TESTING=off
```
Compile
```bash
cmake --build build/hoomd
```
And install
```bash
cmake --install build/hoomd
```

Upgrade pip and install required/useful Python packages<br>
*NOTE:* the latest version of gsd requires Numpy 2.0, which was released in June 2024 and (as of June 2024) is not yet available on Discovery; therefore, you must install an older gsd version for now
```bash
pip install --upgrade pip
pip3 install numpy
pip3 install gsd==3.2.1
pip3 install matplotlib
```

You can now run simulations using the standard version of HOOMD-blue v4.2.1
<br>

### [LOCAL] Installing hoomd mod

#### Getting our modified HOOMD-blue v4.2.1

Our modifications for HOOMD-blue v4.2.1 can be installed from the Github repository [hoomd4.2.1-mod](https://github.com/procf/hoomd4.2.1-mod) 

Move to your `hoomd4.2.1-mod` directory and clone our modifications from the Github repository
```bash
git clone git@github.com:procf/hoomd4.2.1-mod.git
```
**NOTE**: This filepath is a bit clunky (../hoomd4.2.1-mod/hoomd4.2.1-mod/), but it is the best way to keep your software installation and cloned git repo separate.
<br>

#### Creating a Python Virtual Environment
Before we install HOOMD-blue we need to create a virtual Python environment to work in. 

Virtual environments give you more control over which version of Python you are using (e.g. Python 3 vs Python 2) and let you create multiple different "development environments" with different packages installed (e.g. NumPy, SciPy, etc.). There are many ways to set up virtual Python environments (pyenv, venv, virtualenvwrapper, etc.), but HOOMD-blue recommends using venv. 

In your `hoomd4.2.1-mod` directory, create a new Python 3 virual environment called `hoomdmod4.2.1-venv` with
```bash
python3 -m venv hoomdmod4.2.1-venv
```
To use your virtual environment, source into it with
```bash
source hoomdmod4.2.1-venv/bin/activate
```
The name of your virtual environment (hoomdmod-venv) will now appear in the command prompt like this:
```bash
% source hoomdmod4.2.1-venv/bin/activate
(hoomdmod-venv) % 
```
You can double check that you are now accessing the correct Python environment with the `which python` command
```bash
(hoomdmod-venv) % which python
/Users/your_username/repositories/hoomd4.2.1-mod/hoomdmod4.2.1-venv/bin/python
```

#### Make sure you have Open-MPI installed
Make sure that you have installed Open-MPI
```
brew install open-mpi
```

#### Installing our modified HOOMD-blue v4.2.1
**Make sure you are in the `hoomd4.2.1-mod` directory and the correct vitual environemnt is activated**
```bash
(hoomdmod-venv) hoomd4.2.1-mod %
```

Install the remaining prerequisites (pybind11, eigen, cereal)
```bash 
python3 hoomd4.2.1-mod/hoomd-v4.2.1-procf/install-prereq-headers.py
```
(enter "y" to proceed when prompted)

Configure HOOMD-blue with cmake
```bash
cmake -B build/hoomd -S hoomd4.2.1-mod/hoomd-v4.2.0-procf -DENABLE_MPI=on -DBUILD_HPMC=off -DBUILD_METAL=off -DBUILD_TESTING=off
```
Compile
```bash
cmake --build build/hoomd
```
And install
```bash
cmake --install build/hoomd
```

Upgrade pip and install required/useful Python packages <br>
*NOTE:* the latest version of gsd requires Numpy 2.0, which was released in June 2024 and (as of June 2024) is not yet available on Discovery; therefore, you must install an older gsd version for now
```bash
pip install --upgrade pip
pip3 install numpy
pip3 install gsd==3.2.1
pip3 install matplotlib
```

You can now run simulations using HOOMD-blue v4.2.1 with the core modifications from our group
<br>

### [LOCAL] Updating your installation

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

You are now ready to use HOOMD-blue! See [Simulating waterDPD](/04-Simulating-waterDPD.md) for more information on running simulations and next steps.

