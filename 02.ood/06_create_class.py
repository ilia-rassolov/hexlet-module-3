from dataclasses import dataclass


@dataclass
class Customer:
    id: int
    name: str
    email: str

    def __eq__(self, other):
        return self.id == other.id


class Address:
    def __init__(self, street, city, country, zipcode):
        self.street = street
        self.city = city
        self.country = country
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}, {self.zipcode}"

    def __eq__(self, other):
        return self.__str__() == other.__str__()


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self, id, customer, shipping_adress):
        self.id = id
        self.customer = customer
        self.shipping_adress = shipping_adress
        self.items = dict()
        self.total_price = 0

    def add_item(self, item, quantity):
        if item.name not in self.items:
            self.items[item.name] = quantity
        else:
            self.items[item.name] += quantity
        self.total_price += item.price * quantity

    def remove_item(self, item):
        quantity_start = self.items.get(item.name, 0)
        if quantity_start < 1:
            pass
        self.total_price -= item.price * 1
        if quantity_start == 1:
            self.items.pop(item.name, None)
        else:
            self.items[item.name] -= 1

    def get_total_price(self):
        return self.total_price


address1 = Address("123 Main St", "Cityville", "USA", "12345")
address2 = Address("456 Oak Rd", "Townsville", "Canada", "67890")
address3 = Address("456 Oak Rd", "Townsville", "Canada", "67890")

customer1 = Customer(1, "John Doe", "john@example.com")
customer2 = Customer(2, "Alice Smith", "alice@example.com")
customer3 = Customer(1, "Bob Mcmaffin", "bob@example.com")

order1 = Order(1, customer1, address1)
order2 = Order(2, customer2, address2)
order3 = Order(3, customer3, address3)
order4 = Order(3, customer3, address3)

item1 = Item("Product A", 10.00)
item2 = Item("Product B", 5.00)
item3 = Item("Product C", 15.00)

print(order1.shipping_adress)
print(order1.items)
print(item2.name)
print('*'*99)

order1.add_item(item1, 2)
order1.add_item(item2, 3)
order2.add_item(item3, 1)
print(address1)
print(order1.items)
print(order2.items)
print(order3.items)
order1.remove_item(item1)
print(order2.items)
order1.get_total_price()
print(item1.price)
order1.add_item(item1, 2)
order1.add_item(item2, 3)
print(order1.total_price)
order1.add_item(item1, 2)
print(order1.total_price)
print(order2.shipping_adress == order3.shipping_adress)  # True)
print(order1.customer == order3.customer)  # True)
print('*'*50)
order4.add_item(item1, 2)
print(order4.total_price)
order4.add_item(item2, 3)
print(order4.total_price)
order4.remove_item(item1)
order4.remove_item(item2)
print(order4.total_price)
order4.add_item(item1, 2)
print(order4.total_price)


