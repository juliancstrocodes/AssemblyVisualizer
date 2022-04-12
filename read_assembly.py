from config import get_instruction_info
from config import BITS

f = open("input_file.s", "r")
INSTRUCTIONS = get_instruction_info([])

# Read the assembly file and store the instructions in a list
commands = []
for line in f:
    if line.strip().startswith(tuple(INSTRUCTIONS.keys())):
        commands.append(line.strip().replace("\t", " "))

new_f = open("output_file.md", "w")
new_f.write(
    "# Assembly Commands from File (copy and paste to https://stackedit.io/app#)\n\n")
# Reads the elements of each line and prints appropriate instructions
for assembly_line in commands:
    try:
        line = assembly_line.split()[0]
        registers = assembly_line.split()[1:]
        INSTRUCTIONS = get_instruction_info(registers)
        bits = line[-1]
        command = line[:-1]
        new_f.write("## ```" + assembly_line + "```\n")
        if command in INSTRUCTIONS:
            new_f.write("<strong>Assembly Command<strong>: " +
                        " ".join(INSTRUCTIONS[command][1]) + "\n\n")
            new_f.write("<strong>Bytes<strong>: " +
                        bits + " == " + BITS[bits] + "\n\n")
            new_f.write("> " + INSTRUCTIONS[command][2] + "\n")
            new_f.write("![image](" + INSTRUCTIONS[command][0] + ")\n")
        else:
            new_f.write("<strong>Assembly Command<strong>: " +
                        INSTRUCTIONS[line][1] + "\n")
            new_f.write("> " + INSTRUCTIONS[line][2] + "\n")

        new_f.write("\n")
    except:
        print("Error: Invalid instruction ", command)
new_f.write("<h6>https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html</h6>")
