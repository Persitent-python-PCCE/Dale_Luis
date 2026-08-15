from Project0.config.connection import get_connection
from Project0.Model.customer import Customer


class CustomerDAO:

    def create_customer(self, customer):

        con = get_connection()
        cursor = con.cursor()

        q = "INSERT INTO Customer (name, email, password, phone, role) VALUES (%s, %s, %s, %s, %s)"

        values = (customer.name,customer.email,customer.password,customer.phone,customer.role)

        cursor.execute(q, values)
        con.commit()

        customer.customer_id = cursor.lastrowid

        cursor.close()
        con.close()

        return customer

    def find_by_email(self, email):

        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = "SELECT * FROM Customer WHERE email = %s"

        cursor.execute(q, (email,))

        row = cursor.fetchone()

        cursor.close()
        con.close()

        if row is None:
            return None

        return Customer(customer_id=row["customer_id"],name=row["name"],email=row["email"],password=row["password"],phone=row["phone"],role=row["role"],created_at=row["created_at"])

    def find_by_id(self, customer_id):

        con = get_connection()
        cursor = con.cursor(dictionary=True)

        q = "SELECT * FROM Customer WHERE customer_id = %s"

        cursor.execute(q, (customer_id,))

        row = cursor.fetchone()

        cursor.close()
        con.close()

        if row is None:
            return None

        return Customer(customer_id=row["customer_id"],name=row["name"],email=row["email"],password=row["password"],phone=row["phone"],role=row["role"],created_at=row["created_at"])