from Project0.Dao.product_dao import ProductDAO
from Project0.Model.product import Product
from Project0.exceptions.exceptions import (
    InvalidProductError,
    ValidationError,
    UnauthorizedError
)


class ProductService:

    def __init__(self):
        self.product_dao = ProductDAO()

    def get_products(self):
        return self.product_dao.get_all_products()

    def get_all_products(self):
        return self.product_dao.get_all_products()

    def search_by_name(self, name):

        if not name.strip():
            raise ValidationError("Search name cannot be empty.")

        return self.product_dao.search_by_name(name)

    def search_by_category(self, category_name):

        if not category_name.strip():
            raise ValidationError("Invalid category.")

        return self.product_dao.search_by_category(category_name)

    def add_product(self, name, description, price, stock, category_id, supplier_id):

        if price < 0:
            raise ValidationError("Price cannot be negative.")

        if stock < 0:
            raise ValidationError("Stock cannot be negative.")

        return self.product_dao.add_product(Product(
            product_name=name, p_description=description, price=price,
            stock=stock, category_id=category_id, supplier_id=supplier_id
        ))

    def update_product(self, product_id, name, description, price, stock, category_id, supplier_id):

        self.get_product_by_id(product_id)

        return self.product_dao.update_product(Product(
            product_id=product_id, product_name=name, p_description=description,
            price=price, stock=stock, category_id=category_id,
            supplier_id=supplier_id
        ))

    def delete_product(self, product_id):

        self.get_product_by_id(product_id)

        return self.product_dao.delete_product(product_id)

    def get_product_by_id(self, product_id):
        product = self.product_dao.get_product_by_id(product_id)
        if product is None:
            raise InvalidProductError("Invalid product ID.")
        return Product(
            product_id=product["product_id"],
            product_name=product["product_name"],
            p_description=product["p_description"],
            price=product["price"], stock=product["stock"],
            category_id=product["category_id"],
            supplier_id=product["supplier_id"], is_active=product["is_active"]
        )
