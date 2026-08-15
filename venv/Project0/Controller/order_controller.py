from Project0.Service.order_service import OrderService
from Project0.utils.file_handler import backup_database, log_event
from Project0.exceptions.exceptions import (
    EmptyCartError,
    InvalidCouponError
)

class OrderController:

    def __init__(self):
        self.order_service = OrderService()

    def place_order(self, customer_id):

        print("\n===== CHECKOUT =====")

        coupon = input(
            "Enter coupon code (press Enter to skip): "
        ).strip()

        if coupon == "":
            coupon = None

        try:
            order = self.order_service.place_order(
                customer_id,
                coupon
            )

            log_event(
                f"Checkout completed: customer_id={customer_id}, "
                f"order_id={order['order_id']}"
            )

            try:
                backup_database()
            except Exception as backup_error:
                log_event(f"Database backup failed: {backup_error}")
                print("Order completed, but the CSV backup could not be created.")
            else:
                print("CSV backup created successfully.")

            print("\nOrder placed successfully!")
            print(f"Order ID: {order['order_id']}")
            print(f"Total Amount: ₹{order['total_amount']}")

        except EmptyCartError as e:
            print(f"Error: {e}")

        except InvalidCouponError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error: {e}")

    def order_history(self, customer_id):

        print("\n========== ORDER HISTORY ==========")

        try:
            orders = self.order_service.get_order_history(
                customer_id
            )

            if not orders:
                print("You have no previous orders.")
                return

            for order in orders:

                print(
                    f"Order ID: {order['order_id']}\n"
                    f"Order Date: {order['order_date']}\n"
                    f"Total: ₹{order['total_amount']}\n"
                    f"--------------------------"
                )

        except Exception as e:
            print(f"Error: {e}")
