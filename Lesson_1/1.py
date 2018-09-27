# coding: utf-8

print('Введите трёхзначное число')
n = int(input())
print(n)
a = n // 100
b = (n // 10) % 10
c = n % 10

sum = a + b + c
mult = a * b * c

print(f'сумма цифр {sum}, произведение {mult}')