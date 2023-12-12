import tkinter as tk
from tkinter import messagebox
from sql.sql_queries import *
from sql.sql_inserts import *
from sql.sql_functions import *
from app.screens.organizer import OrganizerScreen


class LoginApp:

    def __init__(self, root, cursor):
        self.root = root
        self.cursor = cursor
        self.root.title("Login App")
        
        # Configuración de estilo
        self.root.option_add('*Font', 'Arial 12')
        self.root.option_add('*Button.Background', '#4CAF50')  # Color de fondo del botón
        self.root.option_add('*Button.Foreground', 'white')    # Color del texto del botón
        self.root.option_add('*Button.Relief', 'flat')          # Tipo de relieve del botón

        # Configurar la aplicación para iniciar en pantalla completa
        self.root.attributes('-fullscreen', True)

        self.create_widgets()

    def create_widgets(self):
        # Variables para almacenar la entrada del usuario
        self.correo_var = tk.StringVar()
        self.contraseña_var = tk.StringVar()

        # Marco principal con fondo blanco
        main_frame = tk.Frame(self.root, bg='#F0F0F0')  # Fondo gris claro
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)  # Agregado espacio alrededor del marco

        # Centrar verticalmente todos los elementos
        y_padding = int(self.root.winfo_screenheight() * 0.25)

        # Título AstralAcademy
        title_label = tk.Label(main_frame, text="AstralAcademy", font=('Arial', 24, 'bold'), bg='#F0F0F0')  # Fondo gris claro
        title_label.pack(pady=(y_padding, 10))

        # Etiquetas y entradas para el correo y la contraseña
        tk.Label(main_frame, text="Correo electrónico:", font=('Arial', 14), bg='#F0F0F0').pack(pady=5)
        tk.Entry(main_frame, textvariable=self.correo_var, width=40, font=('Arial', 12)).pack(pady=5)

        tk.Label(main_frame, text="Contraseña:", font=('Arial', 14), bg='#F0F0F0').pack(pady=5)
        tk.Entry(main_frame, textvariable=self.contraseña_var, show="*", width=40, font=('Arial', 12)).pack(pady=5)

        # Botón para realizar el inicio de sesión
        login_button = tk.Button(main_frame, text="Iniciar Sesión", command=self.login, width=20, height=2)
        login_button.pack(pady=20)  # Aumentado espacio debajo del botón
        
    def login(self):
        # Obtener las credenciales del usuario
        correo_electronico = self.correo_var.get()
        contraseña = self.contraseña_var.get()

        # Realizar el inicio de sesión
        resultado = buscar_usuario_por_credenciales(self.cursor, correo_electronico, contraseña)

        if resultado:
        # Desempaquetar la información del usuario
            _, nombre, correo_electronico, _, rol = resultado

        # Determinar el caso según el rol
        if rol == "Organizador":
            self.open_organizer_screen(nombre)
        elif rol == "Visitante":
            self.open_visitor_screen(nombre)
        elif rol == "DirectorAcademico":
            self.open_academic_director_screen(nombre)
        elif rol == "Ponente":
            self.open_speaker_screen(nombre)
        elif rol == "Registrado":
            self.open_registered_screen(nombre)
        else:
            messagebox.showerror("Error, usuario no encontrado")
    
    def open_organizer_screen(self, organizer_name):
        organizer_window = tk.Toplevel(self.root)  # Utiliza Toplevel en lugar de Tk
        organizer_screen = OrganizerScreen(self.cursor, organizer_window, organizer_name)

    def open_success_screen(self, user_data):
        # Cerrar la ventana actual
        self.root.destroy()

        # Crear una nueva ventana para la pantalla de éxito
        success_window = tk.Tk()
        success_window.title("Login Exitoso")

        # Mostrar la información del usuario
        tk.Label(success_window, text=f"Bienvenido, {user_data[1]}").pack(pady=10)

        # Agregar más elementos según sea necesario para la nueva pantalla

        success_window.mainloop()