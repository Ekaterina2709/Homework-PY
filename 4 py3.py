3) Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 7, 2, 6, 3, 4, 5, 8, 1, 2, 9, 4, 1]
print(f'Исходный список {numbers}')
new = []
for i in set(numbers):
    if numbers.count(i) == 1:
        new.append(i)
print(f'Новый список {new}')
    
