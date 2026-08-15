from Project0.Dao.cart_dao import CartDAO
from Project0.Dao.order_dao import OrderDAO
from Project0.Dao.product_dao import ProductDAO

from Project0.exceptions.exceptions import (
    EmptyCartError,
    InsufficientStockError,
    InvalidProductError
)


class OrderService:

    def __init__(self):
        self.cart_dao = CartDAO()
        self.order_dao = OrderDAO()
        self.product_dao = ProductDAO()

    def place_order(self, customer_id, coupon=None):

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

        total = 0

        for item in items:

            product = self.product_dao.get_product_by_id(
                item["product_id"]
            )

            if product is None:
                raise InvalidProductError(
                    "Product no longer exists."
                )

            if product["stock"] < item["quantity"]:
                raise InsufficientStockError(
                    f"Insufficient stock for "
                    f"{product['product_name']}"
                )

            total += (
                item["price"] *
                item["quantity"]
            )

        order_id = self.order_dao.create_order(
            customer_id,
            total
        )

        for item in items:

            self.order_dao.add_order_detail(
                order_id,
                item["product_id"],
                item["quantity"],
                item["price"]
            )

            if not self.product_dao.reduce_stock(
                item["product_id"],
                item["quantity"]
            ):
                raise InsufficientStockError(
                    "Insufficient stock during checkout."
                )

        self.cart_dao.clear_cart(
            cart["cart_id"]
        )

        return {"order_id": order_id, "total_amount": total}

    def get_order_history(self, customer_id):

        return self.order_dao.get_orders_by_customer(
            customer_id
        )

    def order_details(self, order_id):

        return self.order_dao.get_order_details(
            order_id
        )
