# 4. Определить, какое число в массиве встречается чаще всего.

import  random

N = 20
array = [random.randint(0,9) for i in range(N)]
print(array)
array_2 = [0] * N
print(array_2)

for i, item in enumerate(array):
    for j in array:
        if item == j:
            array_2[i] += 1

print(array_2)

print(f'Число {array[max(array_2)]} встречается {max(array_2)} раз(а)')