# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


import random

N = 10
array = [random.randint(0,10) for i in range(N)]
print(array)

summ = 0
max_ = max(array) # вставить код из 3 задачи
min_ = min(array) # вставить код из 3 задачи


for i, item in enumerate(array):
    if item == max_:
        max_ind = i
    if item == min_:
        min_ind = i

print(f'Максимальный элемент {max_} имеет индекс  {max_ind}')
print(f'Минимальный элемент {min_} имеет индекс  {min_ind}')


for i, item in enumerate(array):
    if min_ind < max_ind:
        if i > min_ind and i < max_ind:
            print(item, end = "  ")
            summ += item
    else:
        if i < min_ind and i > max_ind:
            print(item, end="  ")
            summ += item
print()
print(f'Сумма =  {summ}')