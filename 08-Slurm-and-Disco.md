# Running Simulations on Discovery

This is a guide to the basics of running DPD colloids simulations with HOOMD-blue using Discovery, Northeastern University's HPC cluster. 

This guide is optimized for macOS. See the [Guide to Accessing Discovery](/08-Accessing-Discovery.md) for prerequisites. This guide also assumes that you are familiar with the other content in this repository and know how to run DPD simulations of colloids with HOOMD-blue.

[Last Update: August 2022]

This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Running Jobs on Discovery](/08-Slurm-and-Disco.md#running-jobs-on-discovery)
2. [GitHub on Discovery](/08-Slurm-and-Disco.md#github-on-discovery)
3. [Installing HOOMD-blue on Discovery](/08-Slurm-and-Disco.md#installing-hoomd-blue-on-discovery)
4. [Writing sbatch Scripts](/08-Slurm-and-Disco.md#writing-sbatch-scripts)
5. [Monitoring a Job and Job Stats](/08-Slurm-and-Disco.md#monitoring-jobs-and-job-stats)
<br>

## Running Jobs on Discovery

When you sign into Discovery you are on the "login node" but you should **ALWAYS** run your jobs on a "compute node" using either srun (for interactive jobs) or sbatch (for scheduling jobs to run in the background).

The "s" in srun and sbatch stands for the [Slurm Workload Manager](https://slurm.schedmd.com/documentation.html), which is what most HPC clusters use to manage all the different "jobs" users are running. More information about Slurm is available in the [Discovery documentation](https://rc-docs.northeastern.edu/en/latest/using-discovery/usingslurm.html) and in this repository's [Programming Resources](/Programming-Resources#slurm).

Whether you are using srun or sbatch, you will only have access to the resources available on the partition you are running your job on. (e.g. a timelimit of <24hrs for the short partition vs. <5days for the long partition, certain CPU architectures are only available on certain partitions, etc.). Make sure that your job matches the [limits/requirements for the partition you are working on](https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html) before running it.

The [Discovery documentation has a full guide to srun](https://rc-docs.northeastern.edu/en/latest/using-discovery/srun.html) and the variety of flags that are available for customizing your session. The simplest way to use srun is to move to the first available compute node (with no restrictions on what type of node that is), and then use that node interactively as you normally would on your own computer. To do this, use the command:
```bash
srun --pty /bin/bash
```
OR, if you have X11 enabled for graphical interfaces, be sure to carry that over with
```bash
srun --pty --x11 /bin/bash
```
<br>

The [Discovery documentaion also has a full guide to sbatch](https://rc-docs.northeastern.edu/en/latest/using-discovery/sbatch.html). You can use sbatch to run a job in the background (on a *separate* compute node) from either the login node OR an srun session, but you will need to write a bash script with all of the commands you want to run.

We will use sbatch scripts to install HOOMD-blue in this tutorial.
<br>
<br>
## GitHub on Discovery

In order to install your own version of HOOMD-blue on the Discovery cluster you will first need to set up command line git.

This is the same as setting up git on your computer, but since Discovery runs Linux, you will need to use the Linux commands to link to GitHub.

First, login to Discovery and make sure you are in your home directory (`~` AKA `/home/your_username`)
```bash
ssh your_username@login.discovery.neu.edu
```
```bash
[your_username@login-01 ~]$ pwd
/home/your_username
```

Initialize git
```bash
git init
```
Congifure git with your GitHub username
```bash
% git config --global user.name "your_Github_username"
```
and set your email (use an email address that you have verified on Github)
```bash
% git config --global user.email "the_email_you_use_with_Github"
```
*Note: Your username and email will be recorded as part of the commit history of any repository you contribute to. If you would like your email to be kept private, you can use the Github-generated `users.noreply.github.com` email instead. To access this* [manage your email settings on Github](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address)

Follow Github's step-by-step instructions for setting up SSH Authentication on Linux, starting with [Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys).

You can now work with GitHub repositories on Discovery.
<br>
<br>
## Installing HOOMD-blue on Discovery

**You should install your own version(s) of HOOMD-blue in your folder on `/work/props`.**

As mentioned above, you should **always** install software using a compute node and NOT the login node (either using an interactive srun session or an sbatch script). You will also need to load the modules for all the required software (i.e. Python, OpenMPI, etc.) before installing HOOMD-blue.

To simplify things we created sbatch scripts that complete all the steps for installation. They are available in the [Scripts/hpc](/Scripts/hpc) folder of this repository.

To access them on Discovery, clone this repository to your work folder
```bash
git clone git@github.com:procf/colloids-setup.git
```
and then copy the relevant scripts to the directory where you want to install HOOMD-blue. 

When you are ready to install, run the script with
```bash
sbatch script-name
```
<br>

## Writing sbatch Scripts

An sbatch script is a bash file. Bash files that are *executable*, such as an sbatch script, typically are NOT given an extension as part of their name (i.e. they are called "script-name" NOT "script-name.bash").

In a bash file, `#` marks a bash command and `##` marks a comment.

Our bash files typically have 3 sections:

1. A bash script always starts with `#!/bin/bash`

2. Every line that starts with `#SBATCH` or `#sbatch` specifies an attribute related to the job we are running with Slurm. Typically this includes:
	* `-J name` or `--job-name=name` your reference name for the job
	* `-N #` or `--nodes=#` the number of nodes requested
	* `-n #` (for use with MPI) the number of cores requested on those nodes
	* `-t days-hours:min:sec` or `--time=days-hours:min:sec` the length of time requested for the job (all parameters are a number, for example "24:00:00" for 1 day or "4-12:00:00" for 4 and a half days)
	* `-p` or `--partition` the partition you want to work on (i.e. short, long, etc.) 
	* `--constraint=name` which lets you select specific types of CPU (for example, when running MPI scripts you should only use the newer cores with faster "Infiniband" communication, and you can select this with "--constraint=ib")
	* `--mem=#GB` for requesting specific memory allocation (we do not often use this)
	* `--gres` for setting GPU options (we don't use this with HOOMD-blue because we don't do GPU simulations)
	* `-o %A.out` or `--output=Output.%j.out` the name for standard output file (containing the text that would typically be displayed in the Terminal when a job is running, here it is instead saved to a file you can view later); by default slurm usually save standard output and standard error to the file "slurm-%j.out", where the "%j" is the job number, but you can specify a different name with these commands (%A is also the job number)
	* `-e %A.out` the name for the standard error file, if you want to separate out error text from output text

*When you are planning a job, it's recommended that you request more time than you need (i.e. plan a job that takes 12 hours to run and request the maximum 24 hours on the short partition to run it). This gives you built in time to fix the simulation if anything goes wrong.

As mentioned above, if you are running MPI simulations, it's also recommended that you only use the newest compute nodes, which use Infiniband for faster communication between nodes (turn this on with the "--constraint=ib" flag).*

3. After all of the sbatch commands have been set, enter the commands you want the job to run on Discovery. Typically this will be
	* purge software modules to remove any that are unneeded (a safety step)
	* load Python
	* source into your virtual environment
	* load additional required modules
	* run your simulation
<br>

## Monitoring Jobs and Job Stats

You can use squeue to view your current jobs, displaying the job number, partition it is running on, job name, the user running the job, the status (running/pending, etc.), the time the job has been running, the number of nodes being used, and a list of the specific node IDs
```bash
[your_username@login-00 ~ ]$ squeue -u your_username
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
```

Once a job is complete you can view how long it ran (as well as other stats) with the command
```bash
seff [jobID]
```

