from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    name: str
    email: str


@dataclass
class Address:
    street: str
    city: str
    country: str
    zip_code: str


@dataclass
class Item:
    name: str
    price: float


class Order:
    def __init__(self, id, customer, shipping_address, items=dict(), total_price=0):
        self.id = id
        self.customer = customer
        self.shipping_address = shipping_address
        self.items = items
        self.total_price = total_price

    def __eq__(self, other):
        return self.id == other.id

    def add_item(self, item, quantity):
        if item not in self.items:
            self.items[item] = quantity
        else:
            self.items[item] += quantity

    def remove_item(self, item, quantity):
        if quantity >= self.items.get(item, 0)
            self.items = list(filter(lambda x: x[item] != item, self.items))
        else:
            self.items[item] += quantity






