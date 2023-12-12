import mysql.connector

def connect_db():  # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="astralacademy"
    )
    return conexion
    
def get_cursor(conexion): # Obtener el cursor
    cursor = conexion.cursor()
    return cursor
        
def disconnect_db(conexion): # Desconecta la base de datos
    conexion.close()
            
def close_cursor(cursor): # Cierra el cursor
    cursor.close()
    
def connect_testing_db():  # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="testing"
    )
    return conexion
    
