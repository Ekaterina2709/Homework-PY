# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n 
# и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

N = int(input('Введите число N '))
s = 0
A = []
for i in range(1, N + 1):
    s += (1 + 1 / i) ** i
    print(f'{i} = > {s}')
    A.append(s)
print(A)
