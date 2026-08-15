from Project0.config.connection import get_connection

class CategoryDAO:
    def get_all_categories(self):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = "SELECT * FROM Categories"

        cursor.execute(q)

        categories = cursor.fetchall()

        cursor.close()
        con.close()

        return categories

    def get_category_by_id(self, category_id):
        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = "SELECT * FROM Categories WHERE category_id = %s"

        cursor.execute(q, (category_id,))

        category = cursor.fetchone()

        cursor.close()
        con.close()

        return category