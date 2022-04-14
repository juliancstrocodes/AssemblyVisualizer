from config import get_instruction_info, get_register_dict, BITS
import re

f = open("input_file.s", "r")
regex = re.compile('[^a-zA-Z0-9()]')

INSTRUCTIONS = get_instruction_info()
REGISTERS = get_register_dict()


def break_down_line(assembly_line):
    line = assembly_line.split()[0]
    args = assembly_line.split()[1:]
    bits = line[-1]
    mnemonic = line[:-1]
    return line, mnemonic, args, bits


def get_value(arg, registers_used, addresses_used):
    try:
        arg_cleaned = regex.sub('', arg)

        # if arg_cleaned is a const
        if arg_cleaned.isdigit():
            return int(arg_cleaned)

        if arg_cleaned[0] == '(':
            address_of_register = addresses_used[arg_cleaned[1:-1]]
            print(address_of_register)
            return address_of_register, True, arg_cleaned[1:-1]
        else:
            address_of_register = registers_used[arg_cleaned]
            return address_of_register, False, arg_cleaned
    except Exception as e:
        return None, None, None


def arithmetic_operations(arg1, registers_used, addresses_used, mnemonic, arg2=None):
    # are the args addresses or register
    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)
    value_2, is_value_2, arg2_cleaned = get_value(
        arg2, registers_used, addresses_used)

    # if arg2 is none, then operation is inc/dec
    if arg2 == None:
        if mnemonic == 'inc':
            result = value_1 + 1
        elif mnemonic == 'dec':
            result = hex(value_1 - 1)

        if is_value_1:
            addresses_used[arg1_cleaned] = result
        else:
            registers_used[arg1_cleaned] = result

    else:
        if mnemonic == 'add':
            result = hex(value_2 + value_1)
        elif mnemonic == 'sub':
            result = hex(value_2 - value_1)

        if is_value_2:
            addresses_used[arg2_cleaned] = result
        else:
            registers_used[arg2_cleaned] = result

    return registers_used, addresses_used


registers_used = {"rsp": 1, "eax": 3}
addresses_used = {"eax": 0, "2": None, "3": None, "4": None,
                  "5": None, "6": None, "7": None, "8": None, "9": None, }

# Read the assembly file and store the instructions in a list
commands = []
for line in f:
    if line.strip().startswith(tuple(INSTRUCTIONS.keys())):
        commands.append(line.strip().replace("\t", " "))

print(addresses_used)
for index, assembly_line in enumerate(commands):
    line, mnemonic, args, bits = break_down_line(assembly_line)

    if assembly_line == "pushq %rbp" and commands[index + 1] == "movq %rsp, %rbp":
        continue

    if assembly_line == "popq %rbp" and commands[index + 1] == "ret":
        continue

    try:
        if INSTRUCTIONS[mnemonic][0] == "arithmetic_operations":
            if len(args) == 1:
                arg1 = args[0]
                arg2 = None
            else:
                arg1 = args[0]
                arg2 = args[1]
            registers_used, addresses_used = arithmetic_operations(arg1, registers_used,
                                                                   addresses_used, mnemonic, arg2)

    except Exception as e:
        continue

print(addresses_used)
