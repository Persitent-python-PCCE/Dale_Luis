from Project0.Controller.auth_controller import AuthController
from Project0.Controller.product_controller import ProductController
from Project0.Controller.cart_controller import CartController
from Project0.Controller.order_controller import OrderController
from Project0.Controller.admin_controller import AdminController
from Project0.Controller.review_controller import ReviewController

from Project0.exceptions.exceptions import (
    InvalidMenuChoiceError,
    DatabaseConnectionError
)


class EcommerceApp:

    def __init__(self):
        self.auth_controller = AuthController()
        self.product_controller = ProductController()
        self.cart_controller = CartController()
        self.order_controller = OrderController()
        self.admin_controller = AdminController()
        self.review_controller = ReviewController()

        self.current_user = None

    def start(self):

        while True:

            print("\n")
            print("=" * 40)
            print("       E-COMMERCE APPLICATION")
            print("=" * 40)
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            print("=" * 40)

            try:
                choice = int(input("Enter your choice: "))

                if choice not in range(1, 7):
                    raise InvalidMenuChoiceError(
                        "Please select a valid menu option."
                    )

                if choice == 1:
                    self.login()

                elif choice == 2:
                    self.register()
                    
                elif choice == 3:
                    print("\nThank you for using the E-Commerce Application!")
                    break

            except ValueError:
                print("\nError: Please enter a number.")

            except InvalidMenuChoiceError as e:
                print(f"\nError: {e}")

            except DatabaseConnectionError as e:
                print(f"\nDatabase Error: {e}")

    def register(self):

        customer = self.auth_controller.register()

        if customer:
            print("\nYou can now login using your credentials.")

    def login(self):

        customer = self.auth_controller.login()

        if customer is None:
            return

        self.current_user = customer

        if customer.role.strip().upper() == "ADMIN":
            self.admin_menu()
        else:
            self.customer_menu()

        self.current_user = None

    def customer_menu(self):

        while self.current_user is not None:

            print("\n")
            print("=" * 40)
            print("          CUSTOMER MENU")
            print("=" * 40)
            print("1. Browse Products")
            print("2. Search Product")
            print("3. Search by Category")
            print("4. View Cart")
            print("5. Add Product to Cart")
            print("6. Remove Product from Cart")
            print("7. Checkout")
            print("8. Order History")
            print("9. Add Product Review")
            print("10. View Product Reviews")
            print("11. Logout")
            print("=" * 40)

            try:
                choice = int(input("Enter your choice: "))

                if choice not in range(1, 12):
                    raise InvalidMenuChoiceError(
                        "Invalid menu choice."
                    )

                customer_id = self.current_user.customer_id

                if choice == 1:

                    self.product_controller.show_products()

                elif choice == 2:

                    self.product_controller.search_by_name()

                elif choice == 3:

                    self.product_controller.search_by_category()

                elif choice == 4:

                    self.cart_controller.view_cart(
                        customer_id
                    )

                elif choice == 5:

                    self.cart_controller.add_to_cart(
                        customer_id
                    )

                elif choice == 6:

                    self.cart_controller.remove_from_cart(
                        customer_id
                    )

                elif choice == 7:

                    self.order_controller.place_order(
                        customer_id
                    )

                elif choice == 8:

                    self.order_controller.order_history(
                        customer_id
                    )

                elif choice == 9:

                    self.review_controller.add_review(
                        customer_id
                    )

                elif choice == 10:

                    self.review_controller.view_reviews()

                elif choice == 11:

                    self.auth_controller.logout()
                    self.current_user = None

            except ValueError:
                print("\nError: Please enter a number.")

            except InvalidMenuChoiceError as e:
                print(f"\nError: {e}")

    def admin_menu(self):

        while self.current_user is not None:

            print("\n")
            print("=" * 40)
            print("            ADMIN MENU")
            print("=" * 40)
            print("1. Browse Products")
            print("2. Search Product")
            print("3. Search by Category")
            print("4. Add Product")
            print("5. Update Product")
            print("6. Delete Product")
            print("7. Logout")
            print("=" * 40)

            try:
                choice = int(input("Enter your choice: "))

                if choice not in range(1, 9):
                    raise InvalidMenuChoiceError(
                        "Invalid menu choice."
                    )

                customer_id = self.current_user.customer_id

                if choice == 1:

                    self.product_controller.show_products()

                elif choice == 2:

                    self.product_controller.search_by_name()

                elif choice == 3:

                    self.product_controller.search_by_category()

                elif choice == 4:

                    self.admin_controller.add_product(
                        self.current_user
                    )

                elif choice == 5:

                    self.admin_controller.update_product(
                        self.current_user
                    )

                elif choice == 6:

                    self.admin_controller.delete_product(
                        self.current_user
                    )

                elif choice == 7:

                    self.auth_controller.logout()
                    self.current_user = None

            except ValueError:
                print("\nError: Please enter a number.")

            except InvalidMenuChoiceError as e:
                print(f"\nError: {e}")


# Program Entry Point
if __name__ == "__main__":

    app = EcommerceApp()

    try:
        app.start()

    except KeyboardInterrupt:
        print("\n\nApplication closed.")

    except Exception as e:
        print(f"\nUnexpected error: {e}")
