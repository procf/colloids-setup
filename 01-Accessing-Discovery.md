# Getting Setup with the Discovery Cluster

Discovery is a High-Performance Computing (HPC) cluster managed by the Research Computing section at Northeastern. The most up-to-date information about Discovery is available on the [Research Computing Docs](https://rc-docs.northeastern.edu/en/latest/welcome/welcome.html), and you can always email them with any questions at rchelp@northeastern.edu

This is a guide to getting setup to use the Discovery Cluster at Northeastern University for research in the PRO-CF Group.

This guide is optimized for macOS.

[Last Update: November 2023]

This guide was compiled by Rob Campbell.

## Contents
1. [Getting Access](/01-Accessing-Discovery.md#getting-access)
2. [Connecting to Discovery](/01-Accessing-Discovery.md#connecting-to-discovery)
3. [X11 and Visual Interfaces](/01-Accessing-Discovery.md#x11-and-visual-interdaces)
4. [Learning How to Use Discovery](/01-Accessing-Discovery.md#learning-how-to-use-discovery)
5. [Getting Access to the work Directory](/01-Accessing-Discovery.md#getting-access-to-the-work-directory)
6. [Requesting Access to Additonal Partitions](/01-Accessing-Discovery.md#requesting-access-to-additonal-partitions)
7. [Copying files to and from Discovery](/01-Accessing-Discovery.md#copying-files-to-and-from-discovery)
8. [Loading Existing Software](/01-Accessing-Discovery.md#loading-existing-software)
9. [Creating Virtual Environments](/01-Accessing-Discovery.md#creating-virtual-environments)
10. [Github on Discovery](/01-Accessing-Discovery.md#github-on-discovery)
11. [Next Steps](/01-Accessing-Discovery.md#next-steps)
<br>

## Getting Access

To request access to the Discovery cluster, go to the [Getting Access page](https://rc-docs.northeastern.edu/en/latest/gettingstarted/get_access.html) on the RC-docs and follow the link to complete the [ServiceNow RC Access Request form](https://service.northeastern.edu/tech?id=sc_cat_item&sys_id=0ae24596db535fc075892f17d496199c). We do not need the software Gaussian.
<br>
<br>
## Connecting to Discovery

Once you have been granted access to Discovery you will need to login remotely to the cluster to view files and run jobs.

Most of us use the macOS Terminal shell to access Discovery from the command line. You can also access Discovery from the command line on Windows and Linux, or you can access Discovery online in a virtual terminal environment called Open OnDemand (OOD) ([more information about OOD is available on the RC-docs](https://rc-docs.northeastern.edu/en/latest/using-ood/index.html))

Your account should come with both a home folder (named after your Northeastern username: `your_username`) and a `scratch` folder (`/scratch/your_username`).

To login to your Discovery home folder from the Terminal shell, use the command
```bash
ssh your_username@login.discovery.neu.edu
```
And enter your Northeastern username and password.

You can then move to the `scratch` folder with
```bash
cd /scratch/your_username
```
or log out with the `logout` command
```bash
logout
```
To learn more about connecting to Discovery, see [Connecting to Cluster](https://rc-docs.northeastern.edu/en/latest/gettingstarted/connectingtocluster/index.html) in the RC-docs.

You can also streamline your log-in process by setting up [Passwordless SSH](https://rc-docs.northeastern.edu/en/latest/first_steps/passwordlessssh.html) login.
<br>
<br>
## X11 and Visual Interfaces

At some point you will probably want to use applications with a visual interface on Discovery (i.e. using X11 and GUI interfaces), for example: viewing Python plots directly on Discovery (without having to save and download a file to your local computer).

Setting up X11 requires 3 additional steps:

1. Set up [Passwordless SSH](https://rc-docs.northeastern.edu/en/latest/first_steps/passwordlessssh.html) 
2. (macOS only) Install XQuartz (available on the [XQuartz website](https://www.xquartz.org/)) and run it in the background (*Do NOT use the Terminal application within XQuartz to sign in to Discovery, use the default Terminal that comes with your Mac*)
3. log into Discovery using the "-Y" flag
```bash
ssh -Y your_username@login.discovery.neu.edu
```
You can test if this worked with the command `xeyes` which will make a pair of eyes appear in the corner of your screen that follow your cursors movement.
<br>
<br>
## Learning How to Use Discovery

The Research Computing (RC) team at Northeastern is the best resource for learning about Discovery. You can read more on the [RC-docs](https://rc-docs.northeastern.edu/en/latest/welcome/welcome.html) or email them at rchelp@northeastern.edu

The RC team has recorded several training sessions. You can access them on the [RC-docs](https://rc-docs.northeastern.edu/en/latest/tutorialsandtraining/index.html) or by going to the [Training page](https://rc.northeastern.edu/support/training/).

You can also schedule an "office hours" style meeting for 1-on-1 help from a Research Computing staff member at the RC [Consulting page](https://rc.northeastern.edu/support/consulting/).
<br>
<br>
## Getting Access to the `work` Directory

The `home` and `scratch` directories are available to all students; however, `home` has very limited storage space and is NOT a good place to run your simulations, and files on `scratch` are deleted every month to free-up space.You can get started in your `scratch` folder, but for long-term research in the PRO-CF group you will want access to our `work` directory.

As a member of the PRO-CF Group you should automatically be given access to the `props` directory on `work` ("PROPS" is our old acronym). This is where you will store most of your data.

After connecting to Discovery, you can check this with
```bash
cd /work/props
```

**If you do not automatically have permission to access this directory, email RC Help to request access.**

After you get access to `/work/props` you can create your own folder for your projects
```bash
cd /work/props
mkdir yourname
```
<br>

## Requesting Access to Additonal Partitions

You automatically have access to the essential partitions for running small jobs on Discovery; however, you will likely need access to additional partitions, such as `long` or `large`, during the course of your research.

Discuss with Safa and other current students about whether or not you need access to these partitions. You can read more about what is available and find the Partition Access Request From on the [Paritions page](https://rc-docs.northeastern.edu/en/latest/hardware/partitions.html) of the RC-docs.
<br>
<br>
## Copying files to and from Discovery

There are several ways that you can copy files to and from Discovery. The main 2 methods you can get started with are:

1. You can transfer small files from your computer to Discovery using the Terminal with the `scp` command and Discovery's dedicated transfer node (`xfer`). You cannot transfer data from the `login` node or any other node except `xfer`.

For example, to transfer a file to your `/scratch` space, use the command:
```bash
scp filename your_username@xfer.discovery.neu.edu:/scratch/your_username/
```
and to transfer a file from `/scratch` to your computer, use the command:
```bash
scp your_username@xfer.discovery.neu.edu:/scratch/your_username/filename .
```

2. If you prefer a traditional file-folder interface, you can use the software [Filezilla](https://filezilla-project.org/) or the OOD File Explorer.

More details on these and other file transfer methods is available in the [Data Management](https://rc-docs.northeastern.edu/en/latest/datamanagement/index.html) section of the RC-docs.
<br>
<br>
## Loading Existing Software

You have your account, you have your `work/props/` folder to store files, you can transfer data back and forth from your local computer ...what about software?

You can install your own software on Discovery, but most software you need should already be available as a loadable module from the `shared` drive.

Check your currently loaded software with `module list`
```bash
[yourusername@login-01 ~]$ module list
  1) discovery/2021-10-6
```
(You should ALWAYS see the module needed to interact with discovery loaded on your login node)

You can also view all available modules [**NOTE**: this is a very long list]
```bash
module avail
```
Load a specific module
```bash
module load python/3.8.1
```
And unload a module
```bash
module unload python/3.8.1
```
More information about modules is available in the [Software](https://rc-docs.northeastern.edu/en/latest/software/index.html) section of the RC-docs.
<br>
<br>
## Creating Virtual Environments

When you need to install software that is not available as a module (like our custom version of HOOMD-blue), it is good practice to install it as a virtual environment. Since HOOMD-blue's interface uses Python, we will create a virtual Python environment when installing HOOMD-blue.

More details on this process will be covered later. For now all you need to know is that in additionl to loading modules, you will also want to source into a specific virtual environment when running simulations. This gives you more control over your "development environment" -- i.e. the version of Python your using, the packages you have installed (e.g. NumPy, SciPy), etc.
<br>
<br>
## Git and Github on Discovery

You already have created a Github account to access this guide. Git is a version management tool, especially useful for tracking changes you make to the HOOMD-blue sourcecode and for collaborating with others.

If you need help using Github setting up command-line Git, you can check out the separate [Github Guide](https://github.com/procf/getting-started/blob/main/github-guide.md) in the PRO-CF getting-started repository.

The steps for using Git on Discovery are the same as setting up git on your computer, but **since Discovery runs Linux, you will need to use the Linux commands to link to GitHub.**

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
## Next Steps

Once you have access to Discovery and are familiar with the basics you can begin setting up HOOMD-blue and running simulations. See the [introduction to HPC simulations](/02-Slurm-and-Disco.md) for more information.

