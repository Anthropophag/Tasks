import random

numbers = [random.randint(0, 1000) for i in range(random.randint(0, 1000))]
new_numbers = [i for i in numbers
               if i % 3 == 0 and
               i > 0 and
               i % 4 != 0]
print(numbers)
print(new_numbers)















