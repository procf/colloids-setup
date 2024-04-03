# MacOS System Setup Recommendations and Tips

This is a guide to setting up a new MacOS computer for command line programming, specifically what to do before installing and using HOOMD-blue for colloids simulations in the PRO-CF Research Group. If you are new to MacOS, or new to programming on MacOS, then this guide can help you get started.

[Last Update: June 2022]

This guide was complied by Rob Campbell.
<br>

## Contents
1. [Terminal for Command Line Programming in MacOS](/System-Setup/02-macOS-Setup.md#terminal-for-command-line-programming-in-macos)
2. [Xcode](/System-Setup/02-macOS-Setup.md#xcode)
3. [Package Managers](/System-Setup/02-macOS-Setup.md#package-managers)
4. [Text Editors](/System-Setup/02-macOS-Setup.md#text-editors)
5. [Cmake](/System-Setup/02-macOS-Setup.md#cmake)
6. [Python 3](/System-Setup/02-macOS-Setup.md#python-3)
7. [IDEs](/System-Setup/02-macOS-Setup.md#ides)
8. [Git and Github](/System-Setup/02-macOS-Setup.md#git-and-github)
9. [Jupyter Lab](/System-Setup/02-macOS-Setup.md#jupyter-lab)
<br>

## Terminal for Command Line Programming in MacOS

MacOS uses the Terminal application for command line programming. The Terminal app is located in the Utilities folder, and can be accessed by opening Finder and selecting Applications from the Favorites sidebar

>Applications/Utilities/Terminal

or via Launchpad in the Other folder

>Launchpad/Other/Terminal

Once you have opened the Terminal application you can pin a shortcut for opening it to the Dock at the bottom of your screen. 

After you open Terminal, right click the Terminal icon in the Dock at the bottom of your screen, scroll up to "Options," and select "Keep in Dock."

By default, Terminal opens in your home directory (where "your_username" is the name of your account on your computer)
```bash
/Users/your_username
```
This is where you will want to install most packages and create most files and folders/directories/repositories.

In older versions of MacOS the default Terminal window used the bash shell (the same as Linux and most HPC clusters); however, more recent versions of MacOS use the zsh shell (seemingly due to licensing). Both bash and zsh exist on MacOS, but Apple strongly recommends switching to zsh. Many online resources for command line programming on MacOS still reference bash, so keep in mind which shell you are using when troubleshooting.

Using zsh is very similar to using bash. The main difference you will notice at first is the symbol at the end of the prompt

Bash uses $
```bash
$
```
and zsh uses %
```bash
%
```

Another important difference is which file you use to modify the prompt. If you want to make any changes to settings in the Terminal prompt you will need to modify the `~/.bash_profile` in bash and the `~/.zshrc` file in zsh.
<br>
<br>
## Xcode

Now that you are familiar with the Terminal, the first thing you need to do is install Xcode. Xcode includes several essential pieces of software for programming in MacOS.

Open a Terminal window and enter
```bash
xcode-select --install 
```
<br>

## Package Managers

You will also need to install a package manager, such as [Homebrew](https://brew.sh/). You can install Homebrew with
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
This calls a script (from the Homebrew [website](https://brew.sh/)) that explains what it will do and then pauses before installing Homebrew.

Some simple Homebrew commands are:

Update Homebrew
```bash
brew update
```
Install software/packages
```bash
brew install package-name
```
And update installed software
```bash
brew upgrade package-name
```
<br>

## Text Editors

You will want to get comfortable with a command line text editor for quickly creating and editing files. MacOS includes [Nano](https://www.nano-editor.org/) and [Vi](http://ex-vi.sourceforge.net/)/[Vim](https://www.vim.org/). You can update these or install other text editors with Homebrew.

For Vim, open an existing file (or create a new one) with
```bash
vim filename
```

*Note about using Vim:*<br>
Vim is powerful, but difficult to get used to because of its unintuitive default interface and its many functions and shortcuts. The basics of Vim are: 
* Opening a file with `vim` does not allow you to immediately edit it. You must first enter "Instert" mode, by pressing `i`
* To stop editing a file, press `esc` to return to the default mode
* Back in the default "Normal" mode, you can search for something in your file using "/" (for example, to search for instances of the word "something" type "/something")
* The command `:q` will quit a file that has not been edited
* The command `:q!` will quit a file that has been edited WITHOUT saving changes
* The command `:wq` will save (write) and quit a file that has been edited

For more on using Vim, see the lectures in ["The Missing Semester of Your CS Education"](https://missing.csail.mit.edu/) and our other [Vim Programming Resources](/Programming-Resources#vim)
<br>
<br>
## Cmake

HOOMD-blue requires [cmake](https://cmake.org/), which you can go ahead and install or update now with Homebrew
```bash
brew install cmake
```
<br>

## Python 3

MacOS comes with Python 2 pre-installed, but you **DO NOT** want to use this Python. Not only do we want to use Python 3, rather than Python 2, but the pre-installed version of Python 2 is used by your computer internally, and so it's best not to mess with it. 

You can install Python 3 directly with a package manager like Homebrew
```bash
brew install python
```
This will also install pip, the Python package manager, which you can use to install NumPy and other required Python packages once we set up our virtual environments during the HOOMD-blue installation steps.

We use virual environments when running out simulations. Virtual environments give you more control over which packages you are using (e.g. NumPy, SciPy, etc.), by letting you create different development environments with different sets of packages installed. There are many ways to set up virtual Python environments (pyenv, venv, virtualenvwrapper, etc.), but HOOMD-blue recommends using venv, which comes installed with Python.

Another popular option is to use the package and environment manager [conda](https://docs.conda.io/en/latest/) via Miniconda (the basic installation) or Anaconda (a larger installation with 7500+ packages included). Conda is not required for using HOOMD-blue. If you are using conda, see the [conda website for installation steps](https://docs.conda.io/en/latest/).

Whichever installation method you choose, you will be able to check your current version of Python with 
```bash
python --version
```
and the location it is installed with
```
which python
```
You can run the current (default) version of Python with 
```bash
python
```
And you can specify running Python 3 with
```bash
python3
```
<br>

## IDEs

While you can write and edit scripts with a text editor, you will likely want to install an integrated development environment (IDE) for developing and debugging your code.

It is recommended that you download [Eclipse](https://www.eclipse.org/downloads/) for C++ programming.

You can also use Eclipse for developing Python code, but you may be better off with a dedicated Python IDE. For working on MacOS, our group mostly uses [VSCode](https://code.visualstudio.com/) 
<br>
<br>
## Git and Github

Git is a version management tool, especially useful for collaborating with others on shared code. If you're interested in using Github and need help setting up command-line Git, you can check out the separate [Github Guide](https://github.com/procf/getting-started/blob/main/github-guide.md) in the PRO-CF getting-started repository.
<br>
<br>
## Jupyter Lab

Another useful tool for sharing code is [Project Jupyter](https://jupyter.org/) (i.e. Juptyer Lab the updated interface for Jupyter Notebooks). A Jupyter Notebook allows you to write, view, edit, run, and see outputs from code using code-blocks in a web browser. You can also share your code with other users this way, and they can re-run the code to see how it works. Jupyter is a combination of the names of three programming languages: "[Julia](https://julialang.org/)", "[Python](https://www.python.org/)", and "[R](https://www.r-project.org/about.html)" (**Ju**-**Pyt**-e-**R**), which it was originally designed for. You can now use Jupyter for any of these three programming languages, as well as others.

You can learn more about Jupyter and try it online at their [website](https://jupyter.org/). You can then follow their instructions for installing Jupter Lab on your computer using the command line, as well as setting up the Kernels for the languages you are interested in.

Jupyter Notebooks are used extensively by the PRO-CF Machine Learning Team for developing and sharing their code, so if you're interested in learning more about what they do at some point you should definitely start getting familiar with Jupyter Notebooks!


