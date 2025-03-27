import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='GestionDeEstudiantes'
        )
        return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None