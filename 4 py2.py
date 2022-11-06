 2) Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
#  Используем Решето Эратосфена

N = int(input("Введите число натуральное чиcло N:"))
lst = [1] * (N + 1)
lst[0] = 0
lst[1] = 0
spi = []
res = []
for i in range(2, N + 1):
    if lst[i]:
        for j in range(2 * i, N + 1, i):  
            lst[j] = 0
for i in range(1, N+1):
    if lst[i]:
        spi.append(i)
print(f'Список простых множителей:{spi}')
tmp = N
i =  0
while tmp>1:
    if tmp%spi[i]==0:
        tmp /= spi[i]
        res.append(spi[i])     
    elif N == 1:
        break
    else:
        i +=1
print(f'Число {N} входит в список простых' if len(res) == 1 else f'Простые множители числа: {res}')            
