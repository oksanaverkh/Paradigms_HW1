# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random

def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[len(numbers)-1-i] == max(numbers):
                break
            elif numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


array = []
for i in range(10):
    array.append(random.randint(-100, 100))
print(array)

print(sort_list_imperative(array))
