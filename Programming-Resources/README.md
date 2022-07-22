# Programming Resources

This is a collection of programming resources that can help you get started with the tools you need to do research in the PRO-CF Colloids Team.

Our simulations use a variety of tools and programming languages. All of us were new to at least some of these things when we started working in the PRO-CF Research Group, and we're still exploring new things that might make our research easier/better! This directory contains some general resources (either online or as PDFs) that have been useful for learning these skills.

[Last Update: June 2022]

This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Best Practices for Scientific Computing](/Programming-Resources#best-practices-for-scientific-computing)
1. [Best Practices for Collaborating on Code](/Programming-Resources#best-practices-for-collaborating-on-code)
2. [Foundational CS Skills](/Programming-Resources#foundational-cs-skills) (i.e. Command Line, VIM, Git, Markdown, and other general skills)
3. [Python](/Programming-Resources#python)
4. [R](/Programming-Resources#r)
5. [C/C++](/Programming-Resources#cc)
6. [Fortran](/Programming-Resources#fortran)
7. [Parallel Computing](/Programming-Resources#parallel-computing)
8. [HPC](/Programming-Resources#hpc)
<br>

## Best Practices for Scientific Computing

* [Good Enough Practices for Scientific Computing]<br>
2016 follow up to "Best Practices for Scientific Computing" as 6 best practices specifically geared towards people who are just getting started with scientific computing. 

* [Best Practices for Scientific Computing]<br>
2014 paper outlining 8 best practices for scientific computing.
<br>

## Best Practices for Collaborating on Code

* [Stealing Google's Coding Practices for Academia]<br>
A 2016 blogpost on the differences between academic code and production code, making an argument for best practices for collaborative programming in academic research: style guides, tooling, code review, pair programming, and open source.

* [Reproducible research: Goals, Guidelines and Git]<br>
Slides from a 2019 Princeton workshop with an overview of reproducible research best practices and a guide to setting up Git (geared towards bioinformatics, but still useful)

* [Making READMEs Readable]<br>
Best practices for open-source READMEs/documentation

[Good Enough Practices for Scientific Computing]: https://swcarpentry.github.io/good-enough-practices-in-scientific-computing/
[Best Practices for Scientific Computing]: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
[Stealing Google's Coding Practices for Academia]: https://da-data.blogspot.com/2016/04/stealing-googles-coding-practices-for.html?m=1
[Reproducible research: Goals, Guidelines and Git]: https://opr.princeton.edu/workshops/Downloads/2019May_RRandGitPratt.pdf
[Making READMEs Readable]: https://github.com/18F/open-source-guide/blob/18f-pages/pages/making-readmes-readable.md
<br>

## Foundational CS Skills
* [The Missing Semester of Your CS Education]<br>
Recorded lectures from MIT CSAIL's course on using the shell, VIM, Command Line, Git, etc.

[The Missing Semester of Your CS Education]: https://missing.csail.mit.edu/

### Command Line

* [Terminal Cheat Sheet](https://github.com/rob10campbell/PRoPS-colloids_setup/blob/main/Programming-Resources/terminal-basics-cheatsheet.pdf) (PDF)

### VIM

* [Graphical vi-vim Cheat Sheet and Tutorial]

[Graphical vi-vim Cheat Sheet and Tutorial]: http://www.viemu.com/a_vi_vim_graphical_cheat_sheet_tutorial.html

### Git

* The [Github Guide](https://github.com/procf/getting-started/blob/main/github-guide.md) in the PRO-CF getting-started reposirory

* [Git Cheat Sheet](/Programming-Resources/git-cheat-sheet_USletter.pdf) (PDF)

* [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)

* [Learn Git Branching](https://learngitbranching.js.org/)<br>
An interactive set of tutorials for learning Git.

* [Pro Git Book](https://git-scm.com/book/en/v2)<br>
Comprehensive free book for learning to use Git repositories.

* [Reproducible research: Goals, Guidelines and Git](https://opr.princeton.edu/workshops/Downloads/2019May_RRandGitPratt.pdf)<br>
Slides from a 2019 Princeton workshop with an overview of reproducible research best practices and a guide to setting up Git.

* [.gitignore Templates](https://github.com/github/gitignore)

* [Setting Up a Github Repository for Your Lab](https://ourcodingclub.github.io/tutorials/git-for-labs/#version)<br>
A guide for how to manage a research lab's Github organizational account. Aimed at ecology and evolutionary biology research, but includes many broadly applicable best practices.

* [Scientific Collaboration and Project Management in GitHub](https://rabernat.medium.com/scientific-collaboration-and-project-management-in-github-d74f2255ae5f)<br>
Blog post about Github for scientific research project management

* [Cookiecutter Science Project](https://github.com/jbusecke/cookiecutter-science-project)<br>
An example template for reproducible science projects (uses Conda)

### Markdown

* [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)

* [Getting Started with writing and formatting on Github](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github)

* [Complete list of github markdown emoji markup](https://gist.github.com/rxaviers/7360908)

<br>

## Python

* [Jupyter Notebooks and Jupyter Lab](https://jupyter.org/)

* [Spyder IDE](https://www.spyder-ide.org/)

* [Formatting strings to automatically call variables](https://realpython.com/lessons/formatting/)

<br>

## R

* [R for Data Science course on LinkedIn Learning] \(LinkedIn Learning)

* [R Essential Training: Wrangling and Visualizing Data] \(LinkedIn Learning)

* [R Essential Training Part 2: Modeling Data] \(LinkedIn Learning)

* [A note on for-loops in R] \(StackOverflow)

* [RStudio Cheat Sheets]

* [RStudio Cheat Sheet: ggplot2] \(a more powerful data visualization package than base R's plot function)

* *R for everyone : advanced analytics and graphics* by Jared Lander (available as an E-book from the [NU Library](https://onesearch.library.northeastern.edu/primo-explore/search?vid=NU))

* [R for Reproducible Scientific Analysis] \(Software Carpentry)

* [10 tips for making your R graphics look their best]

[R for Data Science course on LinkedIn Learning]: https://www.linkedin.com/learning/learning-r-2/r-for-data-science?u=74653650
[R Essential Training: Wrangling and Visualizing Data]: https://www.linkedin.com/learning/r-essential-training-wrangling-and-visualizing-data?contextUrn=urn%3Ali%3AlearningCollection%3A6820781619499036673&u=74653650
[R Essential Training Part 2: Modeling Data]: https://www.linkedin.com/learning/r-essential-training-part-2-modeling-data?contextUrn=urn%3Ali%3AlearningCollection%3A6820781619499036673&u=74653650
[A note on for-loops in R]: https://stackoverflow.com/questions/2908822/speed-up-the-loop-operation-in-r
[RStudio Cheat Sheets]: https://github.com/rstudio/cheatsheets
[RStudio Cheat Sheet: ggplot2]: https://github.com/rstudio/cheatsheets/blob/main/data-visualization-2.1.pdf
[R for Reproducible Scientific Analysis]: https://swcarpentry.github.io/r-novice-gapminder/
[10 tips for making your R graphics look their best]:(https://blog.revolutionanalytics.com/2009/01/10-tips-for-making-your-r-graphics-look-their-best.html)
<br>


## C/C++

* [C++ Language Tutorials/Overview](https://www.cplusplus.com/doc/tutorial/)

* [Headers and Includes Overview](https://www.cplusplus.com/articles/Gw6AC542/) (why use `.cc` and `.h` files)
<br>

## Fortran

* [Quickstart and other Fortran tutorials](https://fortran-lang.org/learn/#book-index)

* Understanding "precision" and "kind"
	* [Best practices for declaring precision of variables](https://fortran-lang.discourse.group/t/best-way-to-declare-a-double-precision-in-fortran/69)
	* [1d0 = 1.0d0](https://fortran-lang.discourse.group/t/1d0-versus-1-0d0/2065)

* [Rounding in Fortran](https://www.ibm.com/support/pages/rounding-midpoint-values-using-mass-functions-dnint-and-vdnint) 

* Interfacing Fortran and Python (f2py)
	* [f2py and alternatives](http://pythonchb.github.io/PythonTopics/interfacing_with_c/fortran_python.html)
	* [f2py has limited KIND parameters](https://numpy.org/devdocs/f2py/advanced.html#dealing-with-kind-specifiers)
	* [example using Python/C++/Fortran together](https://canvas.kth.se/courses/24933/pages/tutorial-cross-language-development-and-python-+-x)  
<br>

## Parallel Computing

### MPI

* [OpenMPI FAQ: General](https://www.open-mpi.org/faq/?category=general)

## HPC

### Slurm

* [Slurm Workload Manager website](https://slurm.schedmd.com/documentation.html) (with links to tutorials and a quick start guide)

* [Slurm Commands Summary](https://slurm.schedmd.com/pdfs/summary.pdf) (PDF)
