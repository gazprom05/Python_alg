# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

N = 10
array_1 = [random.randint(1,N) for i in range(10)]
print(array_1)

max_ = 0
min_ = N
for i in range(len(array_1)):
    if array_1[i] > max_:
        max_ = array_1[i]
        max_index = i
    if  array_1[i] < min_:
        min_ = array_1[i]
        min_index = i

print(f' минимальный элемент {min_}')
print(f' максимальный элемент {max_}')


array_1[min_index], array_1[max_index] = array_1[max_index], array_1[min_index]
print(array_1)

#  при наличии нескольких макс/мин. элементов программа меняет местами последние встретившиеся
