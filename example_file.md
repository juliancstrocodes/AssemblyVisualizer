# Assembly File Visualization
#### Your parameters and the random arguments we used:

__dividend__ --> 1075155568

__divisor__ --> 3090297396

__remainder__ --> 0xfec3f3cd3cac2f85

## ```pushq %rbp``` 
## ```movq %rsp, %rbp``` 
<h4>Opened up the stack frame</h4>

## ```movl %edi, -20(%rbp)``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|

## ```movl %esi, -24(%rbp)``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|

## ```movq %rdx, -32(%rbp)``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|

## ```movl -20(%rbp), %eax``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| eax | -20|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|

## ```cltd``` 
## ```idivl -24(%rbp)``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| eax | 0x1|
| edx | -0x4|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|

## ```movl %eax, -4(%rbp)``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| eax | 0x1|
| edx | -0x4|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|
| rbp | 0x1|

## ```movl -20(%rbp), %eax``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| eax | -20|
| edx | -0x4|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|
| rbp | 0x1|

## ```movq -32(%rbp), %rax``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| rax | -32|
| eax | -20|
| edx | -0x4|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|
| rbp | 0x1|

## ```movl %edx, (%rax)``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| rax | -32|
| eax | -20|
| edx | -0x4|
| None | -0x4|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|
| rbp | 0x1|

## ```movl -4(%rbp), %eax``` 
| Registers | Value |
| ----------- | ----------- |
| rbp | 0|
| rax | -32|
| eax | -4|
| edx | -0x4|
| None | -0x4|

| Addresses | Value |
| ----------- | ----------- |
| -20 | 1075155568|
| -24 | 3090297396|
| -32 | 0xfec3f3cd3cac2f85|
| rbp | 0x1|

## ```popq %rbp``` 
<h4>Closed up the stack frame</h4>

## ```ret``` 
###### Author: [Julian Castro](https://www.linkedin.com/in/julian-castro-7950aa1a7/) - castrojv@bc.edu

<h6>References: https://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html</h6>