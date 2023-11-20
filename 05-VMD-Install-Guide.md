## VMD Installation Guide

This is a guide for installing the Visual Molecular Dynamics ([VMD]) software, and associated plugins, on your local computer for use with HOOMD-blue simulation data in the PRO-CF Research Group.

This guide is for optimized for macOS. 

[Last Update: August 2022]

[VMD]: https://www.ks.uiuc.edu/Research/vmd/

## Contents
1. [Prerequisites](/05-VMD-Install-Guide.md#prerequisites)
2. [Acquiring VMD](/05-VMD-Install-Guide.md#acquiring-vmd)
3. [Installing VMD](/05-VMD-Install-Guide.md#installing-vmd)
4. [The VMD Interface](/05-VMD-Install-Guide.md#the-vmd-interface)
5. [Prepare VMD for Manually Installing Plugins](/05-VMD-Install-Guide.md#prepare-vmd-for-manually-installing-plugins)
6. [Acquiring the GSD Plugin](/05-VMD-Install-Guide.md#acquiring-the-gsd-plugin)
7. [Installing the GSD Plugin](/05-VMD-Install-Guide.md#installing-the-gsd-plugin)
8. [Adding the GSD Plugin to the Original VMD Application](/05-VMD-Install-Guide.md#adding-the-gsd-plugin-to-the-original-vmd-application)
9. [Opening GSD Files with VMD](/05-VMD-Install-Guide.md#opening-gsd-files-with-vmd)
11. [Opening VMD from the Command Line](05-VMD-Install-Guide.md#opening-vmd-from-the-command-line)
10. [Installing the VMD Movie Plugin Requirements](05-VMD-Install-Guide.md#installing-the-vmd-movie-plugin-requirements)
12. [Next Steps](/05-VMD-Install-Guide.md#next-steps)
<br>

## Prerequisites

You should install VMD on your **local computer**, not on Discovery.

Required for installation:
* macOS or Linux (this guide is optimized for macOS)
* HOOMD-blue (see the [HOOMD-blue Installation and Setup Guide](/03-HOOMDblue-Install-Guide.md))
* A completed simulation (see [Simulating waterDPD](/04-Simulating-waterDPD.md))
<br>

## Acquiring VMD

You should install VMD on your **local computer**, not on Discovery.

VMD is freely available for download with a registered account.

Go to the [VMD website](https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD) and select the latest version appropriate for your operating system.<br>
*Note: There are two different macOS versions, "ARM64" for computers with Apple silicon (i.e. the M1 chip) and "x86_84" for computers with Intel processors.*

You will be prompted to create a username and password to register with VMD. Register for 1 user.

Select and download the version appropriate for your operating system. For macOS versions this will download a DMG file to your Downloads folder e.g. 
* for Intel: `vmd194a51-macx86_64.dmg`
* for ARM: `vmd194a57-arm64-Rev12.dmg`
<br>
<br>
## Installing VMD

Open the DMG file. This will mount the DMG file as a virtual disk and open a new window with a VMD application (called something like `VMD 1.9.4a51-x86_64-Rev9` for Intel Macs or `VMD 1.9.4a57-arm64-Rev12` for ARM Macs) and a PDF of the VMD User's Guide.

Open a new Finder window and go to Applications. In Applications, make a new folder called "VMD"<br>
*Note: In order to manually add a plugin to VMD, which we will do later, you must use this filename or the default filepath will be incorrect. This installation does not currently work for alternate filepaths.*

Copy and paste the VMD file and the user's guide from the DMG window into the Applications/VMD folder.

You can now close the DMG window and eject the virtual disk.

In the Applications/VMD folder, ctrl+click on the VMD file (hold down the `control` key and then click on the file) and select "Open" from the menu. This will open VMD with command overrides, so that you can run the program even though it was not installed through the Apple App Store. **You will get an error saying the software is not from a known provider** and the software will not open. Click Cancel.

Open System Preferences from either the Launchpad, the Applications folder, or the Dock. Go to "Security and Privacy" 

At the bottom of the Security and Privacy window you will see a message that VMD was prevented from opening. Click the "Open Anyway" button<br>
*Note: You may need to click the padlock at the bottom left of the screen and enter your username and password when prompted to unlock these settings before you can save these changes*

Clicking the "Open Anyway" button should immediately open VMD. VMD is now installed and authorized by your computer to open! And you should no longer need to ctrl-click to open VMD, you can open the application normally.
<br>
<br>
## The VMD Interface

VMD opens as 3 separate windows: a Terminal that launches the program with a `startup.command`, the OpenGL Display for viewing visualizations, and the control window called VMD Main. 

Keep the Terminal window open but ignore it, you should not need to interact with it while using VMD.

For now, quit VMD by going to the VMD Main window, selecting File, and then Quit. When prompted whether or not to Really Quit, click Yes. The OpenGL Display and VMD Main windows will both close and the `startup.command` Terminal window will display `[Process completed]` but remain open. You can now close this Terminal window.

*Note: You will probably get an error message from your compuer the first time you quit VMD (and occasionally other times after that) saying that VMD quit unexpectedly. This has to do with how VMD is opened and closed by the `startup.command` and is not a problem with VMD, but a slight incompatibility with how macOS expects programs to work. You don't need to worry about it. Hit Ignore.*
<br>
<br>
## Prepare VMD for Manually Installing Plugins

We will be using VMD to open GSD files; however, GSD is a not one of the filetypes that VMD natively supports. We will need to manually install a plugin to allow VMD to open GSD files, and in order to do that we need to access the Contents inside the VMD application.

*Note: This step is unique to macOS. Unfortunately, the plugin configuration process for manual installation is optimized for Linux, and cannot read the filepath to the VMD application's Contents on macOS without the following modifications. If you are using Linux you should not need to do this.*

In a Finder window, go to Applications/VMD

Right-click (or two-finger click) on the VMD application and select "Show Package Contents" from the menu. This will open a new Finder window for the VMD application, revealing a single folder called "Contents"

Copy the Contents folder. Go back to the Applications/VMD folder, and paste the duplicate Contents folder alongside the VMD aplication and the user's guide.
<br>
<br>
## Acquiring the GSD Plugin

To acquire the GSD plugin, go to the [gsd-vmd Github page](https://github.com/mphowardlab/gsd-vmd), click the bright green "Code" button, and select "Download ZIP"

Open your Downloads folder in Finder and unzip the file. Leave it in the Downloads folder.
<br>
<br>
## Installing the GSD Plugin

The Contents folder contains a directory called "vmd" where we will configure the gsd-vmd plugin for installation.

Open a new Terminal window and move to the /Contents/vmd directory
*Note: There are at least two Applications folders on your computer, one in your home directory and one in your root directory. You do NOT want the Applications folder in your home directory (*`~/Applications/`*), you want the Applications folder in your root directory (*`/Applications/`, *where most applications are installed).*
```bash
cd /Applications/VMD/Contents/vmd
```
Copy the downloaded `gsd-vmd-main` folder to this directory with
```bash
cp -r ~/Downloads/gsd-vmd-main .
```
Move to the new folder
```bash
cd gsd-vdm-main
```
Make a build directory and move to it
```bash
mkdir build && cd build
```
Run cmake to configure the plugin
```bash
cmake ..
```
And then install the plugin
```bash
make install
```
<br>
You can now run VMD (with the GSD plugin installed) from the duplicate Contents folder. To open this version of VMD, select the Unix executable file lovated in the Applications/VMD/Contents/vmd/ folder:
* for Intel: vmd_MACOSXX86_64
* for ARM: vmd_MACOSXARM64

This is functional, but not ideal.
<br>
<br>
## Adding the GSD Plugin to the Original VMD Application

You now have two versions of VMD
1. The original download, without the GSD plugin
2. A copy with the GSD plugin installed, which requires navigating to a Unix executable file to open

If you want to open VMD from an application icon, rather than the Unix executable file, you can copy the new, configured GSD plugin to the original version of VMD.

For Intel Macs:<br>
Open a new Terminal window and move to the VMD application molfile directory (where plugins are stored)
```bash
cd /Applications/VMD/VMD\ 1.9.4a51-x86_64-Rev9.app/Contents/vmd/plugins/MACOSXX86_64/molfile/  
```
Copy the GSD plugin from where it was installed in the duplicate Contents folderto this molfile directory (where you are currently located)
```bash
cp /Applications/VMD/Contents/vmd/plugins/MACOSXX86_64/molfile/gsdplugin.so .
```

For ARM Macs:<br>
Open a new Terminal window and move to the VMD application molfile directory (where plugins are stored)
```bash
cd /Applications/VMD/VMD\ 1.9.4a57-arm64-Rev12.app/Contents/vmd/plugins/MACOSXARM64/molfile/  
```
Copy the GSD plugin from where it was installed in the duplicate Contents folderto this molfile directory (where you are currently located)
```bash
cp /Applications/VMD/Contents/vmd/plugins/MACOSXARM64/molfile/gsdplugin.so .
```


Your should now be able to open GSD files with the original VMD application! You can open the VMD application from the Applications/VMD folder or from Launchpad.<br>
***NOTE: Unfortunately you cannot keep VMD in the Dock.*** *Right-clicking on the icon and selecting "Keep in Dock" will work once, but after you close VMD the path will break and direct to the VMD icon file, not the VMD application. Bummer.*

Before you delete the duplicate Contents folder, the gsd-vmd-main folder in your Downloads, and the gsd-vmd-main.zip file you should test to make sure that you can open GSD files with VMD.
<br>
<br>
## Opening GSD Files with VMD

If you have not already done so, run the waterDPD.py example simulation (see [Simulating waterDPD](/04-Simulating-waterDPD.md) for details).

Open VMD by selecting the icon in Launchpad or the VMD application in the Applications/VMD folder.

Go to VMD Main
* Choose "File"
* Choose "New Molecule"
* Click "Browse" next to "Filename" and navigate to the location of your GSD file<br>
(e.g. repositories/waterDPD-sims/waterDPD/Equilibrium.gsd)
* The "Determine file type" setting should autofill with "HOOMD-blue GSD File"
* Click "Load"

The GSD file should now open! 

You can close the Molecule File Browser and select the OpenGL Display window to view the default visualization setting (which displays "bonds" between your particles).
<br>
<br>
## Opening VMD from the Command Line

So, everything now works great, but there are 2 problems:
1. You can't keep VMD in the Dock
2. You may have noticed that VMD always opens in the home directory, so you will always have to navigate from there to your files before you can open them.

The best way to solve these problems is to open VMD from the Command Line (i.e. the Terminal) instead.

The easiest way to do this is to add an "alias" to the configuration file for your Terminal shell (on macOS this is the `.zshrc` file, as opposed to the `.bashrc` file).

Check to see if you have a .zhsrc file (this will also create a new one if you do not already have it)
```
cd ~ && vim .zshrc
```
**For Intel** Copy and paste the following lines at the end of your .zshrc file
```
# add alias for VMD
alias vmd='csh /Applications/VMD/VMD\ 1.9.4a51-x86_64-Rev9.app/Contents/MacOS/startup.command.csh'
```
**For ARM** Copy and paste the following lines at the end of your .zshrc file
```
# add alias for VMD
alias vmd='csh /Applications/VMD/VMD\ 1.9.4a57-arm64-Rev12.app/Contents/MacOS/startup.command.csh'
```

Restart your Terminal session (or open a new window) and you should now be able to open VMD using the command `vmd`

You can now cd into any directory you like and open VMD with that location as the workin directory!

You can also open a gsd file in VMD from the Terminal with
```
vmd filename.gsd
```
<br>

## Installing the VMD Movie Plugin Requirements

As a final step, you should also install the VMD Movie Plugin software requirements so that you have the full set of movie options when saving visualizations.

The list of requirements for different operating systems is available on the VMD website [here](http://www.ks.uiuc.edu/Research/vmd/plugins/vmdmovie/). 

For macOS you can use the Homebrew package manager to install the required software:

The NetPBM toolkit
```bash
brew install netpbm
```
And ImageMagick (required to create animated GIFs)
```bash
brew install imagemagick
```
The VMD website also suggests that you may need to update the POV-Ray 3.6 configuration file, but that is not usually necessary for us.
<br>
<br>
## Next Steps

See the guide to [Using VMD](/06-Using-VMD.md) for an overview of visualization options. 

