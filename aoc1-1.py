import math
data = open("aoc1-1.txt", "r")
output = open("aoc1-1_result.txt", "w")
sum = 0

for line in data.readlines():
    x = int(line)
    x = math.floor(x/3)
    x = x-2
    #output.write(str(x)+"\n")
    sum += x

output.write(str(sum))
print(sum)
data.close()
output.close()
