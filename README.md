
# Assembly Instruction Visualizer

Visualization tool made for simple C files that allows students in Boston College
CSCI2271 understand how assembly instructions alter memory on the stack. 
Given the complexity of the issue, this needs work. Feel free to
fork and/or improve it.
## Usage

Given the following prompt enter your Boston College cslab
username:

```
----------------------------------------------------------------
Hi Fellow BC Programmer! To visualize the assembly code of your file,
this script will run the following command:
    - Know the path from CSLab to your file
    - Run 'gcc -S {file}.c' 
    - Iterate over that .s file!
    - Make sure your .c file and .s file have the same name.

DISCLAIMER: This script works best when program has ONE function. Also, this was made by a student
and this is a hard problem to visualize, so do not expect this to be perfect.

Nothing will be changed or overwritten in your cslab; if you want to see the code check github!
----------------------------------------------------------------
Enter @cslab.bc.edu directory:

```

Continue following the instructions. This is an example of how it should
look:

```
What is the name of your file? (ex: my_file)
div1
----------------------------------------------------------------
Copy the path to your ASSEMBLY file (i.e. ComputerSystems/pa7/):
ComputerSystems/pa7/
----------------------------------------------------------------
Enter your password (times out in 30 seconds)
castrojv@cslab.bc.edu's password: 
div1.s                                                                     100%  581    72.4KB/s   00:00    
div1.c                                                                     100%  183    22.7KB/s   00:00    
----------------------------------------------------------------
Open example_file.md, copy the text, and paste it into the website I just opened!
```

This should open a website. Copy the contents of example_file.md
and copy and paste it onto the website. This should present your results!

#### [Example Result](https://github.com/juliancstrocodes/assembly_visualizer/blob/main/example_file.md/)


__Feel free to report any errors on the "Issues" page of this repo__
## Installation

Clone this repository on your local machine. By running
this command on your local terminal:
```
git clone git@github.com:juliancstrocodes/assembly_visualizer.git
```

Once cloned. Permit the script run,... and run it.
```
chmod +x cslab-assemble.sh
./cslab-assemble.sh
```


## Support

For support, email castrojv@bc.edu.

