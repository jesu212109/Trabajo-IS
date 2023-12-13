import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sql.sql_queries import consulta_actividades_academicas
from sql.sql_inserts import insertar_preinscripcion

class RegisteredScreen:
    def __init__(self, cursor, registered_window, registered_name):
        self.cursor = cursor
        self.registered_window = registered_window
        self.registered_name = registered_name
        self.registered_window.title(f"Bienvenido, {registered_name}")

        # Configurar la aplicación para iniciar en pantalla completa
        self.registered_window.attributes('-fullscreen', True)

        # Crear y configurar el marco principal
        main_frame = tk.Frame(self.registered_window)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # Crear botón para visualizar eventos
        events_button = tk.Button(main_frame, text="Ver Eventos", command=self.show_events)
        events_button.pack(pady=10)

        # Crear tabla para mostrar eventos
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Titulo", "Descripcion", "FechaInicio", "FechaFin", "Aforo", "Ubicacion", "Precio", "DerechosParticipacion"))
        self.tree.heading("#1", text="Titulo")
        self.tree.heading("#2", text="Descripcion")
        self.tree.heading("#3", text="FechaInicio")
        self.tree.heading("#4", text="FechaFin")
        self.tree.heading("#5", text="Aforo")
        self.tree.heading("#6", text="Ubicacion")
        self.tree.heading("#7", text="Precio")
        self.tree.heading("#8", text="DerechosParticipacion")
        self.tree.pack(pady=10)

        # Crear botón para preinscribirse
        preinscribe_button = tk.Button(main_frame, text="Preinscribirse", command=self.preinscribirse)
        preinscribe_button.pack(pady=10)

    def show_events(self):
        # Obtener datos de eventos
        events_data = consulta_actividades_academicas(self.cursor)

        # Limpiar la tabla antes de insertar nuevos datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos en la tabla
        for event in events_data:
            self.tree.insert("", "end", values=event[1:])  # Excluir la primera columna (IDEvento)

    def preinscribirse(self):
        
        messagebox.showinfo("Información", "Has sido preinscrito en la actividad seleccionada")
        
        # Verificar si se seleccionó una fila
        if not self.tree.selection():
            messagebox.showerror("Error", "Por favor, selecciona una actividad académica para preinscribirte.")
            return

        # Obtener la fila seleccionada
        selected_item = self.tree.selection()[0]

        # Obtener el ID de la actividad académica seleccionada
        activity_id = self.tree.item(selected_item, 'values')[0]

        # Verificar si el usuario ya está preinscrito
        self.cursor.execute("SELECT * FROM Preinscripciones WHERE IDUsuarioRegistrado = %s AND IDEvento = %s", (self.registered_name, activity_id))
        existing_preinscription = self.cursor.fetchone()

        if existing_preinscription:
            messagebox.showinfo("Información", "Ya estás preinscrito en esta actividad.")
        else:
            # Insertar preinscripción en la base de datos
            insertar_preinscripcion(self.cursor, activity_id, self.registered_name)
            messagebox.showinfo("Información", "Preinscripción exitosa.")

            # Actualizar la tabla de eventos
            self.show_events()
