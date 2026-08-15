from Project0.config.connection import get_connection


class OrderDAO:

    def create_order(self, customer_id, total_amount):
        
        con = get_connection()
        cursor = con.cursor()

        q = "INSERT INTO orders (customer_id, total_amount)VALUES (%s, %s)"

        cursor.execute(q,(customer_id, total_amount))

        con.commit()

        order_id = cursor.lastrowid

        cursor.close()
        con.close()

        return order_id

    def add_order_detail(self,order_id,product_id,quantity,price):
        con = get_connection()
        cursor = con.cursor()

        q = "INSERT INTO order_details (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"

        cursor.execute(q,(order_id,product_id,quantity,price))

        con.commit()

        cursor.close()
        con.close()

    def get_orders_by_customer(self, customer_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = """
        SELECT
            order_id,
            customer_id,
            order_date,
            total_amount
        FROM orders
        WHERE customer_id = %s
        ORDER BY order_date DESC
        """

        cursor.execute(q, (customer_id,))

        orders = cursor.fetchall()

        cursor.close()
        con.close()

        return orders

    def get_order_details(self, order_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = """
        SELECT
            od.order_detail_id,
            od.product_id,
            p.product_name,
            od.quantity,
            od.price,
            (od.quantity * od.price) AS subtotal
        FROM order_details od
        JOIN products p
        ON od.product_id = p.product_id
        WHERE od.order_id = %s
        """

        cursor.execute(q, (order_id,))

        details = cursor.fetchall()

        cursor.close()
        con.close()

        return details