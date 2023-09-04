# 💡 Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

import random

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


array = []
for i in range(10):
    array.append(random.randint(-100, 100))
print(array)

print(sort_list_declarative(array))