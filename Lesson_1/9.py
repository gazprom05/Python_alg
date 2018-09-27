print('введите 3 числа')
a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        if b > c:
            print(f'Среднее число {b}')
        else:
            print(f'Среднее число {c}')
    else:
        print(f'Среднее число {a}')
else:
    if a > c:
        print(f'Среднее число {a}')
    else:
        if b > c:
            print(f'Среднее число {c}')
        else:
            print(f'Среднее число {b}')