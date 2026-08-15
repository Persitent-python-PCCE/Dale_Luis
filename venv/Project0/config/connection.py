import mysql.connector

def get_connection():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dalerioluis",
        database="e_commerce"
    )
    
    return con