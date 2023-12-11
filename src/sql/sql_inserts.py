def insertar_nombre_actividad(cursor, nombre_actividad):
    try:
        # Consulta para insertar el nombre de la actividad en la tabla Eventos
        query = """
            INSERT INTO Eventos (Titulo, Descripcion, FechaInicio, FechaFin, Aforo, Ubicacion, Precio, DerechosParticipacion, IDUsuarioOrganizador)
            VALUES (%s, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)
        """

        # Parámetros para la consulta
        values = (nombre_actividad,)

        # Ejecutar la consulta
        cursor.execute(query, values)

        # Confirmar la transacción
        cursor.connection.commit()

        print(f"Nombre de actividad '{nombre_actividad}' insertado exitosamente.")
    except Exception as e:
        print(f"Error al insertar el nombre de la actividad: {e}")
