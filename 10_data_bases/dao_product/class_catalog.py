from class_productdao import ProductDAO
import psycopg2


conn2 = psycopg2.connect(dbname='hexlet', user='user')
class Catalog:
    def __init__(self, conn):
        self.conn = conn

    def get_product(self, product_name):
        object = ProductDAO(self.conn).find_product(product_name)
        return {'id': object.id,
                'name': object.name,
                'description': object.description,
                'price': object.price}


print(Catalog(conn2).get_product('breskva'))

# from productDAO import ProductDAO
#
#
# class Catalog:
#     def __init__(self, conn):
#         self.conn = conn
#
#     # BEGIN
#     def get_product(self, name):
#         dao = ProductDAO(self.conn)
#         product = dao.find_by_name(name)
#
#         if product is None:
#             raise KeyError(f'Product {name} is not found')
#
#         id = product.get_id()
#         name = product.get_name()
#         description = product.get_description()
#         price = product.get_price()
#
#         return {
#             'id': id,
#             'name': name,
#             'description': description,
#             'price': price
#         }
#     # END