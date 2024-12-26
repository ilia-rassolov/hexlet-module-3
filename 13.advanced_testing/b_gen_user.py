'''Протестируйте функцию, которая генерирует случайного пользователя. В этом случае пользователь — это словарь с
 тремя полями:

email
first_name
last_name
Для генерации данных используется библиотека Faker:

from functions import get_function
build_user = get_function()

print(build_user())
# => {'email': 'Zion.Reichel12@yahoo.com', 'first_name': 'Elizabeth', 'last_name': 'Zulauf'}
Если какой-то из параметров нужно задать точно, то его можно передать в функцию:

from functions import get_function
build_user = get_function()

print(build_user({'first_name': 'Petya'}))
# => {'email': 'Zion.Reichel12@yahoo.com', 'first_name': 'Petya', 'last_name': 'Zulauf'}
Вам нужно протестировать три ситуации:

Вызов build_user() возвращает словарь нужной структуры
Вызов build_user() возвращает словарь с отличными от предыдущего вызова данными
Установка полей пользователя через переданные параметры в словаре работает верно
Подсказки
Чтобы проверить соответствие словаря, заданным требованиям можно воспользоваться библиотекой schema:

from schema import Schema

schema = Schema({
    'name': str,
    'age': int
})

schema.is_valid({'name': 'Nikolay', 'age': 20}) # True
schema.is_valid({'name': 'Nikolay'}) # False '''

from schema import Schema
from b_func import get_function

build_user = get_function()


# BEGIN (write your solution here)
def test_build_user_schema():
    user = build_user
    schema = Schema({
        'first_name': str,
        'last_name': str,
        'email': str,
    })
    assert schema.is_valid(user)

def test_build_user_comparison():
    user1 = build_user()
    user2 = build_user()
    assert user1 != user2

def test_build_user_params():
    user = build_user({'first_name': 'Petya'})
    assert user['first_name'] == 'Petya'

# END