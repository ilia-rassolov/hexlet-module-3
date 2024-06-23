from collections import defaultdict

class Money:
    def __init__(self, amount_currency, currency='usd'):
        wallet = defaultdict(float)
        wallet[currency] = float(amount_currency)
        self.wallet = wallet

    def add(self, bonus, currency_bonus='usd'):
        self.wallet[currency_bonus] += bonus

    def get_amount(self, currency_):
        wallet_ = dict(self.wallet)
        try:
            print(f"на вашем счёте {wallet_[currency_]} {currency_}")
        except KeyError:
            print(f"на вашем счёте 0.00 {currency_}")

    def get_all_money(self):
        list_ = []
        for k,v in self.wallet.items():
            list_.append(f"{v} {k}")
        print(f"на вашем счёте {', '.join(list_)}")

    @property
    def total_getter(self):
        list_ = []
        for k,v in self.wallet.items():
            list_.append(f"{v} {k}")
        if any(not val for val in self.wallet.values()):
            print(f"Ваш счёт: {', '.join(list_)}")
        else:
            print('Ваш счёт пустой :(')

mon = Money(10, 'eur')
print(mon.__dict__)

mon.add(5, 'rub')
mon.add(2)
print(mon.__dict__)
print(mon.wallet)
mon.get_amount('eur')
mon.get_amount('dm')
mon.get_amount('')
print(mon.__dict__)
mon.get_all_money()
mon.total_getter
mon.wallet = {'eur': 00}
mon.get_all_money()
# html = markdown(markdown_text)
print('-'*78)

class Address:
    def __init__(self, street, house, zipcode):
        self.street = street
        self.house = house
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.house}, {self.zipcode}"

class User:
    def __init__(self, address):
        self.street = address['street']
        self.house = address['house']
        self.zipcode = address['zipcode']

    def get_address(self):
        # Поскольку у нас объект-значение,
        # мы можем создавать его столько раз, сколько нам нужно,
        # но при необходимости этот процесс можно оптимизировать
        return Address(self.street, self.house, self.zipcode)

address = {'street': 'pushkina', 'house': 42, 'zipcode': 42000}
user = User(address)
print(user.get_address())  #=> pushkina, 42, 42000

print(f"{'|' * 78}")

class Collection:
    def __init__(self, coll):
        self.coll = coll

    def map(self, fn):
        self.coll = list(map(fn, self.coll))
        return self

    def filter(self, fn):
        self.coll = list(filter(fn, self.coll))
        return self


    # Возвращает саму коллекцию, а не self.
    # Этот метод всегда последний в цепочке вызовов Collection.
    def all(self):
        return self.coll

names = Collection(['taylor', 'abigail', None])

result = names.map(lambda name: str(name).upper() if name else '').filter(lambda name: name != '')
        # Переводим в верхний регистр
        # Отфильтровываем пустые


# Выводим коллекцию на экран
print(result.all())  # => ['TAYLOR', 'ABIGAIL']

print('*' * 100)

from datetime import date, timedelta


start_day = date.fromisoformat('2008-11-18')
finish_day = date.fromisoformat('2008-11-22')
booking_days = []
while start_day != finish_day:
    booking_days.append(start_day)
    start_day += timedelta(days=1)



print(booking_days, start_day, start_day - timedelta(days=1) in booking_days)