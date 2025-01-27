'''
Дано неотрицательное целое число x, вернуть квадратный корень округленного вниз до ближайшего целого числа .
Возвращаемое целое число также должно быть неотрицательным .
Не допускается использование встроенных функций или операторов экспоненты.
Например, не используйте pow(x, 0.5)в C++ или x ** 0.5Python.

Пример 1:
Ввод: x = 4
 Вывод: 2
 Пояснение: Квадратный корень из 4 равен 2, поэтому мы возвращаем 2.
Пример 2:
Ввод: x = 8
 Вывод: 2
 Пояснение: Квадратный корень из 8 равен 2,82842..., и поскольку мы округляем его до ближайшего целого числа,
  возвращается 2.
'''

def sqrt(x):
    if x == 1:
        return 1
    def inner(high, low):
        if low ** 2 > x:
            return inner(low, low // 2)
        elif high ** 2 <= x < (high + 1) ** 2:
            return high
        elif low ** 2 <= x < (low + 1) ** 2:
            return low
        medium = (high + low) // 2
        if medium ** 2 > x:
            return inner(medium, low)
        else:
            return inner(high, medium)
    return inner(x // 2, x // 4)

lst = [0,1,2,3,4,5,6,7,8,100,1000,100000,21354357467, 100]
print(list(map(lambda x: sqrt(x), lst)))
print(list(map(lambda x: int(x ** 0.5), lst)))





