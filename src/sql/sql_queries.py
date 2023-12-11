import mysql.connector

def buscar_usuario_por_credenciales(cursor, correo_electronico, contraseña): # Busca si el ususario está en la base de datos
    query = "SELECT * FROM Usuarios WHERE CorreoElectronico = %s AND Contraseña = %s"
    cursor.execute(query, (correo_electronico, contraseña))
    resultado = cursor.fetchone()
    return resultado