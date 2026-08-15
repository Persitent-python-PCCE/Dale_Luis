from Project0.Dao.cart_dao import CartDAO
from Project0.Dao.product_dao import ProductDAO

from Project0.exceptions.exceptions import (
    InvalidProductError,
    NegativeQuantityError,
    InsufficientStockError,
    EmptyCartError
)


class CartService:

    def __init__(self):
        self.cart_dao = CartDAO()
        self.product_dao = ProductDAO()

    def get_or_create_cart(self, customer_id):

        cart = self.cart_dao.get_cart(customer_id)

        if cart:
            return cart["cart_id"]

        return self.cart_dao.create_cart(customer_id)

    def add_to_cart(
        self,
        customer_id,
        product_id,
        quantity
    ):

        if quantity <= 0:
            raise NegativeQuantityError(
                "Quantity must be greater than zero."
            )

        product = self.product_dao.get_product_by_id(
            product_id
        )

        if product is None:
            raise InvalidProductError(
                "Invalid product ID."
            )

        if product["stock"] < quantity:
            raise InsufficientStockError(
                "Insufficient stock."
            )

        cart_id = self.get_or_create_cart(
            customer_id
        )

        self.cart_dao.add_item(
            cart_id,
            product_id,
            quantity
        )

    def remove_from_cart(
        self,
        customer_id,
        product_id
    ):

        cart = self.cart_dao.get_cart(customer_id)

        if not cart:
            raise EmptyCartError(
                "Cart is empty."
            )

        removed = self.cart_dao.remove_item(
            cart["cart_id"],
            product_id
        )

        if not removed:
            raise InvalidProductError(
                "Product is not in the cart."
            )

    def view_cart(self, customer_id):

        cart = self.cart_dao.get_cart(customer_id)

        if not cart:
            raise EmptyCartError(
                "Cart is empty."
            )

        items = self.cart_dao.get_cart_items(
            cart["cart_id"]
        )

        if not items:
            raise EmptyCartError(
                "Cart is empty."
            )

        return items