class Counter:
    value = 0
    def inc(self, delta=1):
        current_value = self.value + delta
        if isinstance(current_value, int) and current_value >= 0:
            self.value = current_value
        else:
            self.value = 0


    def dec(self, delta=1):
        current_value = self.value - delta
        if isinstance(current_value, int) and current_value >= 0:
            self.value = current_value
        else:
            self.value = 0