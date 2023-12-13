import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from sql.sql_queries import *
from sql.sql_inserts import *
from sql.sql_functions import *
from app.screens.organizer import *
from app.screens.directoracademico import *

class VisitorScreen:
    def __init__(self, cursor, visitor_window, visitor_name):
        self.cursor = cursor
        self.visitor_window = visitor_window
        self.visitor_name = visitor_name
        self.visitor_window.title(f"Bienvenido, {visitor_name}")
        
        # Configurar la aplicación para iniciar en pantalla completa
        self.visitor_window.attributes('-fullscreen', True)

        # Crear y configurar el marco principal
        main_frame = tk.Frame(self.visitor_window)
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

    def show_events(self):
        # Obtener datos de eventos
        events_data = consulta_actividades_academicas(self.cursor)

        # Limpiar la tabla antes de insertar nuevos datos
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar datos en la tabla
        for event in events_data:
            self.tree.insert("", "end", values=event[1:])  # Excluir la primera columna (IDEvento)

