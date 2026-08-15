from Project0.Service.cart_service import CartService
from Project0.exceptions.exceptions import (
    InvalidProductError,
    NegativeQuantityError,
    InsufficientStockError,
    EmptyCartError
)

class CartController:

    def __init__(self):
        self.cart_service = CartService()

    def add_to_cart(self, customer_id):

        print("\n===== ADD TO CART =====")

        try:
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))

            self.cart_service.add_to_cart(
                customer_id,
                product_id,
                quantity
            )

            print("Product added to cart successfully.")

        except ValueError:
            print("Product ID and quantity must be numbers.")

        except InvalidProductError as e:
            print(f"Error: {e}")

        except NegativeQuantityError as e:
            print(f"Error: {e}")

        except InsufficientStockError as e:
            print(f"Error: {e}")

    def remove_from_cart(self, customer_id):

        print("\n===== REMOVE FROM CART =====")

        try:
            product_id = int(input("Enter product ID: "))

            self.cart_service.remove_from_cart(
                customer_id,
                product_id
            )

            print("Product removed from cart.")

        except ValueError:
            print("Product ID must be a number.")

        except InvalidProductError as e:
            print(f"Error: {e}")

        except EmptyCartError as e:
            print(f"Error: {e}")

    def view_cart(self, customer_id):

        print("\n========== YOUR CART ==========")

        try:
            cart_items = self.cart_service.view_cart(
                customer_id
            )

            if not cart_items:
                raise EmptyCartError(
                    "Your cart is empty."
                )

            total = 0

            for item in cart_items:

                subtotal = (
                    item["price"] *
                    item["quantity"]
                )

                total += subtotal

                print(
                    f"Product ID: {item['product_id']}\n"
                    f"Product: {item['product_name']}\n"
                    f"Price: ₹{item['price']}\n"
                    f"Quantity: {item['quantity']}\n"
                    f"Subtotal: ₹{subtotal}\n"
                    f"--------------------------"
                )

            print(f"Cart Total: ₹{total}")

        except EmptyCartError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")
