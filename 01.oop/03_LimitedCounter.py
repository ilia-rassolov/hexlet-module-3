class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)

class LimitedCounter(Counter):

    def __init__(self, limit):
        super().__init__()
        self.limit = limit
        self.value = min(self.value, self.limit)


    def inc(self, amount_limited_counter_inc=1):
        self.amount_limited_counter_inc = amount_limited_counter_inc
        super().inc(self.amount_limited_counter_inc)
        self.value = min(self.value, self.limit)
    #



counter = LimitedCounter(limit=10)
print(f"{counter.value=}")
counter.inc(20)
print(f"{counter.value=}")
counter.dec(-17)
print(f"{counter.value=}")
counter.dec(7)
print(counter.value)
c2 = LimitedCounter(5)
print(f"{c2.value=}")
c2.dec(-8)
print(f"{c2.value=}")