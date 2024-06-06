class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(self.value + delta)

    def dec(self, delta=1):
        return Counter(self.value - delta)

c = Counter()
print(f"{c.value=}")
print(c.inc(8).value)
# c.inc().inc(5).value
c.inc()
print(f"{c.value=}")
print(f'{c.inc().inc(5).dec(4).value=}')
c.inc(40)
print(f'{c.value=}')
c.dec(30)
print(f'{c.value=}')
print(f'{c.dec(delta=100).value=}')
d = c.inc(100)
print(d.dec().value)
print(f'{c.value=}')
