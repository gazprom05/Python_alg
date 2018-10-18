import random

N = 100
array = [random.randint(-100,100) for i in range(N)]
print(array)
n = 1
while n < len(array):
    for i in range(len(array)-n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
        elif array[i] == array[i + 1]: #самодеятельность, которая иногда вылетает из-за ощибки индексов в 9 строке
            array.pop(i) #if array[i] > array[i + 1]: IndexError: list index out of range
        n += 1
print(array)