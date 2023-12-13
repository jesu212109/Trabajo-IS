import tkinter as tk
from tkinter import messagebox
from sql.sql_queries import *
from sql.sql_inserts import *
from sql.sql_functions import *


class OrganizerScreen:
    def __init__(self, cursor, master, organizer_name):
        self.master = master
        self.cursor = cursor
        self.master.title("Pantalla de Organizador")

        # Configuración de estilo
        self.master.option_add('*Font', 'Arial 12')
        self.master.option_add('*Button.Background', '#4CAF50')  # Color de fondo del botón
        self.master.option_add('*Button.Foreground', 'white')    # Color del texto del botón
        self.master.option_add('*Button.Relief', 'flat')          # Tipo de relieve del botón

        # Configurar la aplicación para iniciar en pantalla completa
        self.master.attributes('-fullscreen', True)

        self.organizer_name = organizer_name

        self.create_widgets()

    def create_widgets(self):
        # Marco principal con fondo blanco
        main_frame = tk.Frame(self.master, bg='white')
        main_frame.pack(expand=True, fill='both')

        # Centrar verticalmente todos los elementos
        y_padding = int(self.master.winfo_screenheight() * 0.25)

        tk.Label(main_frame, text=f"Bienvenido, {self.organizer_name} (Organizador)").pack(pady=y_padding)

        tk.Label(main_frame, text="Nombre de la Actividad Académica:").pack(pady=5)
        self.activity_name_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.activity_name_var, width=40).pack(pady=5)

        tk.Button(main_frame, text="Crear Actividad", command=self.create_activity, width=20, height=2).pack(pady=10)

        tk.Button(main_frame, text="Salir", command=self.master.destroy, width=10, height=2).pack(pady=10)

    def create_activity(self):
        activity_name = self.activity_name_var.get()
        
        if not activity_name:
            messagebox.showerror("Error", "Por favor, ingrese un nombre para la actividad.")
            return
        
        try:
            insertar_nombre_actividad(self.cursor, activity_name)
        except Exception as e:
            messagebox.showerror("Error", e)

        messagebox.showinfo("Información", f"Actividad '{activity_name}' creada exitosamente.")