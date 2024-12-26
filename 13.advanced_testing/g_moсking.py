'''
Протестируйте функцию get_files_count(path, log), которая считает количество всех файлов в указанной директории и
всех поддиректориях. В отличие от предыдущей версии задания, здесь нас интересует, что эта функция выполняет
логирование с помощью функции log(). Мы хотим убедиться, что она один раз отправляет сообщение c текстом 'Go!' в
лог. Для этого придется воспользоваться моком.

Подсказки
unittest.mock.call_count https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_count
unittest.mock.call_args https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args
Обратите внимание в документации, где именно создается мок
'''

import os
from unittest.mock import Mock
from g_func import get_function

get_files_count = get_function()


def get_fixture_path(name):
    return os.path.join('fixtures', name)


# BEGIN (write your solution here)
def test_get_files_count_flat():
    path = 'fixtures/flat'
    mock = Mock()
    get_files_count(path, mock('Go!'))

    assert mock.call_count == 1
    assert mock.call_args.args == ('Go!',)
    assert get_files_count(path, mock('Go!')) == 2

def test_get_files_count_nested():
    path = 'fixtures/nested'
    mock = Mock()
    get_files_count(path, mock)

    assert mock.call_count == 1
    assert mock.call_args.args == ('Go!',)
    assert get_files_count(path, mock('Go!')) == 4

# END