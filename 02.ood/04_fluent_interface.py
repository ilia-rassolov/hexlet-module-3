from functools import reduce

class Collection:
    def __init__(self, data):
        self.data = data

    def strip_(self):
        self.data = list(map(lambda city: {'name': city['name'].strip(),
                                           'country': city['country'].strip()}, self.data))
        return self

    def lower_(self):
        self.data = list(map(lambda city: {'name': city['name'].lower(),
                                           'country': city['country'].lower()}, self.data))
        return self
    #
    def uniq_(self):
        self.data = list(reduce(lambda cities, city: cities.append(city), self.data, []))
        return self

    def all(self):
        return self.data

    def format(self):
        return self.strip_().lower_().uniq_().all()

raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]

city = Collection(raw)
print(city.format())




