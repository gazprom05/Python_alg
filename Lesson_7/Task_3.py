import random

m = int(input('Введите  число, характеризующее длину ряда'))
n = 2 * m + 1
array = [random.randint(-100,100) for i in range(n)]
print(array)
temp = 0
arr_1 = []
arr_2 = []
temp = array[random.randint(0, len(array))]
print(temp)

for i in range(len(array)):
    while i < len(array):
        if

