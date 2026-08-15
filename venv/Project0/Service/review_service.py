from Project0.Dao.review_dao import ReviewDAO
from Project0.Dao.product_dao import ProductDAO

from Project0.exceptions.exceptions import (
    InvalidProductError,
    ValidationError
)


class ReviewService:

    def __init__(self):
        self.review_dao = ReviewDAO()
        self.product_dao = ProductDAO()

    def add_review(
        self,
        customer_id,
        product_id,
        rating,
        comment
    ):

        product = self.product_dao.get_product_by_id(
            product_id
        )

        if product is None:
            raise InvalidProductError(
                "Invalid product ID."
            )

        if rating < 1 or rating > 5:
            raise ValidationError(
                "Rating must be between 1 and 5."
            )

        if not comment.strip():
            raise ValidationError(
                "Comment cannot be empty."
            )

        return self.review_dao.add_review(
            customer_id,
            product_id,
            rating,
            comment
        )

    def get_reviews(self, product_id):

        product = self.product_dao.get_product_by_id(
            product_id
        )

        if product is None:
            raise InvalidProductError(
                "Invalid product ID."
            )

        return self.review_dao.get_product_reviews(
            product_id
        )