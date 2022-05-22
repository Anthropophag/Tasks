import random

numbers = []
for i in range(random.randint(0, 1000)):
    numbers.append(random.randint(0, 1000000))

for ind in range(len(numbers)):
    numbers[ind] = numbers[ind] ** 2
print(numbers)

















