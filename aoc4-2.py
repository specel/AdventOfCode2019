range_bot = 108457
range_cei = 562041
numbers = set()
counter_empty = dict()
for i in range(10):
    counter_empty[i] = 0


def check(value):
    adj, group, increasing = False, True, True
    counter = counter_empty.copy()
    x = [int(i) for i in str(value)]
    for i in range(5):
        if x[i]==x[i+1]:
            adj = True
            break
    for i in x:
        counter[i] += 1
    if max(counter.values())>2:
        group = False
    for i in counter.values():
        if i==2:
            group = True
        
    for i in range(5):
        if x[i+1]<x[i]:
            increasing = False
    return adj & increasing & group


#testy        [True,   False,  True,   False,  False]
test_values = (112233, 123444, 111122, 111222, 123334)
tests = [check(value) for value in test_values]
print(tests)

for number in range(range_bot, range_cei):
    if check(number):
        numbers.add(number)

print(numbers.__len__())


