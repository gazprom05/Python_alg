# coding: utf-8

import random

print('Введите 2 целых числа')
a = int(input())
b = int(input())
rand1 = random.randint(a+1,b-1)
print(f'Случайное число {rand1}')

print('Введите 2 вещественных числа')
c = float(input())
d = float(input())
rand2 = random.uniform(c, d)
print(f'Случайное число {rand2}')

print('Введите 2 символа')
e = input()
f = input()
e1 = ord(e)
e2 = ord(f)
if e1 > e2:
    rand3 = chr(random.randint(e2, e1))
else:
    rand3 = chr(random.randint(e1, e2))

print(f'Случайый символ {rand3}')