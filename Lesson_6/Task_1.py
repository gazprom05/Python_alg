# coding: utf-8

# Урок 2, задание 4.# Win 10 x64
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.

import sys
import turtle
import random
import math

def pamyat(n):
    memory = int(sys.getsizeof(n))
    i = 0
    memory += int(sys.getsizeof(i))
    summ = 0
    memory += int(sys.getsizeof(summ))
    count = 1
    memory += int(sys.getsizeof(count))
    if n > 11:
        turtle.speed(0)
    while i < n:
        summ += count
        memory += int(sys.getsizeof(summ))
        count /= (-2)
        memory += int(sys.getsizeof(count))
        i += 1
        memory += int(sys.getsizeof(i))
        turtle.screensize(canvwidth = memory * 4 , canvheight = memory * 3 , bg = None)

    turtle.goto(n, memory)
    turtle.getscreen()
    turtle.circle(10)
    turtle.write(f'Для {n} элементов требуется {memory}кб памяти', font=("Arial", 18, "normal"))


def ask():
    ans = turtle.textinput("Выходим? Если нет, то n*10", "Y")
    return ans


n = 1
turtle.shape('turtle')
turtle.color('blue')
answer = ''
turtle.goto(0, 0)
turtle.circle(10)
while answer != 'N':
    answer = ask()
    if answer == 'Y':
        break
    else:
        pamyat(n)
        n *= 10
else:
    print(f'ряд состоит из {n} элементов, суумаа элементов ряда {summ}, памяти заняло {memory} кб')






