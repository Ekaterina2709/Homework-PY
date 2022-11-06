 4) Задана натуральная степень k. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0

from random import randint
k = int(input('Введите натуральную степень k:'))
kof = [randint(0, 100) for i in range(k+1)]
poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(kof) if j][::-1])
# Поиск и замены:
poly = poly.replace('x^1', 'x')
poly = poly.replace('x^0', '')
print(kof)
print(f'Степень многочлена, тождественно равного нулю, не определена' if k == 0 else f'{poly}=0')
