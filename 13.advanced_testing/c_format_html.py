'''
Протестируйте функцию, которая форматирует и изменяет указанный HTML-файл:

# Содержимое файла до форматирования:
# <div><p>Hello, <a href="https://hexlet.io">Hexlet</a></p></div>

prettify_html_file('/path/to/file')

# Содержимое форматирования:
# <div>
#  <p>
#   Hello,
#   <a href="https://hexlet.io">
#    Hexlet
#   </a>
#  </p>
# </div>
Подсказки
В директории test_data лежат готовые тестовые данные
Для копирования файлов воспользуйтесь модулем shutil https://docs.python.org/3/library/shutil.html
tmp_path https://docs.pytest.org/en/7.1.x/how-to/tmp_path.html#the-tmp-path-fixture
'''

import os
import shutil

import pytest
from c_func import get_function

prettify_html_file = get_function()


# BEGIN (write your solution here)
def test_prettify_html_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "tmp_file.html"
    shutil.copyfile('test_data/before.html', p)

    with open('test_data/after.html', 'r') as f:
        fixture = f.read()

    prettify_html_file(p)

    with open(p, 'r') as res:
        result = res.read()

    assert len(list(tmp_path.iterdir())) == 1
    assert result == fixture
# END
