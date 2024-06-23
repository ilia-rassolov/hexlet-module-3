### 00_pattern

Реализуйте функцию to_Klass(), которая принимает на вход словарь и возвращает объект типа Klass такой же структуры.

data = {
    'key': 'value',
    'key2': 'value2',
}
config = to_Klass(data)

config.key ## value
config.key2 ## value2
Подсказки
Вам понадобится функция setattr
user = User()
setattr(user, 'f', 'foo')
print(user.f) #=> foo
В пайтоне классы созданные лишь для хранения значений принято оборачивать в декоратор @dataclass
А чтобы не конфликтовать с зарезервированным именем class принято именовать через k

# 01.validation

Валидация - процесс проверки корректности данных. В вебе происходит всегда при отправке форм, например, регистрация на 
многих сайтах проверяет корректность введенного емейла, его уникальность (что такого пользователя ещё нет).

Каждый тип валидации в таких системах обычно представлен классом-валидатором, который принимает на вход опции и 
предоставляет интерфейс в виде функции validate. Эта функция принимает на вход то что проверяется (валидируется) 
и возвращает словарь с ошибками. Если словарь пустой, значит ошибок нет.

solution.py
Реализуйте класс PasswordValidator ориентируясь на тесты.

Этот валидатор поддерживает следующие опции:

min_len (по умолчанию 8) — минимальная длина пароля
contain_numbers (по умолчанию False) — требование содержать хотя бы одну цифру
Словарь ошибок в ключах содержит название опции, а в значении текст указывающий на ошибку

validator = PasswordValidator()
errors = validator.validate('qwerty1')
print(errors)  # => {'min_len': 'too small'}

options = {'contain_numbers': True}
validator = PasswordValidator(**options)
errors = validator.validate('qwerty')
print(errors)  # => {'min_len': 'too small', 'contain_numbers': 'should contain at least one number'}

# валидатор должен игнорировать несуществующие опции
validator = PasswordValidator(numberz=None)
errors = validator.validate('qwertya3sdf')
print(errors) # => {}

class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    # BEGIN (write your solution here)

    
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)

# 02.truncate

Для работы с текстом в вебе бывает полезна функция truncate(), которая обрезает слишком длинный текст и ставит в конце,
например, многоточие:

truncate('long text', {'length': 3})  ## lon...

Реализуйте класс Truncater с единственным методом truncate(). В классе уже присутствует конфигурация по умолчанию:

OPTIONS = {
    'separator': '...',
    'length': 200,
}
separator отвечает за символ(ы) добавляющиеся в конце, после обрезания строки, а length это длина до которой происходит
сокращение. Если строка короче или равна этой опции, то никакого сокращения не происходит. Конфигурацию по умолчанию 
можно переопределить передав новую при инициализации (она мержится с тем что в классе), а также через передачу 
конфигурации вторым параметром в метод truncate(). Оба этих способа можно комбинировать.

truncater = Truncater()
truncater.truncate('one two')  # one two
truncater.truncate('one two', length=6)  # one tw...
truncater2 = Truncater(length=6, separator='*')
truncater2.truncate('one two')  # one tw*

# 03.url

В данном упражнении вам предстоит реализовать класс Url, который позволяет извлекать из HTTP адреса, представленного 
строкой, его части.

Класс должен содержать методы:

__init__ — принимает на вход HTTP адрес в виде строки.

get_scheme() — возвращает протокол передачи данных.

get_hostname() — возвращает имя хоста.

get_query_params() — возвращает параметры запроса в виде пар ключ-значение объекта.

get_query_param() — получает значение параметра запроса по имени. Если параметр с переданным именем не существует,
метод возвращает значение заданное вторым параметром (по умолчанию равно None).

__eq__(self, other) — сравнивает два объекта класса Url и возвращает результат сравнения — True или False.

url = Url('http://hexlet.io:80?key=value&key2=value2')
url.get_scheme() # http
url.get_hostname() # hexlet.io
url.get_query_params()
# {
#  key: [value],
#  key2: [value2],
# }
url.get_query_param('key') # value
# второй параметр — значение по умолчанию
url.get_query_param('key2', 'lala') # value2
url.get_query_param('new', 'ehu') # ehu
url.get_query_param('new') # None
url == Url('http://hexlet.io:80?key=value&key2=value2') # True
url == Url('http://hexlet.io:80?key=value') # False
Подсказки
для парсинга url воспользуйтесь функциями urlparse и parse_qs из модуля urllib
__eq__

# 04.fluent_interface

Эту задачу можно решить огромным числом способов. Почти наверняка ваш способ будет не такой как решение учителя. 
Для отработки fluent interface в задаче используется класс Collection. Мы не даем никаких подсказок насчет того, 
какие функции нужно использовать. Как минимум вы знаете главную тройку map, filter и reduce. Их вполне достаточно, 
но можно и лучше если внимательно поизучать функции в модуле сollection.py.

data = [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 20}, {'name': 'Charlie', 'age': 30}]
c = Collection(data)
c.unique().all()

# [{'age': 30, 'name': 'Charlie'},
# {'age': 20, 'name': 'Bob'},
# {'age': 20, 'name': 'Alice'}]

c.unique().group_by(lambda row: (row['age'], row['name'])).all()
# [{30: ['Charlie']}, {20: ['Bob', 'Alice']}]

c.unique().group_by(lambda row: (row['age'], row['name'])).sort_by(lambda row: list(row.keys())).all()
# [{20: ['Bob', 'Alice']}, {30: ['Charlie']}]
solution.py
Реализуйте функцию format() которая принимает на вход список городов, производит внутри некоторые преобразования и 
возвращает структуру определенного формата.

Входные данные

raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]
Входная структура представляет из себя список городов, где каждый город это словарь с ключами name и country. 
Значения в этих ключах не нормализованы. Они могут быть в любом регистре и содержать начальные и концевые пробелы. 
Сами города могут дублироваться в рамках одной страны.

Результат

expected = [{'russia': ['moscow', 'samara']},
            {'turkey': ['antalia', 'istambul']},]
Конечная структура — словарь, в котором ключ это страна, а значение — список имен городов отсортированный по именам. 
Сама структура отсортирована по странам. Дублей городов в выходной структуре быть не должно, а сами страны и города 
должны быть записаны в нижнем регистре без ведущих и концевых пробелов.

Подсказки
1. для вывода промежуточных значений используйте метод .print()
2. 
from functools import reduce as _reduce


class Collection:
    def __init__(self, iterable):
        self.iterable = iterable

    def map_(self, func):
        return Collection(list(map(func, self.iterable)))

    def filter_(self, func):
        return Collection(list(filter(func, self.iterable)))

    def reduce_(self, func, acc=None):
        return Collection([_reduce(func, self.iterable, acc)])

    # возвращает коллекцию с уникальными значениями
    def unique(self):
        tuples = set(tuple(sorted(d.items())) for d in self.iterable)
        return Collection(list(dict(t) for t in tuples))

    # группирует коллекцию по указаному ключу
    def group_by(self, func):
        def reducer(acc, val):
            key, value = func(val)
            if key not in acc:
                acc[key] = []
            acc[key].append(value)
            return acc
        result_dict = _reduce(reducer, self.iterable, {})
        return Collection([{k: v} for k, v in result_dict.items()])

    # сортирует колекцию по ключу
    def sort_by(self, func):
        return Collection(sorted(self.iterable, key=func))

    def print(self):
        print(self.iterable)
        return Collection(self.iterable)

    def all(self):
        return list(self.iterable)

# 05.Booking

Booking — процесс бронирования чего-либо. В интернете существует множество сайтов, предлагающих бронирование машин, 
квартир, домов, самолётов и многого другого. Несмотря на то, что такие сайты предлагают разные услуги, букинг везде
работает почти идентично. Выбираются нужные даты и, если они свободны, производится бронирование.

solution.py
Реализуйте класс Booking, который позволяет бронировать номер отеля на определённые даты. Метод класса book() принимает 
на вход две даты в текстовом формате. Если бронирование возможно, то метод возвращает True и выполняет бронирование 
(даты записываются во внутреннее состояние объекта).

booking = Booking()
booking.book('2008-11-11', '2008-11-13')  # True
booking.book('2008-11-12', '2008-11-12')  # False
booking.book('2008-11-10', '2008-11-12')  # False
booking.book('2008-11-12', '2008-11-14')  # False
booking.book('2008-11-10', '2008-11-11')  # True
booking.book('2008-11-13', '2008-11-14')  # True
Подсказки
По обычаям гостиничного сервиса время заселения в номер — после полудня первого дня, а время выселения — до полудня 
последнего дня. Конкретные часы варьируются в разных отелях. Но в данной практике это не важно, главное понять принцип,
по которому указываются даты:

booking = Booking()

# забронировать номер на два дня
booking.book('2008-11-10', '2008-11-12')

# бронь невозможна, 11-го числа номер будет занят
booking.book('2008-11-11', '2008-11-15')

# бронь возможна, потому что 12-го числа номер освободится
booking.book('2008-11-12', '2008-11-13')

# бронь невозможна, съём, сроком менее одного дня, обычно не практикуется
booking.book('2008-11-17', '2008-11-17')

# бронь возможна, съём номера на один день
booking.book('2008-11-17', '2008-11-18')

from datetime import date














