import os


def _right(path):
    f = open(path)
    data = f.read()
    f.close()
    return data


def _fail1(path):
    os.remove(path)


def _fail2(path):
    if not os.path.exists(path):
        return

    f = open(path)
    data = f.read()
    f.close()
    return data


functions = {
    "right": _right,
    "fail1": _fail1,
    "fail2": _fail2
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]