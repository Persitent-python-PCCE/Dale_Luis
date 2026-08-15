from datetime import datetime


class Order:

    def __init__(
        self,
        order_id=None,
        customer_id=None,
        order_date=None,
        total_amount=0.0
    ):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date or datetime.now()
        self.total_amount = total_amount

    def __str__(self):
        return (
            f"Order ID: {self.order_id} | "
            f"Customer ID: {self.customer_id} | "
            f"Total: ₹{self.total_amount}"
        )