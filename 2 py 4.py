# 4 – Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
N = int(input('Введите число N: '))
rnd = []
new = []
for i in range(N):
    rnd.append(randint(-N, N + 1))
print(f'Сформированный список{rnd}')
with open('file.txt','r') as fil:
    for line in fil:
        if -len(rnd)<= int(line)< len(rnd):
            new.append(rnd[int(line)])
print(f'Выбранные элементы по заданным индексам {new}')
