'''
tests/test_solution.py
Протестируйте функцию get_files_count(), которая считает количество всех файлов в указанной директории и всех
 поддиректориях:

from functions import get_function
get_files_count = get_function()

get_files_count("/path/to/directory")  # 4
У этой функции есть дополнительное поведение. Во время обхода файлов она записывает информацию о задействованных
 файлах в специальный файл — журнал действий (лог).

Все, что мы хотим – чтобы функция считала количество файлов. При этом запись в файл является нежелательным
побочным эффектом — каждый запуск будет заполнять какой-то файл, который мы никак не используем. Попробуем
 избавиться от этого эффекта. Для записи в файл функция get_files_count(), использует другую функцию,
  которую можно подменить:

def get_files_count(filepath, log=write_data_to_file):
    # Где-то внутри во время работы
    write_data_to_file(f"File {name} has been processed")
Для подмены нужно передать вторым параметром функцию-пустышку, которая не будет ничего делать. В таком случае
 ее вызов внутри get_files_count() хоть и отработает, но не породит побочного эффекта.

Подсказки
Передайте этой функции путь до директории внутри fixtures и убедитесь в том, что она правильно посчитала
количество файлов внутри
'''

import os
from d_func import get_function

get_files_count = get_function()


# BEGIN (write your solution here)
def pass_func():
    pass

def test_get_files_count():
    assert get_files_count('fixtures/flat', pass_func) == 2
    assert get_files_count('fixtures/nested', pass_func) == 4

# END