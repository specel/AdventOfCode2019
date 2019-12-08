range_bot = 108457
range_cei = 562041
numbers = set()

def check(value):
    adjacency, increasing = False, True
    x = [int(i) for i in str(value)]
    for i in range(5):
        if x[i]==x[i+1]:
            adjacency = True
            break
    for i in range(5):
        if x[i+1]<x[i]:
            increasing = False
    return adjacency & increasing


for number in range(range_bot, range_cei):
    if check(number):
        numbers.add(number)

print(numbers.__len__())



    

