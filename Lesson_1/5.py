print('Введите 2 символа')
a = input()
b = input()
num_a = ord(a) - 96
num_b = ord(b)- 96
n = abs(num_a - num_b)

print(f'порядковый номер первого символа {num_a}')
print(f'порядковый номер второго символа {num_b}')
print(f'расстояние между ними {n}')