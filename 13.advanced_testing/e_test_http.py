'''
tests/test_solution.py
Протестируйте функцию get_user_main_language(user_name, client), которая определяет язык, на котором пользователь
 создал больше всего репозиториев.

Для реализации этой задачи функция get_user_main_language() выполняет запрос к веб-сервису при помощи клиента client.
 Этот клиент извлекает все репозитории указанного пользователя по первому параметру user_name. Каждый репозиторий в
 этом списке содержит указание основного языка репозитория. Эта информация используется для поиска того языка, который
 используется чаще. Если список репозиториев пуст, функция возвращает None. Замените клиент тестовым двойником:

# Запрос, который выполняет функция get_user_main_language()
# Именно этот метод нужно будет подменить в фейковом клиенте
data = client.list_for_users(user_name)
# Список репозиториев — data. У каждого репозитория может быть много полей,
# но нас интересует ровно одно – language
# Эти данные нужно подготовить в тестах для фейкового клиента
print(data)
# [{ "language": "php", ... }, { "language": "javascript", ... }, ...]
src/FakeClient.py
Реализуйте фейковый клиент и используйте этот клиент в тестах для подмены.
'''

from e_fake_client import FakeClient
from e_func import get_function

get_user_main_language = get_function()


# BEGIN (write your solution here)
def test_get_user_main_language():
    fake_client = FakeClient()
    assert get_user_main_language('user_name', fake_client) == "javascript"
    assert get_user_main_language('', fake_client) is None



# END
