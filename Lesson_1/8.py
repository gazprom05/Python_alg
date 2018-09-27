print('Введите год')
year = int(input())
n = year % 4
if n == 0:
    print('Год високосный')
else:
    print('Год не високосный')