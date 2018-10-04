# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

array = [i for i in range(2,100)]
print(array)

n = [i for i in range(2,10)]
print(n)

result = [0] * 8

for i in array:
   for j in n:
       if i % j == 0:
           result[j-2] += 1

print(result)

for i in range(0,8):
    print(f'Цифре {n[i]} кратно {result[i]} чисел')