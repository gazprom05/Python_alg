import timeit
import random
import cProfile


def try_1(M,N):
    matrix = []
    for i in range(N):
        row = []
        summ = 0
        # print(f'{i}-я строка!!!')

        for j in range(M - 1):
            num = random.randint(0,9)
            summ += num
            row.append(num)

        row.append(summ)
        matrix.append(row)

    # for line in matrix:
    #     print(line)



def try_2(M,N):
    def line(M,N):
        a = []
        sum_ = 0
        for i in range(M):
            if i < N:
                n = random.randint(0,9)
                a.append(n)
                sum_ += n
            if i == N:
                a.append(sum_)
        # print('Строка заполнена')
        return a

    array = []
    m = 0
    while m < N:
        m += 1
        array.append(line(M,N))

    # for line_ in array:
    #     print(line_)

M = 5000
N = 4000

cProfile.run('try_1(M,N)')  #131981365 function calls in 29.857 seconds
print('_' * 20)
cProfile.run('try_2(M,N)')  #105613036 function calls in 24.576 seconds
#
# print(timeit.timeit(try_1()))