from class_productdao import ProductDAO


class Catalog:

    def get_product(self, product_name):
        object = ProductDAO(product_name).find_product()
        return {'id': object.id,
                'name': object.name,
                'description': object.description,
                'price': object.price}


print(Catalog().get_product('banan2'))