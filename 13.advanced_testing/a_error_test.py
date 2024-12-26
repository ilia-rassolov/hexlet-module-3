'''
В этом задании вам предстоит работать с функцией read(), которая читает содержимое файла. Напишите негативный тест
 этой функции, проверяющий ошибочные ситуации. Рассмотрите следующие ситуации:

Файл не найден
В функцию передан путь до директории read(filepath)
from functions import get_function
read = get_function()

read('/undefined')  # FileNotFoundError
read('/etc')  # IsADirectoryError
'''

import pytest
from a_functions import get_function

read = get_function()


# BEGIN (write your solution here)
import os


def test_read_with_nonexistent():
    with pytest.raises(FileNotFoundError):
        read("none")


def test_read_with_directory():
    with pytest.raises(IsADirectoryError):
        read("/etc")


# END