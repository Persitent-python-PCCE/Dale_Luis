import unittest

from Project0.Controller.admin_controller import AdminController
from Project0.Model.customer import Customer
from Project0.Model.product import Product


class TestModels(unittest.TestCase):

    def test_product_stores_given_values(self):
        product = Product(
            product_id=1,
            product_name="Notebook",
            price=50.0,
            stock=10
        )

        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.product_name, "Notebook")
        self.assertEqual(product.price, 50.0)
        self.assertEqual(product.stock, 10)

    def test_customer_has_customer_role_by_default(self):
        customer = Customer(name="Dale", email="dale@example.com")

        self.assertEqual(customer.name, "Dale")
        self.assertEqual(customer.role, "CUSTOMER")

    def test_admin_user_is_allowed_to_use_admin_functions(self):
        admin = Customer(name="Admin", email="admin@example.com", role="admin")
        controller = AdminController()

        controller.check_admin(admin)


if __name__ == "__main__":
    unittest.main()
