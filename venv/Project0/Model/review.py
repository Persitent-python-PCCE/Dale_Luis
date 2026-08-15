from datetime import datetime


class Review:

    def __init__(
        self,
        review_id=None,
        customer_id=None,
        product_id=None,
        rating=None,
        comment=None,
        review_date=None
    ):
        self.review_id = review_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment
        self.review_date = review_date or datetime.now()

    def __str__(self):
        return (
            f"Product ID: {self.product_id} | "
            f"Rating: {self.rating}/5 | "
            f"Comment: {self.comment}"
        )