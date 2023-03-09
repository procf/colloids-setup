# Hardware Requirements and System Recommendations

This is a guide to choosing a computer for research simulating colloids with HOOMD-blue in the PRO-CF Research Group.

[Last Update: June 2023]

This guide was compiled by Rob Campbell.
<br>

## Contents
1. [Operating System](/System-Setup/00-Hardware.md#operating-system)
2. [Laptop vs. Desktop](/System-Setup/00-Hardware.md#laptop-vs-desktop)
3. [Memory](/System-Setup/00-Hardware.md#memory)
4. [Storage](/System-Setup/00-Hardware.md#storage)
5. [GPU](/System-Setup/00-Hardware.md#gpu)
6. [Processor](/System-Setup/00-Hardware.md#processor)
7. [Current Hardware Used by Group Members](/System-Setup/00-Hardware.md#current-hardware-used-by-group-members)
<br>

## Operating System

HOOMD-blue currently requires macOS or Linux. MacOS is recommended because it is what current group members use, and what you can get the most help troubleshooting. That said, if you are familiar with Linux and prefer it over macOS you can definitely choose to use a Linux machine.
<br>
<br>
## Laptop vs. Desktop

A laptop is sufficient for this work. Most simulations are run on Northeastern's Discovery research cluster, so you will mainly be using your computer for writing scripts, debugging, and interfacing with the cluster. Most members of the group have chosen 13" laptops because they're more portable, but if you prefer a larger screen for programming absolutely go for it.
<br>
<br>
## Memory

Memory is the **most important** feature for our work. Opt for at least 16GB, although it is unlikely you'll actually need more than 16GB unless you plan to use other software that requries it.
<br>
<br>
## Storage

For storage, we recommend *at least* 500GB-1TB. Our files can be quite large, and you will need to keep some of them on your laptop for analysis. You can get by on 500GB, but more will make life easier. Additional long term storage is available on Discovery.
<br>
<br>
## GPU

Although HOOMD-blue does have GPU options, our implementation of HOOMD-blue is currently CPU only and you will **not** need a high performance GPU unless you intend to develop new code for it. You will also have access to other GPU options through Northeastern's high performance computing cluster ("Discovery"). 
<br>
<br>
## Processor

Any reasonably current processor should be good enough for this work. Our group members use the 2022 Apple M1 Pro, 2018 Intel i7, 2020 Intel i7, and 2020 Intel i5 without issue.
<br>
<br>
## Current Hardware Used by Group Members

[Last Update: March 2023]

14-inch MacBook Pro 2022
* Processor: Apple M1 Pro with 10-core CPU, 16-core GPU, 16-core Neural Engine
* Memory: 32GB unified memory
* Storage: 1TB
<br>

16-inch MacBook Pro 2022
* Processor: Apple M1 Pro with 10-core CPU, 16-core GPU, 16-core Neural Engine
* Memory: 32GB unified memory
* Storage: 1TB
<br>

13-inch MacBook Pro 2020
* Processor: 2 GHz Quad-Core Intel Core i7
* Memory: 16GB 3733 MHz LPDDR4X
* Storage: 512GB SSD
<br>

13-inch MacBook Pro 2020
* Processor: 2 GHz Quad-Core Intel Core i5
* Memory: 16GB 3733 MHz LPDDR4X
* Storage: 512GB SSD
<br>

13-inch MacBook Pro 2018
* Processor: 2.7 GHz Quad-Core Intel Core i7
* Memory: 16GB 2133 MHz LPDDR3
* Storage: 500GB
<br>


