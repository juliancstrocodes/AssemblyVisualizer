# Assembly Commands from File
copy and paste to https://stackedit.io/app# for a cleaner visual

## ```pushq %rbp```
## ```movq %rsp, %rbp```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```movl %edi, %eax```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```cmpl %rsp, %rsi```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```je  .L0```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```movq %rdx, %r10```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```cltd```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```divl %esi```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 3|
| esi | 400|
| rsi | 10|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```movl %edx, (%r10)```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 0x85|
| esi | 400|
| rsi | 10|
| edx | 0x1|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

## ```popq %rbp```
## ```ret```
| Registers | Value |
| ----------- | ----------- |
| rsp | 10|
| eax | 0x85|
| esi | 400|
| rsi | 10|
| edx | 0x1|

| Addresses | Value |
| ----------- | ----------- |
| eax | 4|
| 2 | None|
| 3 | None|
| 4 | None|
| 5 | None|
| 6 | None|
| 7 | None|
| 8 | None|
| 9 | None|

###### Author: [Julian Castro](https://www.linkedin.com/in/julian-castro-7950aa1a7/) - castrojv@bc.edu

<h6>References: https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html</h6>