'''
Представьте, что существует маленький магазинчик фруктов, в котором работает всего один продавец. Он не помнит все
цены на товары и когда приходит покупатель, начинает искать цену в своем журнале. Это занимает довольно много времени,
 покупатели нервничают. Гораздо проще было бы, если бы у него был электронный каталог, куда бы он мог ввести название
  товара и получить всю информацию о нем из базы данных. В этом упражнении вам предстоит разработать такое приложение

src/product.py
Создайте класс Product, который будет представлять собой товар в нашем магазине. У товара есть уникальный идентификатор,
 название, описание и цена. Добавьте в класс необходимые свойства и методы по своему усмотрению

src/productDAO.py
Создайте класс ProductDAO, который предназначен для работы с таблицей товаров products. Создайте в классе метод, который
 будет получать из таблицы данные о товаре по его названию и возвращать объект товара. Считаем, что название товара в
  таблице уникально. Таблица имеет следующую структуру:

products

id - id товара
name - название товара
description - описание
price - цена
src/catalog.py
Сам каталог. В классе Catalog создайте метод get_product(), который возвращает информацию о товаре. Метод принимает
один параметр — название товара, строку. Метод должен вернуть словарь — полную информацию о товаре, который содержит
его идентификатор, название, цену и описание.
'''


class Product:
    def __init__(self, name, description, price, id=None):
        self.name = name
        self.description = description
        self.price = price
        self.id = id

#
# class Product:
#     def __init__(self, name, description, price):
#         self.id = None
#         self.name = name
#         self.description = description
#         self.price = price
#
#     def get_id(self):
#         return self.id
#
#     def get_name(self):
#         return self.name
#
#     def get_description(self):
#         return self.description
#
#     def get_price(self):
#         return self.price
#
#     def set_id(self, id):
#         self.id = id