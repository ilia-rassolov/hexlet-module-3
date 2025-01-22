'''
Многие функции обработки данных зачастую работают с файловой системой. Но помимо усложнений в форме внешних эффектов,
они могут зависеть от недетерминированных значений, таких как время.

tests/test_solution.py
В этом упражнении вам предстоит протестировать функцию delete_old_files(), которая удаляет файлы в указанной
 директории, которые старше заданного количества дней. Функция также возвращает список удаленных файлов.

tree dir
# предположим, что file1 и file2 созданы 2 дня назад
# а file3 создан 5 дней назад
.
|- dir
    |- file1.txt
    |- file2.txt
    |- file3.txt
delete_old_files('dir', 3) # ["file1.txt", "file2.txt"]
tree dir
# в директории останется только file3.txt
.
|- dir
    |- file3.txt
Если директория не существует, функция возвращает None. Если директория пустая, то функция возвращает пустой список.
Чтобы проверить возраст файла, функция delete_old_files() использует функцию is_file_old(). Функция is_file_old()
возвращает True, если файл старше заданного количества дней, и False в противном случае. Возраст файла определяется
как разница между текущим временем и временем последнего изменения файла, где текущее время — это результат
вызова datetime.now().

Подсказки
В тестах вам уже предоставлена функция create_file(), которая создаёт файл с заданной датой изменения. Используйте
 её для создания файлов с разными датами изменения.
tmp_path https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html#the-tmp-path-fixture
При тестировании функций работающих со временем важно фиксировать текущее время для детерминированности тестов. Для
этого можно использовать библиотеку freeze_time. https://github.com/spulec/freezegun
'''

import os
from datetime import datetime, timedelta

from freezegun import freeze_time
from h_func import get_function

delete_old_files = get_function()


def create_file(directory, filename, days_old):
    """Вспомогательная функция для создания файла с заданной датой изменения."""
    file_path = os.path.join(directory, filename)
    with open(file_path, "w") as f:
        f.write("test content")
    old_time = datetime.now() - timedelta(days=days_old)
    os.utime(file_path, (old_time.timestamp(), old_time.timestamp()))


# BEGIN (write your solution here)
def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    create_file(d, 'file1.txt', 5)
    create_file(d, 'file2.txt', 5)
    create_file(d, 'file3.txt', 2)
    delete_old_files(d, 3)

    assert len([1 for file in d.iterdir()]) == 1
    assert os.path.exists(d / 'file3.txt') == True

# END