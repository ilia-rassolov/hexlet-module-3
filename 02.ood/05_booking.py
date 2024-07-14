from datetime import date, timedelta

class Booking:
    def __init__(self):
        self.busy = []



    def book(self, check_in, check_out):

        def is_valid_data(start_day, finish_day):
            if finish_day <= start_day:
                return False
            return True

        if not is_valid_data(check_in, check_out):
            return False

        check_in = date.fromisoformat(check_in)
        check_out = date.fromisoformat(check_out)
        booking_days = []
        while check_in != check_out:
            booking_days.append(check_in)
            check_in += timedelta(days=1)
        for day in booking_days:
            if day in self.busy:
                return False
        self.busy.extend(booking_days)
        return True

booking = Booking()
print(booking.book('2008-11-10', '2008-11-11'))

print(booking.book('2008-11-12', '2008-11-17'))
print(booking.book('2008-11-16', '2008-11-19'))
print(booking.book('2008-11-22', '2008-11-21'))
print(booking.book('2008-11-10', '2008-11-11'))
print(booking.busy)

booking2 = Booking()
print(booking2.busy)
print(booking2.book('2008-11-10', '2008-11-11'))
print(booking2.busy)






