from datetime import date, timedelta

class Booking:
    def __init__(self):
        self.busy = []

    def validate_data(self):
        if '@' not in self.data.get('email', ''):
            self.errors.append('Invalid email')
        return self
    def book(self, start_day, finish_day):
        start_day = date.fromisoformat(start_day)
        finish_day = date.fromisoformat(finish_day)
        booking_days = []
        while start_day != finish_day:
            booking_days.append(start_day)
            start_day += timedelta(days=1)
        if len(booking_days) < 2:
            return False
        for day in booking_days:
            if day in self.busy:
                return False
        self.busy.extend(booking_days)
        return True

booking = Booking()
print(booking.book('2008-11-10', '2008-11-12'))
print(booking.book('2008-11-12', '2008-11-17'))
print(booking.book('2008-11-18', '2008-11-19'))
print(booking.book('2008-11-18', '2008-11-22'))

booking2 = Booking()
print(booking.book('2008-11-10', '2008-11-12'))
# print(f"{}")





