# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

N = 10
array = [random.randint(0,10) for i in range(N)]
print(array)

min_ = min(array) # вставить код из 3 задачи
print(f'Минимальный элемент {min_}')
for i, item in enumerate(array):
    if item == min_:
        min_ind = i
        break

array_2 = array

array_2.remove(min_)
print(array_2)

min_2 = min(array_2)
for i, item in enumerate(array_2):
    if item == min_2:
        if i > min_ind:
            min_ind_2 = i+1
        else:
            min_ind_2 = i

print(f'В исходном массиве первый минимальный элемент {min_} имеет индекс {min_ind}, второй минимальый элемент(на самом деле последний из вторых) {min_2} '
      f'имеет индекс {min_ind_2} ')