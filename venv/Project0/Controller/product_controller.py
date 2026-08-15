from Project0.Service.product_service import ProductService
from Project0.exceptions.exceptions import (
    InvalidProductError,
    ValidationError
)

class ProductController:

    def __init__(self):
        self.product_service = ProductService()

    def show_products(self):

        print("\n===== PRODUCTS =====")

        try:
            products = self.product_service.get_all_products()

            if not products:
                print("No products available.")
                return

            for product in products:
                print(
                    f"ID: {product.product_id} | "
                    f"Name: {product.product_name} | "
                    f"Price: ₹{product.price} | "
                    f"Stock: {product.stock}"
                )

        except Exception as e:
            print(f"Error: {e}")

    def search_by_name(self):

        print("\n===== SEARCH PRODUCT =====")

        name = input("Enter product name: ").strip()

        if not name:
            print("Product name cannot be empty.")
            return

        try:
            products = self.product_service.search_by_name(name)

            if not products:
                print("No products found.")
                return

            for product in products:
                print(
                    f"ID: {product.product_id} | "
                    f"Name: {product.product_name} | "
                    f"Price: ₹{product.price} | "
                    f"Stock: {product.stock}"
                )

        except Exception as e:
            print(f"Error: {e}")

    def search_by_category(self):

        print("\n===== SEARCH BY CATEGORY =====")

        category = input("Enter category name: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        try:
            products = self.product_service.search_by_category(category)

            if not products:
                print("No products found in this category.")
                return

            for product in products:
                print(
                    f"ID: {product.product_id} | "
                    f"Name: {product.product_name} | "
                    f"Price: ₹{product.price} | "
                    f"Stock: {product.stock}"
                )

        except Exception as e:
            print(f"Error: {e}")

    def view_product(self):

        print("\n===== PRODUCT DETAILS =====")

        try:
            product_id = int(input("Enter product ID: "))

            product = self.product_service.get_product_by_id(product_id)

            print(f"\nProduct ID: {product.product_id}")
            print(f"Name: {product.product_name}")
            print(f"Description: {product.p_description}")
            print(f"Price: ₹{product.price}")
            print(f"Stock: {product.stock}")

        except ValueError:
            print("Product ID must be a number.")

        except InvalidProductError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")
