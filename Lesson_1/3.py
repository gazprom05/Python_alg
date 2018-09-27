print('Введите координаты 2 точек x1, y1, x2, y2')
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dot_1 = [x1, y1]
dot_2 = [x2, y2]

A = dot_1[1] - dot_2[1]
B = dot_2[0] - dot_1[0]
c = dot_1[0] * dot_2[1] - dot_2[1] * dot_1[1]
print(f'Уравнение4 прямой {A}x + {B}y + {c} = 0')