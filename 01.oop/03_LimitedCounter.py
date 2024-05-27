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
        self.value = min(self.value, limit)

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)


    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


counter = LimitedCounter(limit=10)
counter.inc(20)
counter.inc(7)
print(counter.value)
counter.inc(7)
print(counter.value)
