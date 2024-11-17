'''
Представьте себе типичную ситуацию из боевиков, где правительственный агент пытается выяснить владельца автомобиля, участвующего погоне. В процессе он вводит номер автомобиля в компьютерную программу и получает нужную ему информацию. В этом упражнении мы разработаем похожее приложение, которое по номеру автомобиля позволит нам узнать всю информацию о его владельце

scr/user.py
Класс User, представляет собой владельца автомобиля. У пользователя есть уникальный идентификатор, имя, фамилия, адрес и список принадлежащих ему автомобилей.

scr/car.py
Класс Car, представляет автомобиль. У автомобиля есть уникальный идентификатор, производитель, модель, номер(строка), цвет и владелец. Добавьте в класс необходимые свойства и методы по своему усмотрению. Владелец автомобиля связан с автомобилями связью один-ко-многим через уникальный идентификатор пользователя.

scr/carDAO.py
Создайте в классе CarDAO метод, который будет получать из базы все данные об автомобиле, включая информацию о его владельце.

Структура таблиц:

users

id - id владельца
first_name - имя
last_name - фамилия
address - адрес
cars

id - id автомобиля
user_id - id владельца
manufacturer - производитель автомобиля
model - модель
plate - регистрационный номер
color - цвет
scr/car_base.py
Создайте класс CarBase, описывающий базу данных автомобилей. В нем создайте метод get_info(), который возвращает информацию об автомобиле. Метод принимает один параметр — номер автомобиля, строку. Метод должен вернуть словарь — полную информацию об автомобиле, включая информацию о владельце.

Если такого автомобиля в базе данных нет, метод должен выбросить исключение KeyError
'''
from dataclasses import dataclass, field
from typing import List, Optional

from cars import Car


@dataclass
class User:
    first_name: str
    last_name: str
    address: str
    id: Optional[int] = None
    cars: List[Car] = field(default_factory=list)

    def add_car(self, car: Car):
        self.cars.append(car)
