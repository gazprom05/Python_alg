import random
import cProfile

def try_1(N):
    matrix = [[random.randint(0, 100) for _ in range(N)] for _ in range(N * 2)]

    # for line in matrix:
    #     print(*line, sep='\t')

    max_ = float('-inf')

    for j in range(len(matrix[0])):
        min_ = matrix[0][j]

        for i in range(len(matrix)):
            if matrix[i][j] < min_:
                min_ = matrix[i][j]

        if min_ > max_:
            max_ = min_

    print(f'Max in min = {max_}')




def try_2(N):
    array = [[random.randint(0, 100) for _ in range(N)] for _ in range(N * 2)]
    # for line in array:
    #     print(line)
    # print('-' * 10)
    array_2 = tuple(zip(*array[::]))

    # for line in array_2:
    #     print(line)

    max_ = 0

    for i in array_2:
        if min(i) >max_:
            max_ = min(i)

    print(f'максимальный элемент среди минимальных элементов столбцов матрицы {max_}')


N = 10000
cProfile.run('try_1(N)')  #1053476377 function calls in 231.816 seconds
print('_' * 50)
print('*' * 50)    # переворот матрицы оказался быстрее, но разница не велика
print('_' * 50)
cProfile.run('try_2(N)') #1053473848 function calls in 228.916 seconds