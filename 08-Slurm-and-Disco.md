# Running Simulations on Discovery

***TO BE UPDATED***

This is a guide to the basics of running DPD colloids simulations with HOOMD-blue using Discovery, Northeastern University's HPC cluster. 

This guide is optimized for macOS. See the [Guide to Accessing Discovery](/08-Accessing-Discovery.md) for prerequisites. This guide also assumes that you are familiar with the other content in this repository and know how to run DPD simulations of colloids with HOOMD-blue.

[Last Update: August 2022]

This guide was compiled by Rob Campbell.
<br>

## Contents
1. [GitHub and Discovery](/08-Slurm-and-Disco.md#github-and-discovery)
1. [Installing HOOMD-blue on Discovery](/08-Slurm-and-Disco.md#installing-hoomd-blue-on-discovery)
2. [Scheduling a Job with Slurm](/08-Slurm-and-Disco.md#scheduling-a-job-with-slurm)
3. [Monitoring a Running Job](/08-Slurm-and-Disco.md#monitoring-a-running-job)
<br>

## GitHub and Discovery

In order to install your own version of HOOMD-blue on the Discovery cluster you will first need to set up command line git.

Since Discovery runs Linux, you will need to use the Linux commands to link to GitHub:

Login to Discovery and make sure you are in your home directory (`~` AKA `/home/your_username`)
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
Congifure git with your GitHub credentials
```bash
% git config --global user.name "your_Github_username"
```
and set your email (use an email address that you have verified on Github)
```bash
% git config --global user.email "the_email_you_use_with_Github"
```
*Note: Your username and email will be recorded as part of the commit history of any repository you contribute to. If you would like your email to be kept private, you can use the Github-generated `users.noreply.github.com` email instead. To access this* [manage your email settings on Github](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-user-account/managing-email-preferences/setting-your-commit-email-address)

Follow the Github's step-by-step instructions on setting up SSH Authentication on Linux, starting with [Checking for existing SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys).

You can now work with private Github repositories on Discovery.
<br>
<br>
## Installing HOOMD-blue on Discovery

You should install your own version(s) of HOOMD-blue in your folder on `/work/props`.


Go to the your folder on the `work` directory and create a new folder for your installation of HOOMD-blue.
```bash
[your_username@login-00 ~]$ cd /work/props/yourname/HOOMD-blue
[your_username@login-00 HOOMD-blue]$ 
```
Before installing HOOMD-blue you will need to load some software. Check your currently loaded software first. You should see the module needed to interact with discovery and any other software you have already loaded
```bash
[yourusername@login-00 HOOMD-blue]$ module list
  1) discovery/2021-10-6
```
As discussed in the [HOOMD-blue Installation Guide](/01-HOOMDblue-Install-Guide.md), we will need Python 3 and cmake. Load the latest version of both (unless you know a different version will be necessary for your code). At the time of writing, these are Python 3.8.1 and cmake 3.18.1
```bash
[your_username@login-00 HOOMD-blue]$ module load python/3.8.1
[your_username@login-00 HOOMD-blue]$ module load cmake/3.18.1 
[your_username@login-00 HOOMD-blue]$ module list
  1) discovery/2021-10-06   2) python/3.8.1           3) cmake/3.18.1
```
Now create your virual environment
```bash
[your_username@login-00 HOOMD-blue]$ mkdir VirtEnv
[your_username@login-00 HOOMD-blue]$ python3 -m venv VirtEnv/ --system-site-packages
```
Download and unzip HOOMD-blue 2.9.7
```bash
[your_username@login-00 HOOMD-blue]$ curl -O https://glotzerlab.engin.umich.edu/Downloads/hoomd/hoomd-v2.9.7.tar.gz 
[your_username@login-00 HOOMD-blue]$ tar -xf hoomd-v2.9.7.tar.gz
```
Then enter the virtual environment and make sure you are using the correct version of Python. It should be the version located at your virtual environment NOT the version on Discovery's shared drive (you can compare with the location of cmake)
```bash
[yourusername@login-00 HOOMD-blue]$ source VirtEnv/bin/activate
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ which python
/work/props/yourusername/HOOMD-blue/VirtEnv/bin/python
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ which cmake
/shared/centos7/cmake/3.18.1/bin/cmake
```
Finally, move to the hoomd-v2.9.7 folder and create (and move to) the build folder, configure HOOMD-blue (ignoring the GPU options), and then compile and install HOOMD-blue
```bash
(VirtEnv) [yourusername@login-00 HOOMD-blue]$ cd hoomd-v2.9.7
(VirtEnv) [yourusername@login-00 hoomd-v2.9.7]$ mkdir build && cd build
(VirtEnv) [yourusername@login-00 build]$ cmake ../ -DCMAKE_INSTALL_PREFIX=`python3 -c "import site; print(site.getsitepackages()[0])"` 
(VirtEnv) [yourusername@login-00 build]$ make -j4
(VirtEnv) [yourusername@login-00 build]$ make install 
```
***NOTE: These last 2 steps can take several hours***

Once you have installed the base version of HOOMD-blue you will want to modify it with the files described in [Modifying HOOMD-blue](/06-Modifying-HOOMDblue.md). Copy those files into your new installation of HOOMD-blue and then recompile and reinstall the software to make sure you are running the correct version (this should be faster than the first installation).

When you are finished with the installation you should also unload the modules you are no longer using
```bash

[yourusername@login-00 HOOMD-blue]$ module list
  1) discovery/2021-10-06   2) python/3.8.1           3) cmake/3.18.1
[yourusername@login-00 HOOMD-blue]$ module unload python/3.8.1
[yourusername@login-00 HOOMD-blue]$ module unload cmake/3.18.1
[yourusername@login-00 HOOMD-blue]$ module list
  1) discovery/2021-10-6
```
<br>

## Scheduling a Job with Slurm

It is best practice to use a bash file (i.e. `exec.bash`) to submitting a job on Discovery. This file will use the [Slurm Workload Manager](https://slurm.schedmd.com/documentation.html) to manage the job. More information about Slurm is available in the [Discovery documentation](https://rc-docs.northeastern.edu/en/latest/using-discovery/usingslurm.html) and in this repository's [Programming Resources](/Programming-Resources#slurm).

You can also view an example [exec.bash](/exec.bash) file.

Make sure that your job matches the [limits/requirements for the partition you are working on](https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html).

In a bash file, `#` marks a bash command and `##` marks a comment.

Every line with #sbatch means you are specifying an attribute related to the job. Typical requests include
* `--nodes` the number of nodes requested (commented out in the example because we are not using parallel code)
* `--time=days-hours:min:sec` the length of time requested: all parameters are a number, hours must be less than 24, min and sec less than 6
* `--job-name` your reference name for the job
* `--mem` requested memory allocation
* `--gres` for setting GPU options (commented out in the example file)
* `--output=Output.%j.out` the name for output files (containing the progress output typically displayed in the Terminal when a job is running, here instead saved to a file you can view later). In this example this is set to "Output.jobnumber"
* `-p` or `--partition` the partition you want to work on (short=general) *NOTE: Only use one of these flags, "partition" or "p"*

When you are planning a job, we recommend that you request more time than you need (i.e. plan a job that takes 3 days to run and request the maximum time (5 days) on the long partition to run it). This gives you built in time to fix the simulation if anything goes wrong. Just remember to end your job when it's finished so you free up the resources for other users!

At one point there was an issue with Discovery where you had to specify the desired CPU architecture for your job using `--constraint`, but this has been fixed and choosing a specific architecture is now optional

After all of the #sbatch commands have been set, enter the commands you want the job to run on Discovery. Typically this will be
* load any required software modules
* source into your virtual environment
* run your simulation

For regular HOOMD-blue simulations the only module you will need to load is python (i.e. python/3.8.1).

**NOTE: It is recommended that you specify the exact path of the installation of python in your virtual environment, just to be absolutely sure Discovery does not default to the installation on the shared drive when running your simulation.**

Once you have completed your exec.bash script, you can run it with `sbatch`:
```bash
sbatch exec.bash
```
<br>

## Monitoring a Running Job

You can use squeue to view your current jobs, displaying the job number, partition it is running on, job name, the user running the job, the status (running/pending, etc.), the time the job has been running, the number of nodes being used, and a list of the specific node IDs
```bash
[your_username@login-00 ~ ]$ squeue -u your_username
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
```






