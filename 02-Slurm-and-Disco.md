# Running Simulations on Discovery

This is a guide to the basics of running simulations on Discovery, Northeastern University's HPC cluster. 

This guide is optimized for macOS. See the [Guide to Accessing Discovery](/01-Accessing-Discovery.md) first.

[Last Update: August 2023]

This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Running Jobs on Discovery](/02-Slurm-and-Disco.md#running-jobs-on-discovery)
	* [srun](/02-Slurm-and-Disco.md#srun) (for interactive jobs)
	* [sbatch](/02-Slurm-and-Disco.md#sbatch) (for running jobs in the background)
2. [Monitoring a Job and Job Stats](/02-Slurm-and-Disco.md#monitoring-jobs-and-job-stats)
3. [Next Steps](/02-Slurm-and-Disco.md#next-steps)
<br>

## Running Jobs on Discovery

When you sign into Discovery you are on the "login node" but you should **ALWAYS** run your jobs on a "compute node" using either srun (for interactive jobs) or sbatch (for scheduling jobs to run in the background).

The "s" in srun and sbatch stands for the [Slurm Workload Manager](https://slurm.schedmd.com/documentation.html), which is what most HPC clusters use to manage all the different "jobs" users are running. More information about [Slurm is available in the [RC-docs Slurm section](https://rc-docs.northeastern.edu/en/latest/slurmguide/index.html) and in this repository's [Programming Resources](/Programming-Resources#slurm).

Slurm controls:
* your access to partitions
* your access to compute nodes on those partitions
* the amount of time you can run scripts before getting kicked-off 

### srun

srun lets you remotely login to a computer node and then work normally -- loading software, running scripts, waiting for them to finish, and then viewing results.

There are many options you can choose when use srun, but the simplest way is to move to the first available compute node (with no restrictions on what type of node that is), using the command: 
```bash
srun --pty /bin/bash
```
OR, if you have X11 enabled for graphical interfaces, be sure to carry that over with
```bash
srun --pty --x11 /bin/bash
```

You will then be transfered to a compute node and can use other commands normally.
<br>

### sbatch

sbatch lets you run a job in the background and go do something else. To do this, you need to write a small bash script that: chooses the type of compute node you want to access, runs your files, and saves a log of any errors and output. 

You can submit an sbatch job from both the login node or an srun session. In both cases a brand-new, separate job is created with the sbatch settings. This also means you can run many sbatch jobs at the same time (although some partitions do have limits).

The sbatch script is a bash file. Bash files that are *executable* like an sbatch script (i.e. you use them to run other programs), typically are NOT given an extension as part of their name. They are called "script-name" NOT "script-name.bash"

Here is a sample sbatch file for running an MPI simulation with HOOMD-blue:
```bash
#!/bin/bash
#SBATCH -J sim
#SBATCH -n 27 -N 1
#SBATCH -t 24:00:00
#SBATCH -p short
#SBATCH --constraint=ib
##SBATCH --mem=128Gb
##SBATCH --gres
#SBATCH -o %A.out
#SBATCH -e %A.err

# load required modules and virtual environments
module load python/3.8.1
source hoomdmod4.2.1-venv/bin/activate
module load gcc/11.1.0
module load openmpi/4.1.2-gcc11.1

# run the simulation
mpirun -n 27 python3 sim-gel-DPD.py
```

Our bash files typically have 3 sections:

1. A bash script always starts with `#!/bin/bash`

2. Every line that starts with `#SBATCH` or `#sbatch` specifies a setting for the job we are running with Slurm (**NOTE**: in this section you need to use`##` for a comment). Typically this section includes:
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

*When you are planning an sbatch job, it's recommended that you request more time than you need (i.e. plan a job that takes 12 hours to run and request the maximum 24 hours on the short partition to run it). Some nodes run slower than others, and if your job finishes early the node will be made available for other users. 

*As mentioned above, if you are running MPI simulations, it's also recommended that you only use the newest compute nodes, which use Infiniband for faster communication between nodes (turn this on with the "--constraint=ib" flag).*

3. After all of the sbatch commands have been set, enter the commands you want the job to run on Discovery. Typically this will be
	* load Python, source into your virtual environment, and load additional required modules
	* run your simulation
<br>
<br>
<br>
## Monitoring Jobs and Job Stats

You can use squeue to view a list of your current jobs: the job number, partition it is running on, job name, the user running the job, the status (running/pending, etc.), how long the job has been running, the number of nodes being used, and a list of the specific node IDs
```bash
[your_username@login-00 ~ ]$ squeue -u your_username
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
```

This will show any active srun and sbatch jobs.

Once a job is complete you can view how long it ran (as well as other stats) with the command
```bash
seff [jobID]
```

Because of how we wrote the sbatch script, for sbatch jobs the jobID is the name of the .err and .out files.
<br>
<br>
## Next Steps 

You now know all about how Discovery works! You'll get a lot of hands-on practice with Discovery over the rest of this guide.

The next step is to [Install HOOMD-blue](03-HOOMDblue-Install-Guide.md) on Discovery and/or your local computer.



