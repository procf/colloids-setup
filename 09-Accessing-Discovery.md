# Getting Setup with the Discovery Cluster

This is a guide to getting setup to use the Discovery Cluster at Northeastern University for research in the PRO-CF Group.

This guide is optimized for macOS.

[Last Update: July 2022]

This guide was compiled by Rob Campbell.

## Contents
1. [Getting Access](/09-Accessing-Discovery.md#getting-access)
2. [Connecting to Discovery](/09-Accessing-Discovery.md#connecting-to-discovery)
3. [Learning How to Use Discovery](/09-Accessing-Discovery.md#learning-how-to-use-discovery)
4. [Getting Access to the `work` Directory](/09-Accessing-Discovery.md#getting-access-to-the-work-directory)
5. [Requesting Access to Additonal Partitions](/09-Accessing-Discovery.md#requesting-access-to-additonal-partitions)
6. [Copying files to Discovery](/09-Accessing-Discovery.md#copying-files-to-discovery)
7. [Loading Existing Software](/09-Accessing-Discovery.md#loading-existing-software)
8. [Next Steps](/09-Accessing-Discovery.md#next-steps)
<br>

## Getting Access

To request access to the Discovery cluster, complete the [ServiceNow Research Computing Access Request form](https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0ae24596db535fc075892f17d496199c). We do not need the software Gaussian.

More details on getting access and using Discovery are available in [the Discovery documentation](https://rc-docs.northeastern.edu/en/latest/get_started/get_access.html).
<br>
<br>
## Connecting to Discovery

Once you have been granted access to Discovery you should have both a home folder (named after your Northeastern username: `your_username`) and a `scratch` folder (`/scratch/your_username`) that you can access on the cluster.

You can login to your Discovery home folder from your Terminal shell with the command
```bash
ssh your_username@login.discovery.neu.edu
```
And by entering your Northeastern username and password.

You can then move to the `scratch` folder with
```bash
cd /scratch/your_username
```
or log back out with the `logout` command
```bash
logout
```

<br>
**NOTE**: If you would like to be able to use applications with a visual interface (i.e. X11 and GUI interfaces), including MATLAB or simply viewing Python plots directly from Discovery, then you need to do 4 things:
1. Set up passwordless SSH access to Discovery as described on the [Discovery docs](https://rc-docs.northeastern.edu/en/latest/first_steps/connect_mac.html#passwordless-ssh) 
2. (macOS only) Install XQuartz (available on the [XQuartz website](https://www.xquartz.org/)) and run it in the background (*Do NOT use the Terminal application within XQuartz to sign in to Discovery, use the default Terminal that comes with your Mac*)
3. (macOS only) After you open XQuartz and before logging into Discovery, enter this command in the Terminal window
```bash
defaults write org.macosforge.xquartz.X11 enable_iglx -bool true
```
*You must do this step every time you close and restart XQuartz*

4. log into Discovery using the "-Y" flag
```bash
ssh -Y your_username@login.discovery.neu.edu
```
You can test if this worked with the command `xeyes` which will make a pair of eyes appear in the corner of your screen that follow your cursors movement.

To learn more about connecting to Discovery, see [Connecting to Discovery](https://rc-docs.northeastern.edu/en/latest/get_started/connect.html#mac) in the Discovery docs.
<br>
<br>
## Learning How to Use Discovery

To get started understanding the Discover cluster you should watch the introductory training video on [Northeastern's LinkedIn Learning page](https://www.linkedin.com/checkpoint/enterprise/login/74653650?pathWildcard=74653650&application=learning&redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Flearning%2Fcontent%2F1139340%3Fu%3D74653650).

You can also sign up for [training sessions](https://rc.northeastern.edu/support/training/) on introductory and advanced topics.

And you can schedule an "office hours" style meeting for 1-on-1 help from a Research Computing staff member at the RC [Consulting page](https://rc.northeastern.edu/support/consulting/).
<br>
<br>
## Getting Access to the `work` Directory

As a member of the PRO-CF Group you should have access to the `props` directory on `work` ("PROPS" is our old acronym). This is where you will store most of your data.

After connecting to Discovery, you can check this with
```bash
cd /work/props
```

If you do not have permission to access this directory contact RC Help.

After you get access to `/work/props` you can create your own folder for your projects
```bash
cd /work/props
mkdir yourname
```
<br>

## Requesting Access to Additonal Partitions

You automatically have access to the essential partitions for running small jobs on Discovery; however, you will likely need access to additional partitions, such as `long` or `large`, during the course of your research.

Discuss with Safa and other current students about whether or not you need access to these partitions. If you do, you can request access using the [Partition Access Request Form](https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0c34d402db0b0010a37cd206ca9619b7).
<br>
<br>
## Copying files to Discovery

There are several ways that you can copy files to and from Discovery:

The method used in most Discovery Trainings is the web-based interface [Discovery Open on Demand (OOD)](https://ood.discovery.neu.edu/pun/sys/dashboard).

You can also transfer small files from your computer to Discovery on the terminal with the `scp` command and Discovery's dedicated transfer node (`xfer`). You cannot transfer data from the `login` node or any other node except `xfer`.

For example, to transfer a file to your `/scratch` space, use the command:
```bash
scp filename your_username@xfer.discovery.neu.edu:/scratch/your_username/
```
and to transfer a file from `/scratch` to your computer, use the command:
```bash
scp your_username@xfer.discovery.neu.edu:/scratch/your_username/filename .
```
The Discovery documentation includes more details about [transfering files](https://rc-docs.northeastern.edu/en/latest/using-discovery/transferringdata.html), including options for SSHFS.

The *recommended* method for transfering files (especially large data files) is with Globus, a web-based file transfer interface. You can learn more about how to set up a Globus account, including options Globus' command line tools on the [Using Globus](https://rc-docs.northeastern.edu/en/latest/using-discovery/globus.html#using-globus) page in the Discovery documentation.
<br>
<br>
## Loading Existing Software

Discovery has a large catalog of software available for use on the `shared` drive. In addition to installing your own software onto Discovery, you can load existing modules to use common software packages.

Check your currently loaded software with `module list`
```bash
[yourusername@login-01 ~]$ module list
  1) discovery/2021-10-6
```
(You should ALWAYS see the module needed to interact with discovery loaded on your login node)

You can also view all available modules
```bash
module avail
```
Load a specific module
```bash
module load module-name
```
And unload a module
```bash
module unload module-name
```
More information about modules is available in the [Discovery documentation](https://rc-docs.northeastern.edu/en/latest/software/modules.html).
<br>
<br>
## Next Steps

Once you have access to Discovery and are familiar with the basics you can begin running simulations on Discovery. See the [introduction to HPC simulations](/10-Slurm-and-Disco.md) for more information.

