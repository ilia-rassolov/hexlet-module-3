import psycopg2
from psycopg2.extras import NamedTupleCursor
from dataclasses import dataclass
from typing import Optional

conn = psycopg2.connect(dbname='hexlet', user='mint')


def save_product(product_, conn_):

    with conn_.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(
            "SELECT * FROM products WHERE name = %s;",
            (product_.name,))
        if curs.fetchone() is None:
            if product_.id is None:
                curs.execute(
                    "INSERT INTO products (name, description, price) VALUES (%s, %s, %s) RETURNING id;",
                    (product_.name, product_.description, product_.price)
                )
                product_.id = curs.fetchone().id
            else:
                curs.execute(
                    "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s;",
                    (product_.name, product_.description, product_.price, product_.id)
                )
        conn.commit()


class Product:
    def __init__(self, name, description, price, id=None):
        self.name = name
        self.description = description
        self.price = price
        self.id = id
        save_product(self, conn)


prod = Product('breskva', 'very nice', 45)

print(prod.price)


# https://generatedata.com/generator



