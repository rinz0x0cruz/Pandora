from pwn import *
context.arch = 'amd64'

my_sc = asm("""
	mov rax,0x60
	mov rdi,0x1337
	syscall
""")

print(my_sc)
