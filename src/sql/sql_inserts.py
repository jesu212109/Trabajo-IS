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
    
def insertar_preinscripcion(cursor, id_usuario, id_evento):
    try:
        # Verificar si ya existe una preinscripción para el usuario y evento especificados
        cursor.execute("SELECT * FROM Preinscripciones WHERE IDUsuarioRegistrado = %s AND IDEvento = %s", (id_usuario, id_evento))
        existing_preinscription = cursor.fetchone()

        if existing_preinscription:
            raise ValueError("Ya estás preinscrito en esta actividad.")
        else:
            # Insertar nueva preinscripción
            cursor.execute("INSERT INTO Preinscripciones (IDEvento, IDUsuarioRegistrado) VALUES (%s, %s)", (id_evento, id_usuario))

            # Confirmar la transacción
            cursor._connection.commit()

            print("Preinscripción exitosa.")
    except Exception as e:
        raise e

