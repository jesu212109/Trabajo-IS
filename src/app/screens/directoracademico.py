import tkinter as tk
from tkinter import messagebox
from sql.sql_inserts import insertar_evento

class AcademicDirectorScreen:
    def __init__(self, cursor, master, director_name):
        self.master = master
        self.cursor = cursor
        self.master.title("Pantalla de Director Académico")

        # Configuración de estilo
        self.master.option_add('*Font', 'Arial 12')
        self.master.option_add('*Button.Background', '#4CAF50')  # Color de fondo del botón
        self.master.option_add('*Button.Foreground', 'white')    # Color del texto del botón
        self.master.option_add('*Button.Relief', 'flat')          # Tipo de relieve del botón

        # Configurar la aplicación para iniciar en pantalla completa
        self.master.attributes('-fullscreen', True)

        self.director_name = director_name

        self.create_widgets()

    def center_window(self):
        # Obtener el ancho y alto de la pantalla
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Obtener el ancho y alto del marco principal
        frame_width = self.master.winfo_reqwidth()
        frame_height = self.master.winfo_reqheight()

        # Calcular las coordenadas x y y para centrar la ventana
        x = int((screen_width - frame_width) / 2)
        y = int((screen_height - frame_height) / 2)

        # Establecer la geometría de la ventana centrada
        self.master.geometry(f"+{x}+{y}")

    def create_widgets(self):
        # Marco principal con fondo blanco
        main_frame = tk.Frame(self.master, bg='white')
        main_frame.pack(expand=True, fill='both', pady=(50, 0))  # Añadido pady para aumentar el espacio superior

        # Llamar a la función para centrar la ventana
        self.center_window()

        tk.Label(main_frame, text=f"Bienvenido, {self.director_name} (Director Académico)").pack(pady=50)

        tk.Label(main_frame, text="Crear Nuevo Evento Académico", font=('Arial', 16, 'bold')).pack(pady=10)

        tk.Label(main_frame, text="Título:").pack(pady=5)
        self.title_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.title_var, width=40).pack(pady=5)

        tk.Label(main_frame, text="Descripción:").pack(pady=5)
        self.description_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.description_var, width=40).pack(pady=5)

        tk.Label(main_frame, text="Fecha de Inicio (YYYY-MM-DD):").pack(pady=5)
        self.start_date_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.start_date_var, width=20).pack(pady=5)

        tk.Label(main_frame, text="Fecha de Fin (YYYY-MM-DD):").pack(pady=5)
        self.end_date_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.end_date_var, width=20).pack(pady=5)

        tk.Label(main_frame, text="Aforo:").pack(pady=5)
        self.capacity_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.capacity_var, width=10).pack(pady=5)

        tk.Label(main_frame, text="Ubicación:").pack(pady=5)
        self.location_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.location_var, width=40).pack(pady=5)

        tk.Label(main_frame, text="Precio:").pack(pady=5)
        self.price_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.price_var, width=10).pack(pady=5)

        tk.Label(main_frame, text="Derechos de Participación:").pack(pady=5)
        self.rights_var = tk.StringVar()
        tk.Entry(main_frame, textvariable=self.rights_var, width=40).pack(pady=5)

        tk.Button(main_frame, text="Crear Evento", command=self.create_event, width=20, height=2).pack(pady=10)

        tk.Button(main_frame, text="Salir", command=self.master.destroy, width=10, height=2).pack(pady=10)

    def create_event(self):
        title = self.title_var.get()
        description = self.description_var.get()
        start_date = self.start_date_var.get()
        end_date = self.end_date_var.get()
        capacity = self.capacity_var.get()
        location = self.location_var.get()
        price = self.price_var.get()
        rights = self.rights_var.get()

        # Verificar que los campos requeridos no estén vacíos
        if not (title and start_date and end_date and capacity and location):
            messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
            return

        try:
            insertar_evento(self.cursor, title, description, start_date, end_date, capacity, location, price, rights)
            messagebox.showinfo("Información", f"Evento '{title}' creado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", e)