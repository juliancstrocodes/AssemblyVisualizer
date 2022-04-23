from config import BITS
import random


def visualize():
    # Read file input_file.s and find first line that does not start with a tab character
    f_s = open("input_file.s", "r")
    lines = f_s.readlines()

    function = ""
    signature = ""
    param_types = []

    for line in lines:
        if line[0] != '\t':
            function += line.strip()[:-1]
            break

    f_c = open("input_file.c", "r")

    # find function in c file
    lines = f_c.readlines()
    # if lines contains function
    for line in lines:
        if function in line:
            # Print string within parentheses
            signature = line.strip()[line.find('(') + 1:line.find(')')]
            break

    signature = signature.split(",")
    dummy_params = [0] * len(signature)
    # Find type declaration in each string
    for parameter in signature:
        if "*" in parameter:
            param_types.append("q")
            # Generate a random pointer value
            dummy_params[signature.index(parameter)] = "0x" + \
                hex(random.randint(0, 2**BITS["pointer"]))[2:]
        elif "int" in parameter:
            param_types.append("l")
            # Generate a random integer value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["int"])
        elif "char" in parameter:
            param_types.append("b")
            # Generate a random character value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["char"])
        elif "float" in parameter:
            param_types.append("l")
            # Generate a random float value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["float"])
        elif "double" in parameter:
            param_types.append("q")
            # Generate a random double value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["double"])
        elif "long" in parameter:
            param_types.append("q")
            # Generate a random long value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["long"])
        elif "short" in parameter:
            param_types.append("w")
            # Generate a random short value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["short"])
        elif "unsigned" in parameter:
            param_types.append("l")
            # Generate a random unsigned value
            dummy_params[signature.index(parameter)] = random.getrandbits(
                BITS["unsigned"])
        elif "signed" in parameter:
            param_types.append("l")
            # Generate a random signed value
            dummy_params[signature.index(
                parameter)] = random.getrandbits(BITS["signed"])
        elif "void" in parameter:
            param_types.append("v")
            # Generate a random void value
            dummy_params[signature.index(parameter)] = "0"
        else:
            continue

    return dummy_params, param_types, signature
