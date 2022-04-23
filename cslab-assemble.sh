#!/bin/sh
echo "----------------------------------------------------------------"
echo "Hi Fellow BC Programmer! To visualize the assembly code of your file,
this script will run the following command:
    - Know the path from CSLab to your file
    - Run 'gcc -S {file}.c' 
    - Iterate over that .s file!
    - Make sure your .c file and .s file have the same name.

DISCLAIMER: This script works best when program has ONE function. Also, this was made by a student
and this is a hard problem to visualize, so do not expect this to be perfect.

Nothing will be changed or overwritten in your cslab; if you want to see the code check github!"
echo "----------------------------------------------------------------"
echo "Enter @cslab.bc.edu directory:"
read DIRECTORY
echo "What is the name of your file? (ex: my_file)"
read FILE
echo "----------------------------------------------------------------"
echo "Copy the path to your ASSEMBLY file (i.e. ComputerSystems/pa7/):"
read FILE_PATH
echo "----------------------------------------------------------------"
echo "Enter your password (times out in 30 seconds)"
scp $DIRECTORY:$FILE_PATH\{$FILE.s,$FILE.c\} ./
mv $FILE.s input_file.s
mv $FILE.c input_file.c
echo "----------------------------------------------------------------"
python3 read_memory.py
echo "Open example_file.md, copy the text, and paste it into the website I just opened!"

open https://jbt.github.io/markdown-editor/