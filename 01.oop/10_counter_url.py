"""
Написать класс Counter, считающий количество посещений по-заданному url:
- Конструктор класса принимает строку с url в качестве аргумента
- Метод inc() увеличивает счетчик, соответствующий url, на 1
- Метод get() возвращает словарь с количеством посещений по всем url (включая те, которые
  определены в других counter).
"""
from collections import defaultdict


class Counter:
    def __init__(self, url):
        self.url = url
        self.counter = defaultdict(int)

    def inc(self):
        self.counter[self.url] += 1

    def get(self):
        return dict(self.counter)


counter_yandex = Counter('www.yandex.ru')
counter_google = Counter('www.google.com')
counter_yandex.inc()
counter_yandex.inc()
counter_google.inc()
print(counter_yandex.get())
print(counter_google.get())
