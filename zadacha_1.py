# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

'''text = input("Введите текст:\n")
print(f"Исходный текст: {text}")
new_text = "абв"
lst = [i for i in text.split() if new_text not in i]
print(f'Результат: {" ".join(lst)}')
'''
from math import *

for a in range(150):
    for b in range(150):
        for c in range(150):
            for d in range(150):
                for e in range(150):
                    if (pow(a,5)+pow(b,5)+pow(c,5)+pow(d,5) == pow(e,5)) and (a>2, b>2, c>2, d>2, e>2):
                        print(a,b,c,d,e)
print(a+b+c+d+e)