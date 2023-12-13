from src.sql.sql_queries import buscar_usuario_por_credenciales
from src.sql.sql_functions import connect_testing_db, get_cursor

def test_buscar_usuario_existente():
    # Establece la conexión a la base de datos de prueba
    conexion = connect_testing_db()

    # Obtiene el cursor
    cursor = get_cursor(conexion)


    # Inserta un usuario de prueba en la base de datos de prueba
    cursor.execute("""
        INSERT INTO Usuarios (IDUsuario, Nombre, CorreoElectronico, Contraseña, Rol)
        VALUES (1, 'UsuarioPrueba', 'prueba@example.com', 'password123', 'Visitante')
    """)

    # Asegúrate de que los cambios se guarden en la base de datos
    cursor._connection.commit()

    # Llama a la función que estás probando
    resultado = buscar_usuario_por_credenciales(cursor, "prueba@example.com", "password123")

    # Define la tupla esperada en lugar de un diccionario
    usuario_esperado = (1, 'UsuarioPrueba', 'prueba@example.com', 'password123', 'Visitante')

    # Imprime ambos valores para ayudar a depurar
    print("Resultado:", resultado)
    print("Esperado:", usuario_esperado)

    # Realiza el assert comparando el resultado con la tupla esperada
    assert resultado == usuario_esperado


    # Elimina el usuario de prueba de la base de datos
    cursor.execute("DELETE FROM Usuarios WHERE IDUsuario = 1")
    cursor._connection.commit()
        
    
