from class_product import Product
import psycopg2
from psycopg2.extras import NamedTupleCursor

conn = psycopg2.connect(dbname='hexlet', user='user')


class ProductDAO:
    def __init__(self, conn_):
        self.conn = conn_

    def save_product(self, product_):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as curs:
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
            self.conn.commit()


    def find_product(self, product_name):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute("SELECT * FROM products WHERE name = %s;", (product_name,))
            result = cur.fetchone()
            if result:
                return Product(
                    id=result.id,
                    name=result.name,
                    description=result.description,
                    price=result.price
                )
            else:
                raise KeyError(f"Product {product_name} not found")


prod = Product('blueberry', 'blueberry', 80)
ProductDAO(conn).save_product(prod)

# from product import Product
#
# # BEGIN
# from psycopg2.extras import DictCursor
#
#
# class ProductDAO:
#     def __init__(self, conn):
#         self.conn = conn
#
#     def find_by_name(self, name):
#         with self.conn.cursor(cursor_factory=DictCursor) as cursor:
#             sql = "SELECT * FROM products WHERE name = %s"
#             cursor.execute(sql, (name,))
#             result = cursor.fetchone()
#
#             if result:
#                 product = Product(
#                     result['name'],
#                     result['description'],
#                     result['price']
#                 )
#                 product.set_id(int(result['id']))
#                 return product
#
#         return None