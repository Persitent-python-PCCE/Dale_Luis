class InvalidLoginError(Exception):
    pass


class DuplicateEmailError(Exception):
    pass


class InvalidProductError(Exception):
    pass


class NegativeQuantityError(Exception):
    pass


class InsufficientStockError(Exception):
    pass


class EmptyCartError(Exception):
    pass


class InvalidCouponError(Exception):
    pass


class InvalidMenuChoiceError(Exception):
    pass


class DatabaseConnectionError(Exception):
    pass


class UnauthorizedError(Exception):
    pass


class ValidationError(Exception):
    pass