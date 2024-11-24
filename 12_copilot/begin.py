def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

from functools import reduce

def factorial(n):
    reduce(lambda x, y: x * y, range(1, n + 1), 1)
