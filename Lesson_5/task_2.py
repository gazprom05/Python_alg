from collections import deque

def sum_(a1,b1):
    n = max(len(a1), len(b1))
    a1.reverse()
    b1.reverse()
    print(a1)
    print(b1)
    print(n, '_________________')
    for i in range(n):
        print(a1[i])




a = input('Введите шестнадцатиричное число')
b = input('Введите шестнадцатиричное число')
a1 = deque(a)
b1 = deque(b)
print(a1)
print(b1)


while True:
    action = input('Введите + если хотите сложить числа, * - если умножить')
    if action == '+':
        sum_(a1, b1)
        break
    elif action == '*':
        mult_(a1, b1)
        break
    else:
        print('Try one more time')