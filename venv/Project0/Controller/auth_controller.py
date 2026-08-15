from getpass import getpass

from Project0.Service.auth_service import AuthService
from Project0.utils.file_handler import log_event

from Project0.exceptions.exceptions import (
    InvalidLoginError,
    DuplicateEmailError,
    ValidationError
)


class AuthController:

    def __init__(self):
        self.auth_service = AuthService()
        self.current_user = None

    def register(self):

        print("\n===== REGISTER =====")

        name = input("Enter name: ")
        email = input("Enter email: ")
        password = getpass("Enter password: ")
        phone = input("Enter phone: ")

        try:

            customer = self.auth_service.register(
                name,
                email,
                password,
                phone
            )

            print("\nRegistration successful!")
            print(f"Welcome, {customer.name}!")
            log_event(f"Customer registered: {customer.email}")

            return customer

        except DuplicateEmailError as e:
            print(f"Error: {e}")

        except ValidationError as e:
            print(f"Error: {e}")

        return None

    def login(self):

        print("\n===== LOGIN =====")

        email = input("Enter email: ")
        password = getpass("Enter password: ")

        try:

            customer = self.auth_service.login(
                email,
                password
            )

            self.current_user = customer

            print(
                f"\nWelcome back, {customer.name}!"
            )
            log_event(f"Customer logged in: {customer.email}")

            return customer

        except InvalidLoginError as e:
            print(f"Error: {e}")

        return None

    def logout(self):

        if self.current_user is None:
            print("\nNo user is currently logged in.")
            return

        print(
            f"\nGoodbye, {self.current_user.name}!"
        )

        log_event(f"Customer logged out: {self.current_user.email}")

        self.current_user = None
