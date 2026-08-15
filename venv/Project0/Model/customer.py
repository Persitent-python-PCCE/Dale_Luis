from datetime import datetime


class Customer:

    def __init__(
        self,
        customer_id=None,
        name=None,
        email=None,
        password=None,
        phone=None,
        role="CUSTOMER",
        created_at=None
    ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.role = role
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return f"{self.customer_id} | {self.name} | {self.email} | {self.role}"