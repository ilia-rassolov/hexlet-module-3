'''
В этом задании нужно протестировать такую же функцию get_user_main_language(user), как и в предыдущем упражнении.
 Разница в том, что здесь нужно использовать манкипатчинг, а не инверсию зависимостей.

Подмените атрибут list_for_users() в классе Client, который используется функцией get_user_main_language(user)
для отправки запроса.

# Запрос, который выполняет функция get_user_main_language()
# Именно этот метод нужно будет подменить в фейковом клиенте
data = client.list_for_users(user_name)
# Список репозиториев — data. У каждого репозитория может быть много полей,
# но нас интересует ровно одно – language
# Эти данные нужно подготовить в тестах для фейкового клиента
print(data)
# [{ "language": "php", ... }, { "language": "javascript", ... }, ...]
'''

from e_client import Client
from e_func import get_function

get_user_main_language = get_function()


def fake_methode(self, user_name='user_name'):
    if not user_name:
        return None
    return [{"language": "php" }, {"language": "javascript"},
            {"language": "javascript"}, {"language": "python"}]


Client.list_for_users = fake_methode
client = Client()

def test_get_user_main_language():
    assert get_user_main_language('user_name', client) == "javascript"


def test_get_user_main_language_empty():
    assert get_user_main_language('', client) is None