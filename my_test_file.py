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


