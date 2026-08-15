import re
import bcrypt

from Project0.Dao.customer_dao import CustomerDAO
from Project0.Model.customer import Customer

from Project0.exceptions.exceptions import (
    InvalidLoginError,
    DuplicateEmailError,
    ValidationError
)


class AuthService:

    def __init__(self):
        self.customer_dao = CustomerDAO()

    def register(self, name, email, password, phone):

        if not name.strip():
            raise ValidationError("Name cannot be empty.")

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email):
            raise ValidationError("Invalid email.")

        if len(password) < 6:
            raise ValidationError("Password must contain at least 6 characters.")

        existing = self.customer_dao.find_by_email(email)

        if existing:
            raise DuplicateEmailError(
                "Email already registered."
            )

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        customer = Customer(
            name=name,
            email=email,
            password=hashed_password,
            phone=phone,
            role="CUSTOMER"
        )

        return self.customer_dao.create_customer(customer)

    def login(self, email, password):

        customer = self.customer_dao.find_by_email(email)

        if customer is None:
            raise InvalidLoginError(
                "Invalid email or password."
            )

        password_match = bcrypt.checkpw(
            password.encode("utf-8"),
            customer.password.encode("utf-8")
        )

        if not password_match:
            raise InvalidLoginError(
                "Invalid email or password."
            )

        return customer