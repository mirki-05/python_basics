"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input("Enter number: ")
nn = n + n
nnn = n + n + n

print (f"n+nn+nnn = ", str(int(n) + int(nn) + int(nnn)))