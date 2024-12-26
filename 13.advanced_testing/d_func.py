import os


def default_logger():
    raise Exception("Can not write data to log")


def _right(filepath, log=default_logger):
    log()
    files_count = sum(len(files) for _, _, files in os.walk(filepath))
    return files_count


def _fail1(filepath, log=default_logger):
    dirs_count = sum(len(dirs) for _, dirs, _ in os.walk(filepath))
    return dirs_count


functions = {
    "right": _right,
    "fail1": _fail1,
}


def get_function():
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
