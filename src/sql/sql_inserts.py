import datetime

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
        cursor._connection.commit()

    except Exception as e:
        raise e
    

def insertar_evento(cursor, titulo, descripcion, fecha_inicio, fecha_fin, aforo, ubicacion, precio, derechos):
    
    s = "El evento no está registrado en la base de datos"
    
    try:
        # Validar las fechas
        try:
            fecha_inicio = datetime.datetime.strptime(fecha_inicio, "%Y-%m-%d").date()
            fecha_fin = datetime.datetime.strptime(fecha_fin, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Formato de fecha incorrecto. Utilice el formato 'YYYY-MM-DD'.")

        # Verificar si el título ya existe en la tabla
        cursor.execute("SELECT * FROM Eventos WHERE Titulo = %s", (titulo,))
        existing_event = cursor.fetchone()

        # Si el evento ya existe, realizar una actualización
        if existing_event:
            query = """
                UPDATE Eventos
                SET Descripcion = %s, FechaInicio = %s, FechaFin = %s, Aforo = %s, Ubicacion = %s, Precio = %s, DerechosParticipacion = %s
                WHERE Titulo = %s
            """
            values = (descripcion, fecha_inicio, fecha_fin, aforo, ubicacion, precio, derechos, titulo)
        else:
            raise ValueError("El evento no está registrado en la base de datos.")

        # Ejecutar la consulta
        cursor.execute(query, values)

        # Confirmar la transacción
        cursor._connection.commit()

        print(f"Evento '{titulo}' insertado/actualizado exitosamente.")
    except Exception as e:
        raise e

