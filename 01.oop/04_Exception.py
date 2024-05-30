def suppress(error, or_return=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except error:
                return or_return
            return func(*args, **kwargs)
        return inner
    return wrapper


@suppress(ZeroDivisionError, or_return=42)
def foo():
     return 1 // 0

print(foo())

@suppress((KeyError, IndexError))
def get_item(key, structure):
     return structure[key]

print(get_item(7, "foo") is None)
print(get_item('a', {}) is None)