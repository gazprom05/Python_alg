print('Введит длины 3 отрезков')
a = int(input())
b = int(input())
c = int(input())
if a < (b + c) and b < (a + c) and c < (a + b):
    if a == b:
        if a == c:
            print('Треугольник равносторонный')
        else:
            print('Треугольник равнобедренный')
    else:
        if a == c:
            print('Треугольник равнобедренный')
        else:
            if b == c:
                print('Треугольник равнобедренный')
            else:
                print('Треугольник самый обыкновенный')
else:
    print('Треугольник не получится')