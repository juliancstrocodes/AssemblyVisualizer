DEFINITIONS = ["The mov instruction copies the data item referred to by its first operand (i.e. register contents, memory contents, or a constant value) into the location referred to by its second operand (i.e. a register or memory). While register-to-register moves are possible, direct memory-to-memory moves are not. In cases where memory transfers are desired, the source memory contents must first be loaded into a register, then can be stored to the destination memory address.",
               "The push instruction places its operand onto the top of the hardware supported stack in memory. Specifically, push first decrements ESP by 4, then places its operand into the contents of the 32-bit location at address (%esp). ESP (the stack pointer) is decremented by push since the x86 stack grows down — i.e. the stack grows from high addresses to lower addresses.",
               "The pop instruction removes the 4-byte data element from the top of the hardware-supported stack into the specified operand (i.e. register or memory location). It first moves the 4 bytes located at memory location (%esp) into the specified register or memory location, and then increments ESP by 4.",
               "The lea instruction places the address specified by its first operand into the register specified by its second operand. Note, the contents of the memory location are not loaded, only the effective address is computed and placed into the register. This is useful for obtaining a pointer into a memory region or to perform simple arithmetic operations.",
               "The add instruction adds together its two operands, storing the result in its second operand. Note, whereas both operands may be registers, at most one operand may be a memory location.",
               "The sub instruction stores in the value of its second operand the result of subtracting the value of its first operand from the value of its second operand. As with add, whereas both operands may be registers, at most one operand may be a memory location.",
               "The inc instruction increments the contents of its operand by one.", "The dec instruction decrements the contents of its operand by one.",
               "The imul instruction has two basic formats: two-operand (first two syntax listings above) and three-operand (last two syntax listings above). The two-operand form multiplies its two operands together and stores the result in the second operand. The result (i.e. second) operand must be a register. The three operand form multiplies its second and third operands together and stores the result in its last operand. Again, the result operand must be a register. Furthermore, the first operand is restricted to being a constant value.",
               "The idiv instruction divides the contents of the 64 bit integer EDX:EAX (constructed by viewing EDX as the most significant four bytes and EAX as the least significant four bytes) by the specified operand value. The quotient result of the division is stored into EAX, while the remainder is placed in EDX.",
               "These instructions perform the specified logical operation (logical bitwise and, or, and exclusive or, respectively) on their operands, placing the result in the first operand location.", "These instructions perform the specified logical operation (logical bitwise and, or, and exclusive or, respectively) on their operands, placing the result in the first operand location.", "These instructions perform the specified logical operation (logical bitwise and, or, and exclusive or, respectively) on their operands, placing the result in the first operand location.",
               "Logically negates the operand contents (that is, flips all bit values in the operand).",
               "Performs the two's complement negation of the operand contents.",
               "These instructions shift the bits in their first operand's contents left and right, padding the resulting empty bit positions with zeros. The shifted operand can be shifted up to 31 places. The number of bits to shift is specified by the second operand, which can be either an 8-bit constant or the register CL. In either case, shifts counts of greater then 31 are performed modulo 32.", "These instructions shift the bits in their first operand's contents left and right, padding the resulting empty bit positions with zeros. The shifted operand can be shifted up to 31 places. The number of bits to shift is specified by the second operand, which can be either an 8-bit constant or the register CL. In either case, shifts counts of greater then 31 are performed modulo 32.",
               "Transfers program control flow to the instruction at the memory location indicated by the operand.",
               "The jmp instruction transfers program control flow to the instruction at the memory location indicated by the operand.",
               "Jump when equal. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Jump when not equal. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Jump when last result was zero. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Jump when greater than. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Jump when greater or equal to. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Jump when less than. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Jump when less than or equal to. These instructions are conditional jumps that are based on the status of a set of condition codes that are stored in a special register called the machine status word. The contents of the machine status word include information about the last arithmetic operation performed. For example, one bit of this word indicates if the last result was zero. Another indicates if the last result was negative. Based on these condition codes, a number of conditional jumps can be performed. For example, the jz instruction performs a jump to the specified operand label if the result of the last arithmetic operation was zero. Otherwise, control proceeds to the next instruction in sequence.",
               "Compare the values of the two specified operands, setting the condition codes in the machine status word appropriately. This instruction is equivalent to the sub instruction, except the result of the subtraction is discarded instead of replacing the first operand.",
               "These instructions implement a subroutine call and return. The call instruction first pushes the current code location onto the hardware supported stack in memory (see the push instruction for details), and then performs an unconditional jump to the code location indicated by the label operand. Unlike the simple jump instructions, the call instruction saves the location to return to when the subroutine completes.",
               "The ret instruction implements a subroutine return mechanism. This instruction first pops a code location off the hardware supported in-memory stack (see the pop instruction for details). It then performs an unconditional jump to the retrieved code location.",
               "Converts signed long to signed double long."
               ]

BITS = dict({
    "b": "1 byte",
    "w": "2 bytes",
    "l": "4 bytes",
    "q": "8 bytes"
})


def get_instruction_info(registers):
    v_or_r = []
    args = []
    for i in range(3):
        if i < len(registers):
            if registers[i].startswith("(") and registers[i].endswith(")"):
                v_or_r.append("value")
                args.append(registers[i])
            else:
                v_or_r.append("register")
                args.append(registers[i])
        else:
            v_or_r.append(None)
            args.append(None)

    return dict({
        "mov": ["https://i.ytimg.com/vi/0_r-3eWB54c/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDlD2i6F3GA6o1dmrfPnUxHj0nsfw", ["Move", v_or_r[0], "in", args[0], "to", v_or_r[1], "in", args[1]], DEFINITIONS[0]],
        "push": ["url", ["Push", v_or_r[0], args[0], "on stack"], DEFINITIONS[1]],
        "pop": ["url", ["Pop", v_or_r[0], args[0], "from stack"], DEFINITIONS[2]],
        "lea": ["url", "Load effective address", DEFINITIONS[3]],
        "add": ["url", "Integer addition", DEFINITIONS[4]],
        "sub": ["url", "Integer subtraction", DEFINITIONS[5]],
        "inc": ["url", "Increment", DEFINITIONS[6]],
        "dec": ["url", "Decrement", DEFINITIONS[7]],
        "imul": ["url", "Integer multiply", DEFINITIONS[8]],
        "idiv": ["url", ["Divide value in (%eax) to value in", args[0]], DEFINITIONS[9]],
        "and": ["url", "Bitwise logical and", DEFINITIONS[10]],
        "or": ["url", "Bitwise logical or", DEFINITIONS[11]],
        "xor": ["url", "Bitwise logical xor", DEFINITIONS[12]],
        "not": ["url", "Bitwise logical not", DEFINITIONS[13]],
        "neg": ["url", "Negate", DEFINITIONS[14]],
        "shl": ["url", "Shift left", DEFINITIONS[15]],
        "shr": ["url", "Shift right", DEFINITIONS[16]],
        "jmp": ["url", "Jump", DEFINITIONS[17]],
        "je": ["url", "Jump when equal", DEFINITIONS[18]],
        "jne": ["url", "Jump when not equal", DEFINITIONS[19]],
        "jz": ["url", "Jump when last result was zero", DEFINITIONS[20]],
        "jg": ["url", "Jump when greater than", DEFINITIONS[21]],
        "jge": ["url", "Jump when greater or equal to", DEFINITIONS[22]],
        "jl": ["url", "Jump when less than", DEFINITIONS[23]],
        "jle": ["url", "Jump when less than or equal to", DEFINITIONS[24]],
        "cmp": ["url", "Compare", DEFINITIONS[25]],
        "call": ["url", "Call", DEFINITIONS[26]],
        "ret": ["url", "Return", DEFINITIONS[27]],
        "cltd": ["url", "Convert long to double; moves sign bit of (%eax) to %edx", DEFINITIONS[28]],
    })
