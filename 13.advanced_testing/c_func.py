import os

from bs4 import BeautifulSoup


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def write(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)


def _right(file_path):
    data = read(file_path)

    write(
        file_path,
        BeautifulSoup(data, 'html.parser').prettify()
    )


def _wrong(file_path):
    data = read(file_path)
    write(file_path, data)


functions = {
    "right": _right,
    "wrong": _wrong,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
