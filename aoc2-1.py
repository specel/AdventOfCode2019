DEBUG = False

import math

if DEBUG:
    input_data = open("aoc2-1test.txt", "r")
else:
    input_data = open("aoc2-1.txt", "r")

input_data_lines = input_data.readline().split(",")

data = list()

for line in input_data_lines:
    data.append(int(line))

print(data)

opcode_pos=0
opcode=0

if not DEBUG:
    data[1] = 12
    data[2] = 2
    print(data)



while True:
    opcode = data[opcode_pos]

    if opcode==99: break

    a = data[data[opcode_pos+1]]
    b = data[data[opcode_pos+2]]
    if opcode==1:
        c = a + b
    elif opcode==2:
        c = a * b
    
    c_pos = data[opcode_pos+3]
    data[c_pos] = c

    opcode_pos += 4

print(data)

####################
try:
    input_data.close()
except Exception:
    None

