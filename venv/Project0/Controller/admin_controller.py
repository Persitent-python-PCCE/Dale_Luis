from Project0.Service.product_service import ProductService
from Project0.utils.file_handler import backup_database, log_event

from Project0.exceptions.exceptions import (
    InvalidProductError,
    UnauthorizedError,
    ValidationError
)

class AdminController:

    def __init__(self):
        self.product_service = ProductService()

    def check_admin(self, customer):

        if customer is None:
            raise UnauthorizedError(
                "You must be logged in."
            )

        if customer.role.strip().upper() != "ADMIN":
            raise UnauthorizedError(
                "Admin access required."
            )

    def create_backup(self, action):
        try:
            backup_database()
            log_event(f"Admin product {action}; database backup created.")
            print("CSV backup created successfully.")
        except Exception as backup_error:
            log_event(
                f"Admin product {action}; database backup failed: {backup_error}"
            )
            print("Database change completed, but the CSV backup could not be created.")

    def add_product(self, customer):

        try:
            self.check_admin(customer)

            print("\n===== ADD PRODUCT =====")

            name = input("Product name: ").strip()
            description = input("Description: ").strip()

            price = float(
                input("Price: ")
            )

            stock = int(
                input("Stock: ")
            )

            category_id = int(
                input("Category ID: ")
            )

            supplier_id = int(
                input("Supplier ID: ")
            )

            self.product_service.add_product(
                name,
                description,
                price,
                stock,
                category_id,
                supplier_id
            )

            print("\nProduct added successfully.")
            self.create_backup("added")

        except UnauthorizedError as e:
            print(f"Error: {e}")

        except ValueError:
            print(
                "Price, stock, category ID and supplier ID "
                "must be valid numbers."
            )

        except ValidationError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    def update_product(self, customer):

        try:
            self.check_admin(customer)

            print("\n===== UPDATE PRODUCT =====")

            product_id = int(
                input("Product ID: ")
            )

            name = input("New product name: ").strip()
            description = input("New description: ").strip()
            price = float(input("New price: "))
            stock = int(input("New stock: "))
            category_id = int(input("New category ID: "))
            supplier_id = int(input("New supplier ID: "))

            self.product_service.update_product(
                product_id,
                name,
                description,
                price,
                stock,
                category_id,
                supplier_id
            )

            print("\nProduct updated successfully.")
            self.create_backup("updated")

        except UnauthorizedError as e:
            print(f"Error: {e}")

        except InvalidProductError as e:
            print(f"Error: {e}")

        except ValueError:
            print("Please enter valid values.")

        except ValidationError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    def delete_product(self, customer):

        try:
            self.check_admin(customer)

            print("\n===== DELETE PRODUCT =====")

            product_id = int(
                input("Enter product ID: ")
            )

            confirmation = input(
                "Are you sure? (y/n): "
            ).lower()

            if confirmation != "y":
                print("Delete cancelled.")
                return

            self.product_service.delete_product(
                product_id
            )

            print("Product deleted successfully.")
            self.create_backup("deleted")

        except UnauthorizedError as e:
            print(f"Error: {e}")

        except InvalidProductError as e:
            print(f"Error: {e}")

        except ValueError:
            print("Product ID must be a number.")

        except Exception as e:
            print(f"Error: {e}")
