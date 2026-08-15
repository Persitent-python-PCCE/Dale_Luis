from Project0.Service.review_service import ReviewService

class ReviewController:

    def __init__(self):
        self.review_service = ReviewService()

    def add_review(self, customer_id):

        print("\n===== ADD REVIEW =====")

        try:
            product_id = int(
                input("Product ID: ")
            )

            rating = int(
                input("Rating (1-5): ")
            )

            comment = input(
                "Comment: "
            ).strip()

            self.review_service.add_review(
                customer_id,
                product_id,
                rating,
                comment
            )

            print("Review added successfully.")

        except ValueError:
            print("Product ID and rating must be numbers.")

        except Exception as e:
            print(f"Error: {e}")

    def view_reviews(self):

        print("\n===== PRODUCT REVIEWS =====")

        try:
            product_id = int(
                input("Product ID: ")
            )

            reviews = self.review_service.get_reviews(
                product_id
            )

            if not reviews:
                print("No reviews found.")
                return

            for review in reviews:

                print(
                    f"Rating: {review['rating']}/5\n"
                    f"Comment: {review['comment']}\n"
                    f"Date: {review['review_date']}\n"
                    f"-------------------------"
                )

        except ValueError:
            print("Product ID must be a number.")

        except Exception as e:
            print(f"Error: {e}")