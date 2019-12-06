DEBUG = False

import math

if DEBUG:
    input_data = open("aoc2-1test.txt", "r")
else:
    input_data = open("aoc2-1.txt", "r")

input_data_lines = input_data.readline().split(",")

data_org = list()

for line in input_data_lines:
    data_org.append(int(line))

x=0
y=0

while True:
    data = data_org.copy()
    opcode_pos=0
    opcode=0
    print("test: ",x , "\t", y, end=" ")
    data[1] = x
    data[2] = y

    while True:
        try:
            opcode = data[opcode_pos]
            if opcode==99: 
                break
            a = data[data[opcode_pos+1]]
            b = data[data[opcode_pos+2]]
            if opcode==1:
                c = a + b
            elif opcode==2:
                c = a * b
            data[data[opcode_pos+3]] = c
            opcode_pos += 4
        except IndexError:
            print("E\t", end=" ")
            break
    
    if data[0]==19690720:
        print("\tIt's a hit!") 
        break
 
    print("\tfail")
    y+=1
    if y>99:
        y=0
        x+=1
    if x>99:
        print("fatal error")
        break




print(data)
print("Result of assignment: ")
print((100*data[1])+data[2])

####################
try:
    input_data.close()
except Exception:
    None

