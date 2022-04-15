BITS = dict({
    "b": "8",
    "w": "16",
    "l": "32",
    "q": "64"
})


def get_register_dict():
    return dict({
        "rax": ["eax", "ax", "ah", "al"],
        "rbx": ["ebx", "bx", "bh", "bl"],
        "rcx": ["ecx", "cx", "ch", "cl"],
        "rdx": ["edx", "dx", "dh", "dl"],
        "rsi": ["esi", "si", "sil"],
        "rdi": ["edi", "di", "dil"],
        "rsp": ["esp", "sp", "spl"],
        "rbp": ["ebp", "bp", "bpl"],
        "r8": ["r8d", "r8w", "r8b"],
        "r9": ["r9d", "r9w", "r9b"],
        "r10": ["r10d", "r10w", "r10b"],
        "r11": ["r11d", "r11w", "r11b"],
        "r12": ["r12d", "r12w", "r12b"],
        "r13": ["r13d", "r13w", "r13b"],
        "r14": ["r14d", "r14w", "r14b"],
        "r15": ["r15d", "r15w", "r15b"],
        "rip": ["eip", "ip", "pc"]
    })


def get_instruction_info():
    return dict({
        "mov": ["mov_operation"],
        "push": ["frame_operation"],
        "pop": ["frame_operation"],
        "lea": ["lea_operation"],
        "add": ["arithmetic_operations"],
        "sub": ["arithmetic_operations"],
        "inc": ["arithmetic_operations"],
        "dec": ["arithmetic_operations"],
        "imul": ["mult_operations"],
        "mul": ["mult_operations"],
        "idiv": ["div_operations"],
        "div": ["div_operations"],
        "and": ["bitwise_operations"],
        "or": ["bitwise_operations"],
        "xor": ["bitwise_operations"],
        "not": ["bitwise_operations"],
        "neg": ["bitwise_operations"],
        "shl": ["shift_operations"],
        "shr": ["shift_operations"],
        "jmp": ["jump_begin"],
        "je": ["cmp_jump_to", "=="],
        "jne": ["cmp_jump_to", "!="],
        "jz": ["cmp_jump_to", "=="],
        "jg": ["cmp_jump_to", ">"],
        "jge": ["cmp_jump_to", ">="],
        "jl": ["cmp_jump_to", "<"],
        "jle": ["cmp_jump_to", "<="],
        "cmp": ["cmp_jump_to"],
        "call": [],
        "ret": ["frame_operation"],
        "clt": [],
    })
