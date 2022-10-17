# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

#num = int(input('Введите число: \n'))
#factorial = 1
#for i in range(1, num + 1):
#    factorial *= i
#    print(factorial, end = ',')

num = int(input('Введите число: \n'))
def f(x):
    if x==1:
        return 1
    else:
        return x * f(x-1)

lst = [f(i) for i in range(1, num + 1)]
print(lst, end=',')