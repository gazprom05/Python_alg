# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число
#  и сумму его цифр.

n = input('Введите количество чисел')
nums = []
max = 0

print('Введите числа')

for i in range(0,int(n)):
    nums.append(input('Вводите!'))

for i in range(0, len(nums)):
    num = int(nums[i])
    summ = 0
    while num > 0:
        d = num % 10
        num = num // 10
        summ += d
    if summ > max:
        max = summ
        max_num = nums[i]
print(f'Максимальная сумма цифр({max}) у числа {max_num}')



