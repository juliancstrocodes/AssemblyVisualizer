from config import get_instruction_info, get_register_dict
from operations import *

f = open("input_file.s", "r")

INSTRUCTIONS = get_instruction_info()
REGISTERS = get_register_dict()


def print_stack(registers_used, addresses_used):
    registers = ""
    addresses = ""
    for register in registers_used:
        registers += "| " + str(register) + " | " + \
            str(registers_used[register]) + "|\n"

    for address in addresses_used:
        addresses += "| " + str(address) + " | " + \
            str(addresses_used[address]) + "|\n"
    return registers, addresses


def break_down_line(assembly_line):
    line = assembly_line.split()[0]
    args = assembly_line.split()[1:]
    bits = line[-1]
    mnemonic = ""
    if line[:-1] in INSTRUCTIONS:
        mnemonic += line[:-1]
    elif line in INSTRUCTIONS:
        mnemonic += line
    else:
        return None, None, None, None
    return line, mnemonic, args, bits


def write():
    # make string that loops through registers_used
    registers, addresses = print_stack(
        registers_used, addresses_used)

    new_f.write(
        "| Registers | Value |\n| ----------- | ----------- |\n" + registers + "\n")
    new_f.write(
        "| Addresses | Value |\n| ----------- | ----------- |\n" + addresses + "\n")


# TODO: memory address dictionary and register dictionary
registers_used = {"rsp": 10, "eax": 3, "esi": 400, "rsi": 10, "rbp": 69}
addresses_used = {"eax": 4, "rsi": 6, "rsp": 9, "4": None,
                  "5": None, "6": None, "7": None, "8": None, "9": None, }

new_f = open("example_file.md", "w")
new_f.write(
    "# Assembly Commands from File\ncopy and paste to https://stackedit.io/app# for a cleaner visual\n\n")


# Read the assembly file and store the instructions in a list
commands = []
for line in f:
    if line.strip().startswith(tuple(INSTRUCTIONS.keys())):
        commands.append(line.strip().replace("\t", " "))

for index, assembly_line in enumerate(commands):
    line, mnemonic, args, bits = break_down_line(assembly_line)

    if mnemonic not in INSTRUCTIONS:
        continue

    new_f.write(f"## ```{assembly_line}``` \n")

    if (assembly_line == "pushq %rbp" and commands[index + 1] == "movq %rsp, %rbp"):
        new_f.write("<h4>Opening up the stack frame</h4>\n\n")
        # TODO initialize stack frame
        continue
    if (assembly_line == "popq %rbp" and commands[index + 1] == "ret"):
        new_f.write("<h4>Closing up the stack frame</h4>\n\n")
        continue

    try:
        if INSTRUCTIONS[mnemonic][0] == "arithmetic_operations":
            if len(args) == 1:
                arg1 = args[0]
                arg2 = None
            else:
                arg1 = args[0]
                arg2 = args[1]
            registers_used, addresses_used = summation_operations(
                arg1, registers_used, addresses_used, mnemonic, arg2)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "mult_operations":
            if len(args) == 2:
                arg1 = args[0]
                arg2 = args[1]
                arg3 = None
            else:
                arg1 = args[0]
                arg2 = args[1]
                arg3 = args[2]
            registers_used, addresses_used = mult_operations(
                arg1, arg2, registers_used, addresses_used, mnemonic, arg3)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "div_operations":
            arg1 = args[0]
            registers_used, addresses_used = div_operations(
                arg1, registers_used, addresses_used, mnemonic)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "bitwise_operations":
            if len(args) == 1:
                arg1 = args[0]
                arg2 = None
            else:
                arg1 = args[0]
                arg2 = args[1]
            registers_used, addresses_used = bitwise_operations(
                arg1, registers_used, addresses_used, mnemonic, arg2)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "shift_operations":
            arg1 = args[0]
            arg2 = args[1]
            registers_used, addresses_used = shift_operations(
                arg1, arg2, registers_used, addresses_used, mnemonic)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "jump_begin":
            arg1 = args[0]
            registers_used, addresses_used = jump_begin(
                arg1, registers_used, addresses_used, mnemonic)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "cmp_jump_to":
            # if its a cmp then it will look at current and next line
            if mnemonic == "cmp":
                arg1 = args[0]
                arg2 = args[1]
                registers_used, addresses_used = cmp_jump_to(
                    arg1, arg2, registers_used, addresses_used, mnemonic, commands[index + 1])
                write()
            else:
                continue
        elif INSTRUCTIONS[mnemonic][0] == "mov_operation":
            arg1 = args[0]
            arg2 = args[1]
            registers_used, addresses_used = mov_operation(
                arg1, arg2, registers_used, addresses_used)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "lea_operation":
            registers_used, addresses_used = lea_operation(
                assembly_line, registers_used, addresses_used, mnemonic + bits)
            write()
        elif INSTRUCTIONS[mnemonic][0] == "frame_operation":
            continue
    except Exception as e:
        continue
new_f.write(
    "###### Author: [Julian Castro](https://www.linkedin.com/in/julian-castro-7950aa1a7/) - castrojv@bc.edu\n\n")

new_f.write(
    "<h6>References: https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html</h6>")

# TODO: comparison operations need work
# TODO: some operations do not have a bit end
# TODO: opening and closing stack with call
# TODO: break up operations by sections (.L0,...)
