import psycopg2
from psycopg2.extras import NamedTupleCursor
from dataclasses import dataclass
from typing import Optional

# conn = psycopg2.connect(dbname='hexlet', user='user')

@dataclass
class Product:
    def __init__(self, name, description, price, id=None):
        self.name = name
        self.description = description
        self.price = price
        self.id = id

    def save_product(self, conn):
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            if self.id is None:
                cur.execute(
                    "INSERT INTO products (name, description, price) VALUES (%s, %s, %s) RETURNING id;",
                    (self.name, self.description, self.price)
                )
                self.id = cur.fetchone().id
            else:
                cur.execute(
                    "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s;",
                    (self.name, self.description, self.price, self.id)
                )
            conn.commit()

class ProductDAO(Product):

    def find_product(conn, product_name):
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute("SELECT * FROM products WHERE name = %s;", (product_name,))
            result = cur.fetchone()
            if result:
                return ProductDAO(
                    id=result.id,
                    name=result.name,
                    description=result.description,
                    price=result.price
                )
        return None

prod = Product('apple', 'fruit', 25)

print(prod.name)


https://generatedata.com/generator



