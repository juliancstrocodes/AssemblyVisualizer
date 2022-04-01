from config import INSTRUCTIONS
import time

f = open("input_file.s", "r")

commands = []
for line in f:
    if line.strip().startswith(tuple(INSTRUCTIONS.keys())):
        commands.append(line.strip().replace("\t", " "))

# read lines 1 second at a time
for line in commands:
    try:
        print(INSTRUCTIONS[line.split()[0]][1])
        time.sleep(1)

    except:
        print("Error: Invalid instruction")
