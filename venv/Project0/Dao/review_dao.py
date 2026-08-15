from Project0.config.connection import get_connection

class ReviewDAO:

    def add_review(self,customer_id,product_id,rating,comment):
        con = get_connection()
        cursor = con.cursor()

        q = "INSERT INTO reviews (customer_id, product_id, rating, comment) VALUES (%s, %s, %s, %s)"

        cursor.execute(q,(customer_id,product_id,rating,comment))

        con.commit()

        review_id = cursor.lastrowid

        cursor.close()
        con.close()

        return review_id

    def get_product_reviews(self, product_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = """
        SELECT
            r.review_id,
            r.rating,
            r.comment,
            r.review_date,
            c.name AS customer_name
        FROM reviews r
        JOIN customer c
            ON r.customer_id = c.customer_id
        WHERE r.product_id = %s
        ORDER BY r.review_date DESC
        """

        cursor.execute(q, (product_id,))

        reviews = cursor.fetchall()

        cursor.close()
        con.close()

        return reviews