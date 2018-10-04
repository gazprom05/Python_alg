# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import  random

N = 20
array = [random.randint(-10,10) for i in range(N)]
print(array)

max_otr = -10

for i in array:
    if i < 0:
        if i > max_otr:
            max_otr = i

for i, item in enumerate(array):
    if item == max_otr:
        pos = i
        break
print(f' Максимальный отрицательный элемент {max_otr} стоит на позиции {pos}')