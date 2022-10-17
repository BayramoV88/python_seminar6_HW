#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

#lst = [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]
#print(f'{lst} - исходный список')

#new_lst = []
#for i in lst:
#    if i in new_lst:
#        continue
#    else:
#        new_lst.append(i)
#print(f'{new_lst} - новый список')

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")