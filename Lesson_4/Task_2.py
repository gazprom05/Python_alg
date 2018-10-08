# # Первая функция написана мной, вторая версия скопирована с интернета и доработана в плане вывода.
# Правда, я сравниваю два решета=(

import cProfile

def resheto(n,c):
    array = [0] * n
    for i in range(2, n):
            array[i] = i
    array.pop(0)
    array.pop(0)
    # print(array)
    p = 2
    j = 0
    num_ = 0
    result = []
    while True:
        for i, item in enumerate(array):
            if item % p == 0 and item != p:
                array[i] = 0
        for i, item in enumerate(array):
            if item > p:
                p = item
                break
        # print(f'Выход, p = {p}')
        j += 1
        if j == c:
            break
    # print(array)
    for i in array:
        if i > 0:
            result.append(i)
    # print(result)
    print(f'Искомое число с номером {c} это {result[c-1]}')





def resheto_2(n,c):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    print(f'Искомое число с номером {c} это {b[c-1]}')

    del a

n = 1000000 # int(input('Введите длину ряда'))

c = 50 #int(input('введите порядковый номер искомого числа'))



cProfile.run('resheto(n,c)')      # 100552 function calls in 4.404 seconds    Зато сам))
print('_'*50)
cProfile.run('resheto_2(n, c)')   #78503 function calls in 0.389 seconds



