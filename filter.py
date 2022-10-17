# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#import random
#lst = []
#for i in range(7):
#    lst.append(random.randint(0, 30))
#print(f'{lst} изначальный список')

#sum = 0
#for i in range(0, len(lst)):
#    if i % 2 != 0:
#        sum = sum + lst[i]
#print(f'Сумма элементов на нечетных позициях = {sum}')

import random
lst = []
for i in range(7):
    lst.append(random.randint(0, 30))
print(f'{lst} изначальный список')

def filter_position(lst):
    if (i % 2) != 0:
        return True
    else:
        return False

fil_lst = list(filter(filter_position, lst))
print(fil_lst)

sum = 0
for i in range(len(fil_lst)):
    sum += i
print(f'Сумма элементов на нечетных позициях = {sum}')