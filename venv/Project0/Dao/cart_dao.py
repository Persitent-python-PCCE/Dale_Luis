from Project0.config.connection import get_connection

class CartDAO:
    def get_cart(self, customer_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = "SELECT cart_id FROM cart WHERE customer_id = %s"

        cursor.execute(q, (customer_id,))

        cart = cursor.fetchone()

        cursor.close()
        con.close()

        return cart

    def create_cart(self, customer_id):
        con = get_connection()
        cursor = con.cursor()

        q = "INSERT INTO cart (customer_id) VALUES (%s)"

        cursor.execute(q, (customer_id,))
        con.commit()

        id = cursor.lastrowid

        cursor.close()
        con.close()

        return id

    def add_item(self, cart_id, product_id, quantity):
        con = get_connection()
        cursor = con.cursor()

        q = """
        INSERT INTO cart_items
        (cart_id, product_id, quantity)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE
        quantity = quantity + VALUES(quantity)
        """

        cursor.execute(q,(cart_id, product_id, quantity))

        con.commit()

        cursor.close()
        con.close()

    def remove_item(self, cart_id, product_id):
        con = get_connection()
        cursor = con.cursor()

        q = "DELETE FROM cart_items WHERE cart_id = %s AND product_id = %s"

        cursor.execute(q, (cart_id, product_id))
        con.commit()

        affected = cursor.rowcount

        cursor.close()
        con.close()

        return affected > 0

    def get_cart_items(self, cart_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = """
        SELECT
            ci.cart_item_id,
            ci.product_id,p.product_name,p.price,
            p.stock,ci.quantity,
            (p.price * ci.quantity) AS subtotal
        FROM cart_items ci
        JOIN products p
        ON ci.product_id = p.product_id
        WHERE ci.cart_id = %s
        """

        cursor.execute(q, (cart_id,))

        items = cursor.fetchall()

        cursor.close()
        con.close()

        return items

    def clear_cart(self, cart_id):
        con = get_connection()
        cursor = con.cursor()

        q = "DELETE FROM cart_items WHERE cart_id = %s"

        cursor.execute(q, (cart_id,))
        con.commit()

        cursor.close()
        con.close()