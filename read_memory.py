import sys
from config import ARG_REGISTERS, BITS_SUFFIX, get_instruction_info, get_register_dict
from operations import *
from visualize import visualize
import re

f = open("input_file.s", "r")

INSTRUCTIONS = get_instruction_info()
REGISTERS = get_register_dict()


def open_stack():
    registers_used = {"rbp": 0x0}
    addresses_used = {0x0: None}
    for register in REGISTERS:
        if register not in registers_used:
            registers_used[register] = sys.maxsize
            for section in REGISTERS[register]:
                registers_used[section] = sys.maxsize
    return registers_used, addresses_used


def print_stack(registers_used, addresses_used):
    registers = ""
    addresses = ""
    for register in registers_used:
        if registers_used[register] != None and registers_used[register] != sys.maxsize:
            registers += "| " + str(register) + " | " + \
                str(registers_used[register]) + "|\n"

    for address in addresses_used:
        if addresses_used[address] != None and addresses_used[address] != sys.maxsize:
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


if __name__ == "__main__":

    # TODO: memory address dictionary and register dictionary
    registers_used = {"rbp": 0x0}
    addresses_used = {0x0: None}

    dummy_params, param_types, signature = visualize()

    new_f = open("example_file.md", "w")
    new_f.write("# Assembly File Visualization\n")
    new_f.write(
        "#### Your parameters and the random arguments we used:\n\n")

    for index, param in enumerate(signature):
        param = param.split(" ")[-1]
        new_f.write("__" + param + "__" + " --> " +
                    str(dummy_params[index]) + "\n\n")

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

        # Skip first command
        if index == 0:
            continue

        if (commands[index - 1] == "pushq %rbp" and assembly_line == "movq %rsp, %rbp"):
            new_f.write("<h4>Opened up the stack frame</h4>\n\n")
            registers_used, addresses_used = open_stack()
            continue
        if (assembly_line == "popq %rbp" and commands[index + 1] == "ret"):
            new_f.write("<h4>Closed up the stack frame</h4>\n\n")
            continue

        # Check if assembly_line is placing parameters in the stack
        try:
            if mnemonic == "mov" and len(dummy_params) > 0 and bits == param_types[0] and re.sub(r'[^a-zA-Z0-9\[\]]', '', args[0]) in ARG_REGISTERS[BITS_SUFFIX[bits]]:
                disp = int(args[1].split("(")[0])
                addresses_used[int(registers_used["rbp"]) +
                               disp] = dummy_params[0]
                dummy_params.remove(dummy_params[0])
                param_types.remove(param_types[0])
                write()
                continue
        except Exception as e:
            pass

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
