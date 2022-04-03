# Assembly Commands from File (copy and paste to https://stackedit.io/app#(

## pushq %rbp
<strong>Assembly Command<strong>: Push register %rbp on stack
<strong>Bytes<strong>: q == 8 bytes
> The push instruction places its operand onto the top of the hardware supported stack in memory. Specifically, push first decrements ESP by 4, then places its operand into the contents of the 32-bit location at address (%esp). ESP (the stack pointer) is decremented by push since the x86 stack grows down — i.e. the stack grows from high addresses to lower addresses.
![image](url)

## movq %rsp, %rbp
<strong>Assembly Command<strong>: Move register in %rsp, to register in %rbp
<strong>Bytes<strong>: q == 8 bytes
> The mov instruction copies the data item referred to by its first operand (i.e. register contents, memory contents, or a constant value) into the location referred to by its second operand (i.e. a register or memory). While register-to-register moves are possible, direct memory-to-memory moves are not. In cases where memory transfers are desired, the source memory contents must first be loaded into a register, then can be stored to the destination memory address.
![image](https://i.ytimg.com/vi/0_r-3eWB54c/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDlD2i6F3GA6o1dmrfPnUxHj0nsfw)

## movl %edi, %eax
<strong>Assembly Command<strong>: Move register in %edi, to register in %eax
<strong>Bytes<strong>: l == 4 bytes
> The mov instruction copies the data item referred to by its first operand (i.e. register contents, memory contents, or a constant value) into the location referred to by its second operand (i.e. a register or memory). While register-to-register moves are possible, direct memory-to-memory moves are not. In cases where memory transfers are desired, the source memory contents must first be loaded into a register, then can be stored to the destination memory address.
![image](https://i.ytimg.com/vi/0_r-3eWB54c/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDlD2i6F3GA6o1dmrfPnUxHj0nsfw)

## movq %rdx, %r10
<strong>Assembly Command<strong>: Move register in %rdx, to register in %r10
<strong>Bytes<strong>: q == 8 bytes
> The mov instruction copies the data item referred to by its first operand (i.e. register contents, memory contents, or a constant value) into the location referred to by its second operand (i.e. a register or memory). While register-to-register moves are possible, direct memory-to-memory moves are not. In cases where memory transfers are desired, the source memory contents must first be loaded into a register, then can be stored to the destination memory address.
![image](https://i.ytimg.com/vi/0_r-3eWB54c/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDlD2i6F3GA6o1dmrfPnUxHj0nsfw)

## cltd
<strong>Assembly Command<strong>: Convert long to double; moves sign bit of (%eax) to %edx
> The ret instruction implements a subroutine return mechanism. This instruction first pops a code location off the hardware supported in-memory stack (see the pop instruction for details). It then performs an unconditional jump to the retrieved code location.

## idivl %esi
<strong>Assembly Command<strong>: Divide value in (%eax) to value in %esi
<strong>Bytes<strong>: l == 4 bytes
> The idiv instruction divides the contents of the 64 bit integer EDX:EAX (constructed by viewing EDX as the most significant four bytes and EAX as the least significant four bytes) by the specified operand value. The quotient result of the division is stored into EAX, while the remainder is placed in EDX.
![image](url)

## movl %edx, (%r10)
<strong>Assembly Command<strong>: Move register in %edx, to value in (%r10)
<strong>Bytes<strong>: l == 4 bytes
> The mov instruction copies the data item referred to by its first operand (i.e. register contents, memory contents, or a constant value) into the location referred to by its second operand (i.e. a register or memory). While register-to-register moves are possible, direct memory-to-memory moves are not. In cases where memory transfers are desired, the source memory contents must first be loaded into a register, then can be stored to the destination memory address.
![image](https://i.ytimg.com/vi/0_r-3eWB54c/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDlD2i6F3GA6o1dmrfPnUxHj0nsfw)

## popq %rbp
<strong>Assembly Command<strong>: Pop register %rbp from stack
<strong>Bytes<strong>: q == 8 bytes
> The pop instruction removes the 4-byte data element from the top of the hardware-supported stack into the specified operand (i.e. register or memory location). It first moves the 4 bytes located at memory location (%esp) into the specified register or memory location, and then increments ESP by 4.
![image](url)

## ret
<strong>Assembly Command<strong>: Return
> These instructions implement a subroutine call and return. The call instruction first pushes the current code location onto the hardware supported stack in memory (see the push instruction for details), and then performs an unconditional jump to the code location indicated by the label operand. Unlike the simple jump instructions, the call instruction saves the location to return to when the subroutine completes.

