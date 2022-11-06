# 8086-VM-on-Python
Intel 8086 'Virtual Machine' using Python

## Class and Method
__init__(self, trace=False)
run(self, code, ip)

## Example
```
from i8086 import i8086
vm = i8086(True) # turn trace on
vm.run(['MOV','ax','0xffff','ADD','ax','0xffff'],0)
```
![alt text](https://github.com/aderama2711/8086-VM-on-Python/blob/main/output.png)

## Implemented Opcode
- MOV REG VALUE
- ADD REG REG
- ADD REG VALUE

