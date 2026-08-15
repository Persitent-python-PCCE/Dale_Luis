from Project0.config.connection import get_connection
from Project0.Model.product import Product

class ProductDAO:
    def add_product(self,product):
        con= get_connection()
        cursor = con.cursor()
        q="INSERT INTO Products (product_name,p_description,price,stock,category_id,supplier_id,is_active) values (%s,%s,%s,%s,%s,%s,%s)"
        v = (product.product_name, product.p_description, product.price,
             product.stock, product.category_id, product.supplier_id,
             product.is_active)
        cursor.execute(q,v)
        con.commit()
        id=cursor.lastrowid
        
        cursor.close()
        con.close()
        
        return id
        
        
    def update_product(self, product):
        con= get_connection()
        cursor = con.cursor()
        q="""UPDATE Products
        SET 
            product_name=%s,
            p_description=%s, price=%s, stock=%s,
            category_id=%s, supplier_id=%s 
        WHERE product_id =%s
        """
        v = (product.product_name, product.p_description, product.price,
           product.stock, product.category_id, product.supplier_id,
           product.product_id)
        
        cursor.execute(q,v)
        con.commit()
        
        affected_rows=cursor.rowcount
        
        cursor.close()
        con.close()
        
        return affected_rows>0
    
    def delete_product(self, product_id):
        con = get_connection()
        cursor = con.cursor()

        q = """
            UPDATE products
            SET is_active = 0
            WHERE product_id = %s
        """
        
        cursor.execute(q, (product_id,))
        con.commit()

        affected_rows = cursor.rowcount

        cursor.close()
        con.close()

        return affected_rows > 0

    def reduce_stock(self, product_id, quantity):
        con = get_connection()
        cursor = con.cursor()

        cursor.execute(
            """
            UPDATE Products
            SET stock = stock - %s
            WHERE product_id = %s AND stock >= %s
            """,
            (quantity, product_id, quantity)
        )
        con.commit()

        reduced = cursor.rowcount > 0
        cursor.close()
        con.close()

        return reduced
        
    def get_all_products(self):
        con= get_connection()
        cursor = con.cursor(dictionary=True)
        q = """
        SELECT
            p.product_id,p.product_name,
            p.p_description,p.price,p.stock,
            p.category_id,c.category_name,
            p.supplier_id,p.is_active
        FROM Products p
        JOIN Categories c
        ON p.category_id = c.category_id
        WHERE p.is_active = 1
        """
        cursor.execute(q)
        rows=cursor.fetchall()
        
        cursor.close()
        con.close()
        
        return [self._to_product(row) for row in rows]

    def get_product_by_id(self, product_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM Products WHERE product_id = %s AND is_active = 1",
            (product_id,)
        )
        product = cursor.fetchone()
        cursor.close()
        con.close()
        return product
    
    def search_by_name(self, name):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = "SELECT * FROM Products WHERE product_name LIKE %s AND is_active = 1"

        cursor.execute(q, (f"%{name}%",))

        rows = cursor.fetchall()

        cursor.close()
        con.close()

        return [self._to_product(row) for row in rows]

    def search_by_category(self, category_name):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = """
            SELECT p.*, c.category_name
            FROM Products p
            JOIN Categories c
            ON p.category_id = c.category_id
            WHERE c.category_name LIKE %s
            AND p.is_active = 1
        """

        cursor.execute(q, (f"%{category_name}%",))

        rows = cursor.fetchall()

        cursor.close()
        con.close()

        return [self._to_product(row) for row in rows]

    @staticmethod
    def _to_product(row):
        return Product(
            product_id=row["product_id"],
            product_name=row["product_name"],
            p_description=row["p_description"],
            price=row["price"],
            stock=row["stock"],
            category_id=row["category_id"],
            supplier_id=row["supplier_id"],
            is_active=row["is_active"]
        )
