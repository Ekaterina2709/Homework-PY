Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
 Пример:
для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k = int(input('Введите целое положительное число '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


fibon = [0]
for e in range(1, k+1):
    fibon.append(fib(e))
neg_fib = []
for i in range(k, 0, -1):
    neg_fib.append(str((-1)**(i+1)*fibon[i]))
print(neg_fib+fibon)
