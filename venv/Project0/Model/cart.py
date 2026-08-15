from datetime import datetime


class Cart:

    def __init__(
        self,
        cart_id=None,
        customer_id=None,
        created_at=None
    ):
        self.cart_id = cart_id
        self.customer_id = customer_id
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return f"Cart ID: {self.cart_id} | Customer ID: {self.customer_id}"