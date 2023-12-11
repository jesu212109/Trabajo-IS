import tkinter as tk
from tkinter import messagebox
from sql.sql_queries import buscar_usuario_por_credenciales
from sql.sql_functions import *

class LoginApp:
    def __init__(self, root, cursor):
        self.root = root
        self.cursor = cursor
        self.root.title("Login App")
        self.root.geometry("1920x1080")

        self.create_widgets()

    def create_widgets(self):
        # Variables para almacenar la entrada del usuario
        self.correo_var = tk.StringVar()
        self.contraseña_var = tk.StringVar()

        # Etiquetas y entradas para el correo y la contraseña
        tk.Label(self.root, text="Correo electrónico:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.correo_var, width=40).pack(pady=5)
        
        tk.Label(self.root, text="Contraseña:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.contraseña_var, show="*", width=40).pack(pady=5)

        # Botón para realizar el inicio de sesión
        tk.Button(self.root, text="Iniciar Sesión", command=self.login, width=20, height=2).pack(pady=10)

    def login(self):
        # Obtener las credenciales del usuario
        correo_electronico = self.correo_var.get()
        contraseña = self.contraseña_var.get()

        # Realizar el inicio de sesión
        resultado = buscar_usuario_por_credenciales(self.cursor, correo_electronico, contraseña)

        if resultado:
            # Si las credenciales son correctas, abrir la nueva pantalla
            self.open_success_screen(resultado)
        else:
            # Mostrar un mensaje de error en caso de credenciales incorrectas
            messagebox.showerror("Error", "Contraseña incorrecta")

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