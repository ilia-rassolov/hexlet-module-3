class HourClock:
    def __init__(self, hour=0):
        self.hour = hour

    @property
    def hours(self):
        print(f"{self.hour=}", 'getter')
        return self.hour

    @hours.setter
    def hours(self, time):
        self.hour = time % 12
        print(f"{self.hour=}", 'setter')

clock = HourClock()
print(f"{clock.hours=}")
# # в начале часовая стрелка всегда на нуле
clock.hours += 4
print(f"{clock.hours=}")
# # # ^ эквивалентно clock.hours = clock.hours + 5
clock.hours += 6
print(f"{clock.hours=}")
clock.hours += 5
print(f"{clock.hours=}")
clock.hours -= 4
print(f"{clock.hours=}")
clock.hours = 123
print(f"{17 % 12}")
