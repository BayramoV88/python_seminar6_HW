# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input('Введите число: '))

i = 2
lst = []

while i <= num:
    if num % i == 0:
        lst.append(i)
        num = num // i
        #i = 2
    else:
        i += 1
print(f'список простых множителей - {lst}')

n = int(input('Введите число: '))

i = 2

lst = [num //= i if num % i == 0 for i in range(n)]
print(lst)

