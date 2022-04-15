# Assembly Commands from File

copy and paste to https://stackedit.io/app# for a cleaner visual

## `pushq %rbp`

<h4>Opening up the stack frame</h4>

## `movq %rsp, %rbp`

| Registers | Value |
| --------- | ----- |
| rsp       | 10    |
| eax       | 3     |
| esi       | 400   |
| rsi       | 10    |
| rbp       | 10    |

| Addresses | Value |
| --------- | ----- |
| eax       | 4     |
| rsi       | 6     |
| rsp       | 9     |
| 4         | None  |
| 5         | None  |
| 6         | None  |
| 7         | None  |
| 8         | None  |
| 9         | None  |

## `movl %edi, %eax`

| Registers | Value |
| --------- | ----- |
| rsp       | 10    |
| eax       | None  |
| esi       | 400   |
| rsi       | 10    |
| rbp       | 10    |

| Addresses | Value |
| --------- | ----- |
| eax       | 4     |
| rsi       | 6     |
| rsp       | 9     |
| 4         | None  |
| 5         | None  |
| 6         | None  |
| 7         | None  |
| 8         | None  |
| 9         | None  |

## `leaq -1(%rsi, %rsp, 2), %edx`

| Registers | Value |
| --------- | ----- |
| rsp       | 10    |
| eax       | None  |
| esi       | 400   |
| rsi       | 10    |
| rbp       | 10    |
| edx       | 0x17  |

| Addresses | Value |
| --------- | ----- |
| eax       | 4     |
| rsi       | 6     |
| rsp       | 9     |
| 4         | None  |
| 5         | None  |
| 6         | None  |
| 7         | None  |
| 8         | None  |
| 9         | None  |

## `movq %rdx, %r10`

| Registers | Value |
| --------- | ----- |
| rsp       | 10    |
| eax       | None  |
| esi       | 400   |
| rsi       | 10    |
| rbp       | 10    |
| edx       | 0x17  |
| None      | None  |

| Addresses | Value |
| --------- | ----- |
| eax       | 4     |
| rsi       | 6     |
| rsp       | 9     |
| 4         | None  |
| 5         | None  |
| 6         | None  |
| 7         | None  |
| 8         | None  |
| 9         | None  |

## `cltd`

## `divl %esi`

## `movl %edx, (%r10)`

| Registers | Value |
| --------- | ----- |
| rsp       | 10    |
| eax       | None  |
| esi       | 400   |
| rsi       | 10    |
| rbp       | 10    |
| edx       | 0x17  |
| None      | 0x17  |

| Addresses | Value |
| --------- | ----- |
| eax       | 4     |
| rsi       | 6     |
| rsp       | 9     |
| 4         | None  |
| 5         | None  |
| 6         | None  |
| 7         | None  |
| 8         | None  |
| 9         | None  |

## `popq %rbp`

<h4>Closing up the stack frame</h4>

## `ret`

###### Author: [Julian Castro](https://www.linkedin.com/in/julian-castro-7950aa1a7/) - castrojv@bc.edu

<h6>References: https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html</h6>
