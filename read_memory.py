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
            return address_of_register, True, arg_cleaned[1:-1]
        else:
            address_of_register = registers_used[arg_cleaned]
            return address_of_register, False, arg_cleaned
    except Exception as e:
        return None, None, None


def summation_operations(arg1, registers_used, addresses_used, mnemonic, arg2=None):
    # are the args addresses or register
    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)
    value_2, is_value_2, arg2_cleaned = get_value(
        arg2, registers_used, addresses_used)

    # if arg2 is none, then operation is inc/dec
    if arg2 == None:
        if mnemonic == 'inc':
            result = hex(value_1 + 1)
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


def mult_operations(arg1, arg2, registers_used, addresses_used, mnemonic, arg3=None):
    # TODO: signed or unsigned multiplication operations
    if mnemonic[0] == "i":
        # it is signed
        return

    # are the args addresses or register
    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)
    value_2, is_value_2, arg2_cleaned = get_value(
        arg2, registers_used, addresses_used)
    value_3, is_value_3, arg3_cleaned = get_value(
        arg3, registers_used, addresses_used)

    if arg3 == None:
        result = hex(value_1 * value_2)
        if is_value_2:
            addresses_used[arg2_cleaned] = result
        else:
            registers_used[arg2_cleaned] = result
    else:
        result = hex(value_1 * value_2)
        if is_value_3:
            addresses_used[arg3_cleaned] = result
        else:
            registers_used[arg3_cleaned] = result

    return registers_used, addresses_used


def div_operations(arg1, registers_used, addresses_used, mnemonic):
    # TODO: signed or unsigned division operations
    if mnemonic[0] == "i":
        # it is signed
        return

    divisor = registers_used["eax"]
    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)

    registers_used["eax"] = hex(value_1 // divisor)
    registers_used["edx"] = hex(value_1 % divisor)

    return registers_used, addresses_used


def bitwise_operations(arg1, registers_used, addresses_used, mnemonic, arg2=None):
    # are the args addresses or register
    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)
    value_2, is_value_2, arg2_cleaned = get_value(
        arg2, registers_used, addresses_used)

    # if arg2 is None, then operation is not or neg
    if arg2 == None:

        if mnemonic == 'not':
            result = hex(~value_1)
        elif mnemonic == 'neg':
            result = hex(-value_1)

        if is_value_1:
            addresses_used[arg1_cleaned] = result
        else:
            registers_used[arg1_cleaned] = result

    else:
        if mnemonic == 'and':
            result = hex(value_1 & value_2)
        elif mnemonic == 'or':
            result = hex(value_1 | value_2)
        elif mnemonic == 'xor':
            result = hex(value_1 ^ value_2)

        if is_value_2:
            addresses_used[arg2_cleaned] = result
        else:
            registers_used[arg2_cleaned] = result

    return registers_used, addresses_used


def shift_operations(arg1, arg2, registers_used, addresses_used, mnemonic):

    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)
    value_2, is_value_2, arg2_cleaned = get_value(
        arg2, registers_used, addresses_used)

    if mnemonic == 'shl':
        result = hex(value_1 << value_2)
    elif mnemonic == 'shr':
        result = hex(value_1 >> value_2)

    if is_value_1:
        addresses_used[arg2_cleaned] = result
    else:
        registers_used[arg2_cleaned] = result

    return


def jump_begin(arg1, registers_used, addresses_used, mnemonic):
    # TODO: get value of linking label
    print(f"Jump to {arg1}")
    return


def cmp_jump_to(arg1, arg2, registers_used, addresses_used, mnemonic, next_line):
    # TODO: make cmp operations that returns
    value_1, is_value_1, arg1_cleaned = get_value(
        arg1, registers_used, addresses_used)
    value_2, is_value_2, arg2_cleaned = get_value(
        arg2, registers_used, addresses_used)

    next_mnemonic = next_line.split()[0]
    jump_dst = next_line.split()[1]

    if next_mnemonic == "jz":
        if (eval(f"{value_1} {INSTRUCTIONS[next_mnemonic][1]}")):
            jump_begin(jump_dst, registers_used, addresses_used, mnemonic)

    if (eval(f"{value_1} {INSTRUCTIONS[next_mnemonic][1]} {value_2}")):
        jump_begin(jump_dst, registers_used, addresses_used, mnemonic)
    else:
        print("No Jump")
        return

    # TODO: handle "jz"

    print("next line:", next_line)


# TODO: memory address dictionary and register dictionary
registers_used = {"rsp": 10, "eax": 3, "esi": 400, "rsi": 10}
addresses_used = {"eax": 4, "2": None, "3": None, "4": None,
                  "5": None, "6": None, "7": None, "8": None, "9": None, }

# Read the assembly file and store the instructions in a list
commands = []
for line in f:
    if line.strip().startswith(tuple(INSTRUCTIONS.keys())):
        commands.append(line.strip().replace("\t", " "))

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
            registers_used, addresses_used = summation_operations(
                arg1, registers_used, addresses_used, mnemonic, arg2)
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
        elif INSTRUCTIONS[mnemonic][0] == "div_operations":
            arg1 = args[0]
            registers_used, addresses_used = div_operations(
                arg1, registers_used, addresses_used, mnemonic)
        elif INSTRUCTIONS[mnemonic][0] == "bitwise_operations":
            if len(args) == 1:
                arg1 = args[0]
                arg2 = None
            else:
                arg1 = args[0]
                arg2 = args[1]
            registers_used, addresses_used = bitwise_operations(
                arg1, registers_used, addresses_used, mnemonic, arg2)
        elif INSTRUCTIONS[mnemonic][0] == "shift_operations":
            arg1 = args[0]
            arg2 = args[1]
            registers_used, addresses_used = shift_operations(
                arg1, arg2, registers_used, addresses_used, mnemonic)
        elif INSTRUCTIONS[mnemonic][0] == "jump_begin":
            arg1 = args[0]
            registers_used, addresses_used = jump_begin(
                arg1, registers_used, addresses_used, mnemonic)
        elif INSTRUCTIONS[mnemonic][0] == "cmp_jump_to":
            # if its a cmp then it will look at current and next line
            if mnemonic == "cmp":
                arg1 = args[0]
                arg2 = args[1]
                registers_used, addresses_used = cmp_jump_to(
                    arg1, arg2, registers_used, addresses_used, mnemonic, commands[index + 1])
            else:
                continue

    except Exception as e:
        continue

# TODO: some operations do not have a bit end
# TODO: opening and closing stack with call
# print(registers_used, addresses_used)
