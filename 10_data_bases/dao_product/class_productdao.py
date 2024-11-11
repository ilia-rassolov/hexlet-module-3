from class_product import Product
import psycopg2
from psycopg2.extras import NamedTupleCursor

conn = psycopg2.connect(dbname='hexlet', user='mint')


class ProductDAO:
    def __init__(self, name_dao):
        self.name_dao = name_dao


    def find_product(self):
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute("SELECT * FROM products WHERE name = %s;", (self.name_dao,))
            result = cur.fetchone()
            if result:
                return Product(
                    id=result.id,
                    name=result.name,
                    description=result.description,
                    price=result.price
                )
            else:
                raise Exception(f"KeyError: Product {self.name_dao} not found")

Breskva = ProductDAO('breskva')
print(Breskva.find_product())