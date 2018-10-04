# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

array = [[1,2,3,6],
         [2,6,2,6],
         [3,7,1,8],
         [6,6,8,1]
]
for line in array:
    print(line)
print('-' * 10)
array_2 = tuple(zip(*array[::]))

for line in array_2:
    print(line)

max_ = 0

for i in array_2:
    if min(i) >max_:
        max_ = min(i)

print(f'максимальный элемент среди минимальных элементов столбцов матрицы {max_}')