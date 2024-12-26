import os


def default_logger(message):
    raise Exception("Can not write data to log")


def _right(filepath, log=default_logger):
    log('Go!')
    files_count = sum(len(files) for _, _, files in os.walk(filepath))
    return files_count


def _fail1(filepath, log=default_logger):
    log('Go!')
    log('Go!')
    files_count = sum(len(files) for _, _, files in os.walk(filepath))
    return files_count


def _fail2(filepath, log=default_logger):
    log('Boom!')
    files_count = sum(len(files) for _, _, files in os.walk(filepath))
    return files_count


functions = {
    "right": _right,
    "fail1": _fail1,
    "fail2": _fail2,
}


def get_function():
    # name = os.environ['FUNCTION_VERSION']
    name = 'right'
    return functions[name]
