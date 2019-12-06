DEBUG = False

import math

if DEBUG:
    input_data_lines = ["100756",]
else:
    input_data = open("aoc1-1.txt", "r")
    input_data_lines = input_data.readlines()

sum = 0
sum_modules = 0

for line in input_data_lines:
    x = int(line)
    x = math.floor(x/3)
    x = x-2
    sum += x

    while True:
        x = math.floor(x/3) - 2
        if x <= 0:
            break
        sum_modules += x

print(sum)
print(sum_modules)

print(sum+sum_modules)

try:
    input_data.close()
except Exception:
    None

