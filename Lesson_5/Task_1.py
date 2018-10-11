from collections import Counter, defaultdict, namedtuple
import random


New_firm = namedtuple('New_firm', ['name', 'kv_1', 'kv_2', 'kv_3', 'kv_4', 'sum_'])
n = 3 #int(input('Введите число фирм'))
year_sum = 0
mid_year_sum = 0
mid_year_sum_temp = 0
firm_list = []
for i in range(n):
    name = input('Введите название фирмы')
    kv_1 = random.randint(0,9)#int(input('введите прибыль 1го квартала'))
    kv_2 = random.randint(0,9)# int(input('введите прибыль 2го квартала'))
    kv_3 = random.randint(0,9)# int(input('введите прибыль 3го квартала'))
    kv_4 = random.randint(0,9)# int(input('введите прибыль 4го квартала'))
    sum_ = kv_1 + kv_2 + kv_3 + kv_4
    firm_list.append(New_firm(name, kv_1, kv_2, kv_3, kv_4, sum_))
    mid_year_sum += sum_

for i in firm_list:
    print(i)
print(f'Среднегодовая выручка всех фирм =  {mid_year_sum / n}')

looser = []
winner = []

for i in range(len(firm_list)):
    print(firm_list[i].sum_)
    if firm_list[i].sum_ < (mid_year_sum / n):
        looser.append(firm_list[i].name)
    else:
        winner.append(firm_list[i].name)

print(f'Плохие фирмы {looser}')
print(f'Хорошие фирмы {winner}')

#
#



