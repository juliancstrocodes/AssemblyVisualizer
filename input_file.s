	.file	"div.c"
	.text
	.globl	div_qr
	.type	div_qr, @function
div_qr:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, %eax
	cmpl	%rsp, %rsi
	je		.L0
	movq	%rdx, %r10
	cltd
	divl	%esi
	movl	%edx, (%r10)
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	div_qr, .-div_qr
	.ident	"GCC: (GNU) 4.8.5 20150623 (Red Hat 4.8.5-44)"
	.section	.note.GNU-stack,"",@progbits
