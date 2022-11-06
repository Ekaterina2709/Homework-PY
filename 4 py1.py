# 1) Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

N = input("Введите вещественное число :")
d =  input("Задайте точность округления:")
num = Decimal(N)
num = num.quantize(Decimal(d))
print(f'Число с заданной точностью {d} равно {num}')
