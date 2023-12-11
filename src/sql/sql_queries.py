import mysql.connector

def buscar_usuario_por_credenciales(cursor, correo_electronico, contraseña): # Busca si el ususario está en la base de datos
    query = f"SELECT * FROM Usuarios WHERE CorreoElectronico = '{correo_electronico}' AND Contraseña = '{contraseña}'"
    cursor.execute(query)
    resultado = cursor.fetchone()
    return resultado