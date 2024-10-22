"""
Написать итератор Zipper, конструктор которого принимает на вход список объектов
с методами step() и get_value().
- step всегда возвращает None и вызов этого метода выполняет 'шаг' последовательности
- get_value получает текущее значение последовательности

На каждом шаге итератор должен возвращать кортеж значений всех последовательностей.
"""
from itertools import islice

class Zipper:
    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return self

    def __next__(self):
        result = tuple(s.get_value() for s in self.sequence)
        for obj in self.sequence:
            obj.step()
        return result

class Fibonachi():
    def __init__(self):
        self.a = 0
        self.b = 1

    def step(self):
        self.a, self.b = self.b, self.b + self.a

    def get_value(self):
        return self.a

class NaturNumbers:
    def __init__(self):
        self.x = 0

    def step(self):
        self.x += 1

    def get_value(self):
        return self.x

fibo = Fibonachi()
natur = NaturNumbers()
# print(fibo.get_value())
zipper = Zipper([fibo, natur])
print(list(islice(zipper, 15)))

